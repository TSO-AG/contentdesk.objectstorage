from os import getenv
from dotenv import find_dotenv, load_dotenv
from akeneo.akeneo import Akeneo
from service.masch import checkProductsMasch
load_dotenv(find_dotenv())

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
    if CONNECTION_OUTDOORACTIVE == True:
        print("Checking Outdooractive")
        # checkProductConnections(identifier)
    # Check OpenData
    if CONNECTION_OPENDATA == True:
        print("Checking OpenData")
        # checkProductConnections(identifier)
    # Check Akeneo OST
    if CONNECTION_OST == True:
        print("Checking Akeneo OST")
        # checkProductConnections(identifier)
    # Check Akeneo DEMO
    if CONNECTION_DEMO == True:
        print("Checking Akeneo DEMO")
        # checkProductConnections(identifier)
    # Check Masch
    if CONNECTION_MASCH == True:
        print("Checking Masch")
        checkProductsMasch(updateList)
    # Check Text Blaze
    if CONNECTION_TEXTBLAZE == True:
        print("Checking Text Blaze")
        # checkProductConnections(identifier)
    print("DONE")
    return "Done"