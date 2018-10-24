#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

VERBOSE = False

# Environment DEV:
GRAPH_URL = "https://dev-api.travelgatex.com/"
GRAPH_TOKEN = "PUT YOUR BEARER/APIKEY HERE"

# Environment Pro
#GRAPH_URL_ENTITY = "https://api-core.travelgatex.com/entities/xquery"
#GRAPH_URL_IAM = "https://api-iam.travelgatex.com/controller/xquery"


class GIST_TYPE:
    QA = 0
    DOC = 1
    BOTH = 2


class GIST_CHECK_TYPE:
    JSON = 0
    CALLBACK = 1


class GIST_LEVEL:
    CRITICAL = 2
    MEDIUM = 1
    LOW = 0


class LOG_LEVEL:
    ERROR = "err"
    LOG = "log"
    WARN = "warn"


def getVerbose():
    return VERBOSE


def setVerbose(verbose_value):
    global VERBOSE
    VERBOSE = verbose_value


def getStrContent(url):
    ret_value = None
    with requests.get(
        url,
        headers={'Cache-Control': 'no-cache'}
    ) as resp:
        ret_value = resp.text
    return ret_value
