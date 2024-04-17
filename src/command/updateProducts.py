import datetime
import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject, countFilesInFolder, folderExist
from service.akeneo import getAkeneoProduct
from service.connections import checkConnections

# Load product update list from object storage /export/contentdesk/job/products/updates/index.json
def loadProductUpdates():
    update_list = getObject('export/contentdesk/job/products/updates/index.json')
    return update_list

def testUpdateProductUpdates():
    updateList={}
    updateList["c0d07da1-7875-4053-b129-2820385dade7"] = {"identifier": "c0d07da1-7875-4053-b129-2820385dade7", "action": "update"}
    updateList["dedf67a1-2e33-49a0-ad6c-b3bb91049167"] = {"identifier": "dedf67a1-2e33-49a0-ad6c-b3bb91049167", "action": "update"}
    updateList["dbb48efd-6e22-4665-9987-d1744d028ea7"] = {"identifier": "dbb48efd-6e22-4665-9987-d1744d028ea7", "action": "update"}
    updateList["f0855124-b995-4516-ba61-40b932c31fdf"] = {"identifier": "f0855124-b995-4516-ba61-40b932c31fdf", "action": "update"}
    updateList["ea6fa9b4-4c9a-4335-bc6c-2979ce8d5ece"] = {"identifier": "ea6fa9b4-4c9a-4335-bc6c-2979ce8d5ece", "action": "update"}
    updateList["c43836d5-1033-4955-afa6-84707ef819f4"] = {"identifier": "c43836d5-1033-4955-afa6-84707ef819f4", "action": "create"}
    updateList["31acbe46-aeb5-4f06-a7c5-a6917f2326e0"] = {"identifier": "31acbe46-aeb5-4f06-a7c5-a6917f2326e0", "action": "delete"}

    # 31acbe46-aeb5-4f06-a7c5-a6917f2326e0
    updateProductUpdates(updateList)

def updateProductUpdates(updateList):
    # Add to product updates
    putObject(updateList, 'export/contentdesk/job/products/updates/index.json')
    # Add to index updates
    putObject(updateList, 'export/contentdesk/job/index/updates/index.json')

def getProductUpdateHistory():
    dateToday = datetime.datetime.now().strftime('%Y-%m-%d')
    # check if file exists
    try:
        productHistory = getObject('export/contentdesk/job/index/updates/history/'+dateToday+'/index.json')
    except:
        productHistory = {}
    return productHistory

def updateProductHistory(updateList):
    print("Updating product day history")
    print(updateList)
    dateToday = datetime.datetime.now().strftime('%Y-%m-%d')
    todayHistory = getProductUpdateHistory()
    # dict for each with identifier and action
    for identifier, update in updateList.items():
        print("Updating product " + identifier)
        print(update)
        todayHistory[identifier] = {"identifier": identifier, "action": update['action']}
        putObject(todayHistory, 'export/contentdesk/job/index/updates/history/' + dateToday + '/index.json')
    
def updateProducts(updateList):
    for identifier in updateList:
        if updateList[identifier]["action"] == "product.update" or updateList[identifier]["action"] == "product.create":
            print("Updating product "+identifier)
            try:
                #product = getAkeneoProduct(identifier)
                product = getObject('/api/rest/v1/products/'+identifier+'.json')
                # Check if Folder exist
                if not folderExist('export/contentdesk/products/'+identifier):
                    print("Creating folder export/contentdesk/products/"+identifier)
                    putObject({}, 'export/contentdesk/products/'+identifier+'/index.json')
                    putObject({}, 'export/contentdesk/products/'+identifier+'/history/')
                # make Version
                productHistory = getObject('export/contentdesk/products/'+identifier+'/index.json')
                # how many files in history folder in Object Storage
                # count files in export/contentdesk/products/identifier/history
                i = countFilesInFolder('export/contentdesk/products/'+identifier+'/history')
                # Add/Update Files in Object Storage
                putObject(product, 'export/contentdesk/products/'+identifier+'/index.json')
                putObject(productHistory, 'export/contentdesk/products/'+identifier+'/history/'+str(i)+'.json')
            except:
                print("Product "+identifier+" --> Error")
                # print exception
                print(sys.exc_info()[0])
        elif updateList[identifier]["action"] == "product.removed":
            print("Removing product "+identifier)
            print("Noting to do")
    # Add to Day History
    print("Updating product day history")
    updateProductHistory(updateList)

def __main__():
   # Test
   #print("TEST - ADD PRODUCT UPDATES TO OBJECT STORAGE")
   #testUpdateProductUpdates()
   print("LOADING PRODUCT UPDATES")
   updateList = loadProductUpdates()   
   print("UPDATE PRODUCT")
   updateProducts(updateList)
   print("CHECK CONNECTIONS")
   checkConnections(updateList)
   print("REMOVING PRODUCT UPDATES")
   updateProductUpdates({})
   print("DONE")

if __name__== "__main__":
    __main__()