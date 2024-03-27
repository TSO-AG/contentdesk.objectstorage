import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject
from service.akeneo import getAkeneoProduct

# Load product update list from object storage /export/contentdesk/job/products/updates/index.json
def loadProductUpdates():
    update_list = getObject('export/contentdesk/job/products/updates/index.json')
    return update_list

def testUpdateProductUpdates():
    updateList={}
    updateList["c0d07da1-7875-4053-b129-2820385dade7"] = "c0d07da1-7875-4053-b129-2820385dade7"
    updateList["dedf67a1-2e33-49a0-ad6c-b3bb91049167"] = "dedf67a1-2e33-49a0-ad6c-b3bb91049167"
    updateList["dbb48efd-6e22-4665-9987-d1744d028ea7"] = "dbb48efd-6e22-4665-9987-d1744d028ea7"
    updateProductUpdates(updateList)

def updateProductUpdates(updateList):
    # Add to product updates
    putObject(updateList, 'export/contentdesk/job/products/updates/index.json')
    # Add to index updates
    putObject(updateList, 'export/contentdesk/job/index/updates/index.json')

def updateProducts(updateList):
    for update in updateList:
        print("Updating product "+update)
        product = getAkeneoProduct(update)
        putObject(product, 'export/contentdesk/products/'+update+'.json')

def __main__():
   # Test
   #print("TEST - ADD PRODUCT UPDATES TO OBJECT STORAGE")
   #testUpdateProductUpdates()
   print("LOADING PRODUCT UPDATES")
   updateList = loadProductUpdates()   
   print("UPDATE PRODUCT")
   updateProducts(updateList)
   print("REMOVING PRODUCT UPDATES")
   updateProductUpdates({})
   print("DONE")

if __name__== "__main__":
    __main__()