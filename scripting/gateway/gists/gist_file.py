#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import utils
from logger import LogClient

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

QUERY_FILE = "query.graphql"
RESULT_FILE = "result.json"
CALLBACK_FILE = "callback.py"
BASE_URL = "https://gist.githubusercontent.com/$$USER$$/$$GID$$/"
RAW = "raw/$$FILE$$"


class GObject:
    def __init__(self, gist_info, query, result, callback):
        self.gist_info = gist_info
        self.query = query
        self.result = result
        self.callback = callback


class GistObject:
    def __init__(self, idJson, user, gid, gidbk, type_gist, level, ctype):
        self.idJson = idJson
        self.user = user
        self.gid = gid
        self.gidbk = gidbk
        self.type = type_gist
        self.level = level
        self.check_type = ctype

    def __str__(self):
        return_str = """GIST INFO
        **************
        ID: {0}
        USER: {1}
        GID: {2}
        GID_BACKUP: {3}
        TYPE: {4}
        LEVEL: {5}
        CHECK_TYPE: {6}
        **************
        """
        return return_str.format(
            self.idJson,
            self.user,
            self.gid,
            self.gidbk,
            self.type,
            self.level,
            self.check_type
        )


class GistFile:
    def __init__(self, path):
        self.__gists = []
        with open(path) as f:
            data = json.load(f)
            for gist in data['gists']:
                self.__gists.append(
                    GistFile.GistObject(
                        gist['id'],
                        gist['user'],
                        gist['gist-id'],
                        gist['gist-bck'],
                        gist['type'],
                        gist['level'],
                        gist['check-type']
                    )
                )

    def get_all_gists(self):
        return self.__gists


def extract_function_gist(gistObject):
    logger = LogClient("")
    url_base = BASE_URL.replace("$$USER$$", gistObject.user)
    url_base = url_base.replace("$$GID$$", gistObject.gid)
    url_query = url_base + RAW.replace("$$FILE$$", QUERY_FILE)
    url_result = url_base + RAW.replace("$$FILE$$", RESULT_FILE)
    url_callback = url_base + RAW.replace("$$FILE$$", CALLBACK_FILE)
    logger.writeLog("Extracting gist object from: " + url_base)
    query_file = utils.getStrContent(url_query)
    result_file = None
    callback_file = None
    if gistObject.check_type == utils.GIST_CHECK_TYPE.JSON:
        result_file = utils.getStrContent(url_result)
    else:
        callback_file = utils.getStrContent(url_callback)
    if utils.getVerbose():
        logger.writeLog("Query: ")
        logger.writeLog(query_file)
        logger.writeLog("Expected result: ")
        result_str = result_file if result_file else "None"
        callback_str = callback_file if callback_file else "None"
        logger.writeLog(result_str)
        logger.writeLog("Callback: ")
        logger.writeLog(callback_str)
    logger.writeLog("Done.")
    return GObject(gistObject, query_file, result_file, callback_file)
