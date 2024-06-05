import datetime
import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject, countFilesInFolder, folderExist


def getMaschUpdateJobs():
    # Check if folder exist
    if folderExist('export/contentdesk/job/masch/updates'):
        print("Folder exist")
    else:
        print("Folder does not exist")
        # create folder
        print("Create Folder")
        putObject({}, 'export/contentdesk/job/masch/updates/index.json')
    updateList = getObject('export/contentdesk/job/masch/updates/index.json')
    return updateList

def checkProductsMasch(updateList):
    print("Checking Masch UpdateList")
    updateListMasch = getMaschUpdateJobs()
    for checkProduct in updateList:
        print("Check product:")
        print(checkProduct)
        print("Action:")
        print(updateList[checkProduct]["action"])
        # Get Product from Object Storage
        #product = getObject('export/contentdesk/products/'+checkProduct+'/index.json')
        # check if file exists
        try:
            print("Product "+checkProduct+" File exists")
            product = getObject('api/rest/v1/products/'+checkProduct+'.json')
        except:
            # print exception
            print(sys.exc_info()[0])

        if updateList[checkProduct]["action"] == "product.updated" or updateList[checkProduct]["action"] == "product.created":
            # check if product has values
            if "values" in product:
                print("Product "+checkProduct+" has values")

                # Check if MaschId exists
                if "maschId" in product["values"]:
                    print("Product "+product["identifier"])
                    print("MaschId: ")
                    print(product["values"]["maschId"][0]["data"])
                    maschId = product["values"]["maschId"][0]["data"]
                    if maschId != "":
                        try:
                            updateListMasch[product["identifier"]] = {"identifier": product["identifier"], "action": updateList[checkProduct]["action"]}
                        except:
                            print("Product "+checkProduct+" --> Error")
                            # print exception
                            print(sys.exc_info()[0])
                
                # OR Check if Object new in Category masch
                if "masch_accommodation" in product["categories"]:
                    print("Product "+product["identifier"])
                    print("Category: masch_accommodation")
                    try:
                        updateListMasch[product["identifier"]] = {"identifier": product["identifier"], "action": updateList[checkProduct]["action"]}
                    except:
                        print("Product "+checkProduct+" --> Error")
                        # print exception
                        print(sys.exc_info()[0])
            else:
                print("Product "+checkProduct+" has no values")
        else:
            print("Product "+checkProduct+" removed")
    
    # Check updateListMasch is not empty
    if updateListMasch:
        print("UpdateListMasch")
        print(updateListMasch)
        # check if folder exist
        if folderExist('export/contentdesk/job/masch/updates'):
            print("Folder exist")
        else:
            print("Folder does not exist")
            # create folder
            print("Create Folder")
            putObject({}, 'export/contentdesk/job/masch/updates/index.json')
        putObject(updateListMasch, 'export/contentdesk/job/masch/updates/index.json')
    else:
        print("UpdateListMasch is empty - No Updates")