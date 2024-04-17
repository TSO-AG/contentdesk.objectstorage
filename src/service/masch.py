import datetime
import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject, countFilesInFolder, folderExist

def getMaschUpdateJobs():
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
            product = getObject('/api/rest/v1/products/'+checkProduct+'.json')
            print(product)
        except:
            # print exception
            print(sys.exc_info()[0])

        print(product)
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
        else:
            print("Product "+checkProduct+" has no values")
    
    # Check updateListMasch is not empty
    if updateListMasch:
        print("UpdateListMasch")
        print(updateListMasch)
        putObject(updateListMasch, 'export/contentdesk/job/masch/updates/index.json')
    else:
        print("UpdateListMasch is empty - No Updates")