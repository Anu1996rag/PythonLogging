import os,sys,inspect
from createLogFile import createLogFile
import logging




def createFile():
    path = str(inspect.stack()[1][1]).split("/")
    # methodname = sys._getframe().f_code.co_name
    # file name extracted from the path
    filename = path[len(path) - 1]
    fileLogName = filename + ".log"
    createLogFile(fileLogName)
    print('log file created')




