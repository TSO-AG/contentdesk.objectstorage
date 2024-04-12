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
        print(updateList[checkProduct]["action"])
        
        product = getObject('export/contentdesk/products/'+checkProduct+'/index.json')
        print(product)
        if "maschId" in product["values"]:
            print("Product "+checkProduct+" --> MaschId: "+product["values"]["maschId"])
            maschId = product["values"]["maschId"]
            if maschId != "":
                try:
                     updateListMasch[product["identifier"]] = {"identifier": product["identifier"], "action": updateList[checkProduct]["action"]}
                except:
                    print("Product "+checkProduct+" --> Error")
                    # print exception
                    print(sys.exc_info()[0])

    print ("UpdateListMasch")
    print(updateListMasch)
    putObject(updateListMasch, 'export/contentdesk/job/masch/updates/index.json')