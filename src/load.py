import json
from os import getenv
from dotenv import find_dotenv, load_dotenv
import boto3
load_dotenv(find_dotenv())

OBJECTSTORAGE_ENDPOINT = getenv('OBJECTSTORAGE_ENDPOINT')
OBJECTSTORAGE_BUCKET = getenv('OBJECTSTORAGE_BUCKET')
OBJECTSTORAGE_REGION = getenv('OBJECTSTORAGE_REGION')
OBJECTSTORAGE_ACCESS_KEY = getenv('OBJECTSTORAGE_ACCESS_KEY')
OBJECTSTORAGE_SECRET_ACCESS_KEY = getenv('OBJECTSTORAGE_SECRET_ACCESS_KEY')
OBJECTSTORAGE_EXPORT_PATH = getenv('OBJECTSTORAGE_EXPORT_PATH')

OBJECTSTORAGE_EXPORT_PATH_PRODUCTS = OBJECTSTORAGE_EXPORT_PATH+"products/"

def s3client():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=OBJECTSTORAGE_ACCESS_KEY,
        aws_secret_access_key=OBJECTSTORAGE_SECRET_ACCESS_KEY,
        endpoint_url='https://sos-'+OBJECTSTORAGE_REGION+'.'+OBJECTSTORAGE_ENDPOINT,
    )
    return s3_client

def puObject(data, bucket, filename):
    s3 = s3client()
    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=json.dumps(data),
        ACL='public-read',
        ContentType='application/json')
    
def loadProduct(product):
    puObject(product, OBJECTSTORAGE_BUCKET, OBJECTSTORAGE_EXPORT_PATH_PRODUCTS+product['identifier']+".json")

def putPorductIndex(products):
    puObject(products, OBJECTSTORAGE_BUCKET, OBJECTSTORAGE_EXPORT_PATH_PRODUCTS+"index.json")

def load(products):
    print("Loading data to target")
    print(products)
    productIndex = []
    for product in products:
        print(product)
        puObject(product, OBJECTSTORAGE_BUCKET, OBJECTSTORAGE_EXPORT_PATH_PRODUCTS+product['identifier']+".json")
        # Add to Product Index
        sku = product['identifier']
        productRow = {}
        if 'name' in product['values']:
            name = product['values']['name'][0]['data']
        else :
            name = ""
        if 'family' in product['values']:
            family = product['values']['family'][0]['data']
        else :
            family = ""
        productRow[sku] = {
            "identifier": product['identifier'],
            "name": name,
            "family": family,
            "created": product['created'],
            "updated": product['updated'],
        }
        productIndex.append(productRow)

    putPorductIndex(productIndex)
