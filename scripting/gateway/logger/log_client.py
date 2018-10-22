#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

from utils import LOG_LEVEL, getVerbose
import datetime
import os

MAX_LOGS = 10

class LogClient:
    class __LogClient:
        def __init__(self, arg):
            self.logfile = arg
        def writeResult(self, gid, result, level):
            with open(self.logfile + "-result.csv", "a") as result_file:
                result_str = '1' if result else '0'
                result_file.write(gid + ", " + result_str + ", " + str(level))
                result_file.write("\n")
        def writeLog(self, message, level="log"):
            with open(self.logfile + "." + level, "a") as log:
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = "[" + date + "] " + message
                print (message)
                log.write(message)
                log.write("\n")
        def rotateLogs(self):
            for ext_file in [".err", ".warn", ".log", "-result.csv"]:
                max_filename = self.logfile + ext_file + '.' + str(MAX_LOGS)
                if os.path.exists(max_filename):
                    os.remove(max_filename)
                for x in range(MAX_LOGS-1):
                    filename = self.logfile + ext_file + '.' + str(MAX_LOGS-1-x)
                    destfile = self.logfile + ext_file + '.' + str(MAX_LOGS-x)
                    if os.path.exists(filename):
                        if os.path.exists(destfile):
                            os.remove(destfile)
                        os.rename(filename, destfile)
                if os.path.exists(self.logfile + ext_file):
                    os.rename(self.logfile + ext_file, self.logfile + ext_file + '.1')

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
    def writeResult(self, gid, result, level):
        return self.instance.writeResult(gid, result, level)
    def rotateLogs(self):
        return self.instance.rotateLogs()