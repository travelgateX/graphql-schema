#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

import os
import graphql
import sys
import glob
import datetime
import utils
import tempfile
import urllib
from optparse import OptionParser
from logger import LogClient
from gists import GistFile, GObject
from graphql_client import GraphQLClient

class CallbackException(Exception):
    pass

def recursive_glob(rootdir='.', suffix=''):
    files = []
    for root, dirnames, filenames in os.walk(rootdir):
        files.extend(glob.glob(root + "/*" + suffix))
    return files

def call_callback(gobject, logger, gist):
    with open(os.path.join(os.path.dirname(__file__), "callback.py"), "w") as temp_file:
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
            raise CallbackException(e.message)
    except CallbackException as ex_callback:
        logger.writeLog("Error into callback, error message: " + ex_callback.message, utils.LOG_LEVEL.ERROR)
    except Exception as e:
        logger.writeLog("Error importing callback or executing query: " + e.message, utils.LOG_LEVEL.ERROR)
    finally:
        del sys.modules['callback']
        os.remove(os.path.join(os.path.dirname(__file__), "callback.py"))
        if os.path.exists(os.path.join(os.path.dirname(__file__), "callback.pyc")):
            os.remove(os.path.join(os.path.dirname(__file__), "callback.pyc"))
    return check

parser = OptionParser()
parser.add_option("-p", "--path", dest="path_search",
                  help="Specify the PATH relative to graphql-schema repo dir", metavar="PATH")
parser.add_option("-v", "--verbose", action="store_true", default=False, dest="verbose", help="Show more output message")


(options, args) = parser.parse_args()
# Initialize Logger
logger = LogClient(os.path.join(os.path.dirname(__file__),datetime.datetime.now().strftime("%Y%m%d-%H%M")))

# Store arguments and check them
path_search = options.path_search
utils.setVerbose(options.verbose)
if not path_search:
    logger.writeLog ("ERROR: Wrong argument for microservice path", utils.LOG_LEVEL.ERROR)
    parser.print_help()
    sys.exit(-1)

# Initialize graphql client
graphql_client = GraphQLClient(utils.GRAPH_URL)
graphql_client.inject_token(utils.GRAPH_TOKEN)

# Clean cache
urllib.urlcleanup()

# Get all gist for that direcotry and subdirs
for path_file in recursive_glob(os.path.join(os.path.abspath("."), path_search), '.gist'):
    logger.writeLog("===================================================")
    gist_file = GistFile(path_file)
    filename = os.path.basename(path_file)
    logger.writeLog("Checking Gists into file: " + filename)
    for gist in gist_file.get_all_gists():
        logger.writeLog("\n")
        gobject = gist_file.extract_function_gist(gist)

        if utils.getVerbose:
            logger.writeLog("Checking gist: " + gist.gid)
            logger.writeLog(str(gist))
            if gist.type == utils.GIST_TYPE.DOC:
                logger.writeLog("Avoid this gist cause is a Documentation gist")
                continue
        if "404: Not Found" in gobject.query:
            logger.writeLog("Error downloading gist from GitHub with id " + gobject.gist_info.gid, utils.LOG_LEVEL.ERROR)
            continue
        if gist.check_type == utils.GIST_CHECK_TYPE.JSON:
            if "404: Not Found" in gobject.result:
                logger.writeLog("Error downloading gist from GitHub with id " + gobject.gist_info.gid, utils.LOG_LEVEL.ERROR)
                continue
            check = graphql_client.check_result(gobject.query, gobject.result)
        else:
            if "404: Not Found" in gobject.callback:
                logger.writeLog("Error downloading gist from GitHub with id " + gobject.gist_info.gid, utils.LOG_LEVEL.ERROR)
                continue
            check = call_callback(gobject, logger, gist)
                
        logger.writeLog("Gist: " + gist.gid + " Passed: " + str(check))
        logger.writeLog("\n")
    logger.writeLog("===================================================")


