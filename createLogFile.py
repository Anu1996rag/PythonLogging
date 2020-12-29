import logging.config, os


def createLogFile(logfilename):
    return logging.config.fileConfig(fname='loggingConfiguration.conf', defaults={'logfilename': logfilename})

# createLogFile('abc')
