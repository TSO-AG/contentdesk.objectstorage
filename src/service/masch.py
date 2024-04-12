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
        print(checkProduct)
        print("Action:")
        for value in checkProduct:
            print(value)
        try:
            product = getObject('export/contentdesk/products/'+checkProduct+'/index.json')
            if "maschId" in product["values"]:
                maschId = product["values"]["maschId"]
                if maschId != "":
                    updateListMasch[checkProduct] = {"identifier": product["identifier"], "action": "update"}
        except:
            print("Product "+checkProduct+" --> Error")
            # print exception
            print(sys.exc_info()[0])

    putObject(updateListMasch, 'export/contentdesk/job/masch/updates/index.json')