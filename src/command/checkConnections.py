import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject, countFilesInFolder, folderExist

def getConnectionsUpdate():
    update_list = getObject('export/contentdesk/job/connections/updates/index.json')
    return update_list

def __main__():
    print("START - Check Connections")
    print("Loading Connections Update List")
    updateList = getConnectionsUpdate()
    
    print("DONE")

if __name__== "__main__":
    __main__()