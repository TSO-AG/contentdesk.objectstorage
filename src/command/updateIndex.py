import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject, removeObject
from service.akeneo import getAkeneoProduct

def loadIndexUpdates():
    update_list = getObject('export/contentdesk/job/index/updates/index.json')
    return update_list

def setProductIndexSchema(product):
    index = {}
    index["identifier"] = product["identifier"]
    index["family"] = product["family"]
    index["categories"] = product["categories"]
    index["groups"] = product["groups"]
    index["enabled"] = product["enabled"]
    index["created"] = product["created"]
    index["updated"] = product["updated"]
    #index["values"] = {}
    #for attribute in product["values"]:
    #    index["values"][attribute] = product["values"][attribute]
    return index

def testIndexUpdates():
    updateList={}
    updateList["c0d07da1-7875-4053-b129-2820385dade7"] = "c0d07da1-7875-4053-b129-2820385dade7"
    updateList["dedf67a1-2e33-49a0-ad6c-b3bb91049167"] = "dedf67a1-2e33-49a0-ad6c-b3bb91049167"
    updateList["dbb48efd-6e22-4665-9987-d1744d028ea7"] = "dbb48efd-6e22-4665-9987-d1744d028ea7"
    updateList["f0855124-b995-4516-ba61-40b932c31fdf"] = "f0855124-b995-4516-ba61-40b932c31fdf"
    updateIndexUpdate(updateList)

def updateIndexUpdate(updateList):
    # Add to index updates
    putObject(updateList, 'export/contentdesk/job/index/updates/index.json')

def updateIndex(updateList):
    index = {}
    for identifier in updateList:
        print("Updating product "+identifier)
        #product = getAkeneoProduct(update)
        # get Product from Object Storage
        product = getObject('export/contentdesk/products/'+identifier+'/index.json')
        # get Index from Object Storage
        productIndex = getObject('export/contentdesk/products/index/index.json')
        #productIndex = {}
        index = productIndex
        # Set Index Schema
        index[identifier] = setProductIndexSchema(product)
        # Add Product to Index
        putObject(index, 'export/contentdesk/products/index/index.json')

def setIndexEmpty():
    index = {}
    putObject(index, 'export/contentdesk/products/index/index.json')

def deleteIndex():
    removeObject('export/contentdesk/products/index.json')

def __main__():
   # Test
   #print("TEST - ADD PRODUCT TO INDEX UPDATES")
   #testIndexUpdates()
   print("LOADING INDEX UPDATES")
   updateList = loadIndexUpdates()
   print("UPDATE INDEX")
   updateIndex(updateList)
   print("REMOVING INDEX UPDATES")
   updateIndexUpdate({})
   print("DONE")

if __name__== "__main__":
    __main__()