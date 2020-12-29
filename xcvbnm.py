import logging.config,os

def createLogFile(name):
    #name = '/logs/' + name
    print(name)
    return logging.config.fileConfig(fname='loggingConfig.conf',defaults={ 'logfilename' : name })

createLogFile('abcd')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.warning('fgh')