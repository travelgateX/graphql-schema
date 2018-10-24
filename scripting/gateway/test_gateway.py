#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import datetime
import utils
import tempfile
from optparse import OptionParser
from logger import LogClient
from gists import GistFile, GObject
from graphql_client import GraphQLClient

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"


class CallbackException(Exception):
    def __init__(self, message):
        super().__init__(message)


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
# Store arguments and check them
path_search = options.path_search
utils.setVerbose(options.verbose)
if not path_search:
    logger.writeLog(
        "ERROR: Wrong argument for microservice path",
        utils.LOG_LEVEL.ERROR
    )
    parser.print_help()
    sys.exit(-1)

# Initialize graphql client
graphql_client = GraphQLClient(utils.GRAPH_URL)
graphql_client.inject_token(utils.GRAPH_TOKEN)


# Get all gist for that direcotry and subdirs


repository_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    ".."
)

full_path_search = os.path.join(repository_path, path_search)

gists_files = recursive_glob(full_path_search, '.gist')
print (gists_files)
for path_file in gists_files:
    logger.writeLog("===================================================")
    gist_file = GistFile(path_file)
    filename = os.path.basename(path_file)
    logger.writeLog("Checking Gists into file: " + filename)
    for gist in gist_file.get_all_gists():
        logger.writeLog("\n")
        gobject = gist_file.extract_function_gist(gist)
        check = False
        if utils.getVerbose():
            logger.writeLog("Checking gist: " + gist.gid)
            logger.writeLog(str(gist))
            if gist.type == utils.GIST_TYPE.DOC:
                logger.writeLog("Avoid this gist cause is a Documentation gist")
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
