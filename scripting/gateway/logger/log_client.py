#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

from utils import LOG_LEVEL, getVerbose
import datetime
class LogClient:
    class __LogClient:
        def __init__(self, arg):
            self.logfile = arg
        def writeLog(self, message, level="log"):
            with open(self.logfile + "." + level, "a") as log:
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = "[" + date + "] " + message
                print (message)
                log.write(message)
                log.write("\n")
    instance = None
    def __init__(self, arg):
        if not LogClient.instance:
            LogClient.instance = LogClient.__LogClient(arg)
        else:
            LogClient.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def writeLog(self, message, level="log"):
        return self.instance.writeLog(message, level)
