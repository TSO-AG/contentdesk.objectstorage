import sys
sys.path.append("..")

from service.objectStorage import getObject, putObject

# Load product update list from object storage /export/contentdesk/job/products/updates/index.json
def loadProductUpdates():
    update_list = getObject('export/contentdesk/job/products/updates/index.json')
    return update_list

def updateProductUpdates(updateList):
    putObject(updateList, 'export/contentdesk/job/products/updates/index.json')

def __main__():
   # Test
   print("ADD PRODUCT UPDATES TO OBJECT STORAGE")
   updateList = [
       "c0d07da1-7875-4053-b129-2820385dade7",
       "dedf67a1-2e33-49a0-ad6c-b3bb91049167",
       "dbb48efd-6e22-4665-9987-d1744d028ea7"
   ]
   updateProductUpdates(updateList)

   print("LOADING PRODUCT UPDATES")
   
   print("LOADING")

   print("DONE")

if __name__== "__main__":
    __main__()