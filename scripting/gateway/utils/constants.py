#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

VERBOSE = False

# Environment DEV:
GRAPH_URL = "https://dev-api-iam.travelgatex.com/controller/xquery"
GRAPH_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5EQTFOa00zUVVSRk1EQXdOekF4TVRKRk5UQkdSRGMwUWpreVEwVTJOVVV6UkRrNU5rUkNSZyJ9.eyJodHRwczovL3RyYXZlbGdhdGV4LmNvbS9pYW0iOlt7ImEiOm51bGwsImMiOiJ4dGciLCJnIjpbeyJhIjp7ImFsbCI6eyJlbnRpdHkiOnsiYWNjIjpbImNydWQxYWYiXSwiY2xpIjpbImNydWQxYWYiXSwic3VwIjpbImNydWQxYWYiXX0sImhvdGxzdCI6eyJob3QiOlsiMXgiXX0sImh1YmdyYSI6eyJib2siOlsiMXhmIl0sImJvbyI6WyIxeGYiXSwiYnJkIjpbIjF4ZiJdLCJjYXQiOlsiMXhmIl0sImNmZyI6WyIxeGYiXSwiY25sIjpbIjF4ZiJdLCJxdGUiOlsiMXhmIl0sInJvbSI6WyIxeGYiXSwic3JjIjpbIjF4ZiJdfSwiaWFtIjp7ImFwaSI6WyJjcnVkMWFmIl0sImdycCI6WyJjcnVkMWFmIl0sIm1iciI6WyJjcnVkMWFmIl0sInByZCI6WyJjcnVkMWFmIl0sInJvbCI6WyJjcnVkMWFmIl0sInJzYyI6WyJjcnVkMWFmIl0sIm9wdCI6WyJjcnVkMWFmIl19fX0sImMiOiJkZXZvcHMiLCJnIjpudWxsLCJwIjp7ImlhbSI6eyJncnAiOlsiY3J1ZDEiXX19LCJ0IjoidGVhbSJ9XSwicCI6eyJpYW0iOnsiZ3JwIjpbImNydWQxIl19fSwidCI6InJvb3QifV0sImh0dHBzOi8vdHJhdmVsZ2F0ZXguY29tL21lbWJlcl9pZCI6InNsdWNlYUB4bWx0cmF2ZWxnYXRlLmNvbSIsImlzcyI6Imh0dHBzOi8veHRnLWRldi5ldS5hdXRoMC5jb20vIiwic3ViIjoiQ3MzWmtOanBNQ3cyZlZUOWc2cG4wbHNTSndkNjFQOVhAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vYXBpLnRyYXZlbGdhdGV4LmNvbSIsImlhdCI6MTUzODA2MDYxOCwiZXhwIjoxNTQ1ODM2NjE4LCJhenAiOiJDczNaa05qcE1DdzJmVlQ5ZzZwbjBsc1NKd2Q2MVA5WCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.lX5o49AFB9v2pqHVcMevj73smFF4GIkj-czFw1yDr_PZFbi7e-1ew7HHVmm6SueD-dQVu0HTPh-WELI1hvpx3ZoLxHU5s760gfR6cjZ37zDf3RXhdpJrqRHvyFxVvlZERP0LFYHFYM6-9xK2Crw-hhxXE2yzKQErykWDlBBBsyVsjw_ZvWV964G9tSSneTW4Jgnwg4zaMSt97scZmF8UJ9h5-49idKLLBRNlGBzfJi5W0i0pFlQ4cjYmqLpvv3zyu5MOYTbmC3e2KSB_En6al04AJkdpSpLhOorv-W76l1oOBx2yEG0EMSQFZNz6H5sxxLlfZIYybKSwloOcQ3mAVw"

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
