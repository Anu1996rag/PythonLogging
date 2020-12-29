# this file create new folder everyday in the format "FileName_dd_mm_yyyy" and returns the complete path
# of the folder 

import os,time

# folder name format
todayDate = time.strftime('%d_%m_%Y')


def createFolder():

    # if the log folder does not exists
    if not os.path.exists(os.getcwd()+'/logs'):
        os.makedirs(os.getcwd()+'/logs')

    if not os.path.exists(os.getcwd()+"/logs/" + todayDate):
        os.makedirs('logs/'+todayDate+"/")
        #current folder path
        folderPath = "/logs/"+todayDate+"/"
        return folderPath
    else:
        folderPath = "/logs/"+todayDate+"/"
        return folderPath
