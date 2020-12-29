import os,inspect,sys
import logging
from createLogFile import createLogFile



def efgh():
    path = str(inspect.stack()[1][1]).split("/")
    # methodname = sys._getframe().f_code.co_name
    # file name extracted from the path
    filename = path[len(path) - 1]
    fileLogName = filename  + ".log"
    createLogFile(fileLogName)
    print('log file created')
    logger = logging.getLogger(fileLogName)
    logger.warning('this is a test file')

efgh()