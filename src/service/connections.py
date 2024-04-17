from os import getenv
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

import sys
sys.path.append("..")
from service.masch import checkProductsMasch

# OUTDOORACTIVE
CONNECTION_OUTDOORACTIVE = getenv('CONNECTION_OUTDOORACTIVE')
# OPENDATA
CONNECTION_OPENDATA = getenv('CONNECTION_OPENDATA')
# AKENEOs
CONNECTION_OST = getenv('CONNECTION_OST')
# MASCH
CONNECTION_MASCH = getenv('CONNECTION_MASCH')
# Text Blaze
CONNECTION_TEXTBLAZE = getenv('CONNECTION_TEXTBLAZE')

def checkConnections(updateList):
    print("Checking Connections")
    print(updateList)
    # Check Outdooractive
    print("Checking Outdooractive")
    if CONNECTION_OUTDOORACTIVE:
        print("Checking Outdooractive = TRUE")
        # checkProductConnections(identifier)
    else:
        print("Checking Outdooractive = FALSE")
    # Check OpenData
    print("Checking OpenData")
    if CONNECTION_OPENDATA:
        print("Checking OpenData = TRUE")
        # checkProductConnections(identifier)
    else:
        print("Checking OpenData = FALSE")
    # Check Akeneo OST
    print("Checking Akeneo OST")
    if CONNECTION_OST:
        print("Checking Akeneo OST = TRUE")
        # checkProductConnections(identifier)
    else:
        print("Checking Akeneo OST = FALSE")
    # Check Masch
    print("Checking Masch")
    if CONNECTION_MASCH:
        print("Checking Masch = TRUE")
        checkProductsMasch(updateList)
    else:
        print("Checking Masch = FALSE")
    # Check Text Blaze
    print("Checking Text Blaze")
    if CONNECTION_TEXTBLAZE:
        print("Checking Text Blaze = TRUE")
        # checkProductConnections(identifier)
    else:
        print("Checking Text Blaze = FALSE")
    print("DONE - Checking Connections")
    return "Done"