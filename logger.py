import os,inspect
import logging,logging.config
from createFolder import createFolder

# logging levels

loglevel = "debug"
if loglevel.upper() == "DEBUG":
    loglevels = logging.DEBUG
elif loglevel.upper() == "INFO":
    loglevels = logging.DEBUG
elif loglevel.upper() == "WARNING":
    loglevels = logging.WARNING
elif loglevel.upper() == "ERROR":
    loglevels = logging.ERROR
elif loglevel.upper() == "CRITICAL":
    loglevels = logging.CRITICAL
else:
    loglevels = logging.DEBUG


def createLogFile(logfilename):
    return logging.config.fileConfig(fname='loggingConfiguration.conf', defaults={'logfilename': logfilename})

def loggingInfo(loglevel=logging.DEBUG):
    #creting new folder
    folderPath = createFolder()

    #path of the micro services file to be called
    path = str(inspect.stack()[1][1]).split("/")

    # file name extracted from the path
    filename = path[len(path) - 1]
    fileLogName = os.getcwd() + folderPath + filename + ".log"

    #creating new log file
    createLogFile(fileLogName)
    print('log file created')

    logger = logging.getLogger(fileLogName)
    logger.setLevel(loglevels)




