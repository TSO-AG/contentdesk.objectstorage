import datetime
import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject, countFilesInFolder, folderExist

def updateProductUpdates(updateList):
    # Add to product updates
    putObject(updateList, 'export/contentdesk/job/products/updates/index.json')

def checkProductsMasch(updateList):
    print("Checking Masch UpdateList")
    updateListMasch = {}
    for checkProduct in updateList:
        print("Check product:")
        print(checkProduct["identifier"])
        try:
            product = getObject('export/contentdesk/products/'+checkProduct["identifier"]+'/index.json')
            if "maschId" in product["values"]:
                maschId = product["values"]["maschId"]
                if maschId != "":
                    updateListMasch[maschId] = {"identifier": product["identifier"], "action": checkProduct["action"]}
        except:
            print("Product "+checkProduct["identifier"]+" --> Error")
            # print exception
            print(sys.exc_info()[0])

    putObject(updateListMasch, 'export/contentdesk/job/masch/updates/index.json')