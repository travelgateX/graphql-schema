#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
import datetime
import utils
import tempfile
import threading
import traceback    
from optparse import OptionParser
from logger import LogClient
from gists import GistFile, GObject, extract_function_gist, GistObject
from graphql_client import GraphQLClient


__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

LOCK = threading.Lock()


class CallbackException(Exception):
    def __init__(self, message):
        super().__init__(message)


def writeLogThreading(logger, message, level=utils.LOG_LEVEL.LOG):
    LOCK.acquire()
    logger.writeLog(message, level)
    LOCK.release()


def callback_stress(gobject, logger, gist):
    check = True
    result = graphql_client.execute(gobject.query)
    try:
        if utils.getVerbose():
            
            writeLogThreading(logger, "Executing callback")
        if not result or "errors" in result:
            #writeLogThreading(logger, "Error for gist: " + gobject.gist_info.gid, utils.LOG_LEVEL.ERROR)
            writeLogThreading(logger, "Error: " + str(result), utils.LOG_LEVEL.ERROR)
            if utils.getVerbose():
                writeLogThreading(logger, "With query: ", utils.LOG_LEVEL.ERROR)
                writeLogThreading(logger, gobject.query, utils.LOG_LEVEL.ERROR)
            check = False
        else:
            for org in result['data']['admin']['organizations']['edges']:
                if org['node']['adviseMessage']:
                    #writeLogThreading(logger, "Error for gist: " + gobject.gist_info.gid, utils.LOG_LEVEL.ERROR)
                    writeLogThreading(logger, str(org['node']['adviseMessage'][0]['description']),utils.LOG_LEVEL.ERROR)
                    check = False

    except Exception as e:
        writeLogThreading(logger, 
            "Error into callback_stress or executing query: " + str(e),
            utils.LOG_LEVEL.ERROR
        )
        
        check = False
    return check


def recursive_glob(rootdir='.', suffix=''):
    files = []
    for root, dirnames, filenames in os.walk(rootdir):
        files.extend(glob.glob(root + "/*" + suffix))
    return files


def call_callback(gobject, logger, gist):
    callback_file = os.path.join(os.path.dirname(__file__), "callback.py")
    with open(callback_file, "w") as temp_file:
        temp_file.write(gobject.callback)
    check = False
    try:
        if utils.getVerbose():
            logger.writeLog("Executing callback")
            logger.writeLog(gobject.callback)
        callback_module = __import__('callback')
        callback_method = getattr(callback_module, "callback")
        response_result = graphql_client.execute(gobject.query)
        try:
            check = callback_method(gobject, response_result, logger)
        except Exception as e:
            raise CallbackException(e)
    except CallbackException as ex_callback:
        logger.writeLog(
            "Error into callback, error message: " + str(ex_callback),
            utils.LOG_LEVEL.ERROR
        )
    except Exception as e:
        logger.writeLog(
            "Error importing callback or executing query: " + str(e),
            utils.LOG_LEVEL.ERROR
        )
    finally:
        del sys.modules['callback']
        os.remove(callback_file)
        if os.path.exists(callback_file + "c"):
            os.remove(callback_file + "c")
    return check


def stress_test(logger):
    id_gist_stress = "0f584e164a99758ed61423ddd510928c"
    user_stress = "amian84"
    gist_object = GistObject(0, user_stress, id_gist_stress, id_gist_stress, 0, 2, 1)
    gobject = extract_function_gist(gist_object)
    threads = []
    for i in range(500):
        thread = threading.Thread(target=excute_stress_command, args=[i, gobject, logger, gist_object])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def excute_stress_command(t_id, gobject, logger, gist_object):
    check = callback_stress(gobject, logger, gist_object)
    logger.writeLog("Thread: " + str(t_id) + " Passed: " + str(check))
    logger.writeLog("\n")


def check_404(downloaded_str, logger, gobject):
    if "404: Not Found" in downloaded_str:
        err_message = "Error downloading gist from GitHub with id "
        err_message += gobject.gist_info.gid
        logger.writeLog(
            err_message,
            utils.LOG_LEVEL.ERROR)
        logger.writeResult(
            gobject.gist_info.gid,
            check,
            gobject.gist_info.level)
        return True
    return False

parser = OptionParser()
parser.add_option(
    "-p", "--path",
    dest="path_search",
    help="Specify the PATH relative to graphql-schema repo dir",
    metavar="PATH"
)
parser.add_option(
    "-f", "--file",
    dest="file_gist",
    help="FILE path of gist file relative to graphql-schema repodir",
    metavar="FILE"
)
parser.add_option(
    "-s", "--stress",
    action="store_true",
    dest="stress",
    help="Make a stress test"    
)
parser.add_option(
    "-v",
    "--verbose",
    action="store_true",
    default=False,
    dest="verbose",
    help="Show more output message"
)


(options, args) = parser.parse_args()
# Initialize Logger
# logger = LogClient(
#                    os.path.join(os.path.dirname(__file__),
#                    datetime.datetime.now().strftime("%Y%m%d")))
logger = LogClient(os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "logger"
                    ))
logger.rotateLogs()

check_bearer = (
    utils.GRAPH_TOKEN.startswith("Bearer") or
    utils.GRAPH_TOKEN.startswith("Apikey")
    )
if not check_bearer:
    logger.writeLog(
        "Please configure your token into utils/constants.py file",
        utils.LOG_LEVEL.ERROR
    )
    sys.exit(-1)


# Store arguments and check them
path_search = options.path_search
file_gist = options.file_gist
stress_value = options.stress
utils.setVerbose(options.verbose)

# Initialize graphql client
graphql_client = GraphQLClient(utils.GRAPH_URL)
graphql_client.inject_token(utils.GRAPH_TOKEN)

if not path_search and not file_gist:
    if not stress_value:
        logger.writeLog(
            "ERROR: You must select path or filename to work",
            utils.LOG_LEVEL.ERROR
        )
        parser.print_help()
        sys.exit(-1)
    else:
        stress_test(logger)
        sys.exit(0)

gists_files = []


# Get all gist for that direcotry and subdirs
repository_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    ".."
)

if path_search:
    full_path_search = os.path.join(repository_path, path_search)
    gists_files = recursive_glob(full_path_search, '.gist')
else:
    gists_files.append(os.path.join(repository_path, file_gist))

for path_file in gists_files:
    logger.writeLog("===================================================")
    gist_file = GistFile(path_file)
    filename = os.path.basename(path_file)
    logger.writeLog("Checking Gists into file: " + filename)
    for gist in gist_file.get_all_gists():
        logger.writeLog("\n")
        gobject = extract_function_gist(gist)
        check = False
        if utils.getVerbose():
            logger.writeLog("Checking gist: " + gist.gid)
            logger.writeLog(str(gist))
            if gist.type == utils.GIST_TYPE.DOC:
                logger.writeLog(
                    "Avoid this gist cause is a Documentation gist"
                )
                continue
        if check_404(gobject.query, logger, gobject):
            continue
        if gist.check_type == utils.GIST_CHECK_TYPE.JSON:
            if check_404(gobject.result, logger, gobject):
                continue
            check = graphql_client.check_result(gobject.query, gobject.result)
        else:
            if check_404(gobject.callback, logger, gobject):
                continue
            check = call_callback(gobject, logger, gist)
        logger.writeLog("Gist: " + gist.gid + " Passed: " + str(check))
        logger.writeLog("\n")
        logger.writeResult(gist.gid, check, gist.level)
    logger.writeLog("===================================================")
