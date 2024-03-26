import sys
sys.path.append("..")

from load import clearObjectStorage

def __main__():

   print("LOADING")
   loadData = clearObjectStorage()
   print("DONE")

if __name__== "__main__":
    __main__()