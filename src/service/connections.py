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
CONNECTION_DEMO = getenv('CONNECTION_DEMO')
# MASCH
CONNECTION_MASCH = getenv('CONNECTION_MASCH')
# Text Blaze
CONNECTION_TEXTBLAZE = getenv('CONNECTION_TEXTBLAZE')

def checkConnections(updateList):
    print("Checking Connections")
    # Check Outdooractive
    print("Checking Outdooractive")
    if CONNECTION_OUTDOORACTIVE == True:
        print("Checking Outdooractive = TRUE")
        # checkProductConnections(identifier)
    # Check OpenData
    print("Checking OpenData")
    if CONNECTION_OPENDATA == True:
        print("Checking OpenData = TRUE")
        # checkProductConnections(identifier)
    # Check Akeneo OST
    print("Checking Akeneo OST")
    if CONNECTION_OST == True:
        print("Checking Akeneo OST = TRUE")
        # checkProductConnections(identifier)
    # Check Masch
    print("Checking Masch")
    if CONNECTION_MASCH == True:
        print("Checking Masch = TRUE")
        checkProductsMasch(updateList)
    # Check Text Blaze
    print("Checking Text Blaze")
    if CONNECTION_TEXTBLAZE == True:
        print("Checking Text Blaze = TRUE")
        # checkProductConnections(identifier)
    print("DONE - Checking Connections")
    return "Done"