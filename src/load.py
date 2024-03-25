import json
from os import getenv
from dotenv import find_dotenv, load_dotenv
import boto3
load_dotenv(find_dotenv())

S3_ENDPOINT = getenv('S3_ENDPOINT')
S3_BUCKET = getenv('S3_BUCKET')
S3_REGION = getenv('S3_REGION')
S3_ACCESS_KEY = getenv('S3_ACCESS_KEY')
S3_SECRET_ACCESS_KEY = getenv('S3_SECRET_ACCESS_KEY')
S3_EXPORT_PATH = getenv('S3_EXPORT_PATH')

S3_EXPORT_PATH_PRODUCTS = S3_EXPORT_PATH+"products/"

def s3client():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_ACCESS_KEY,
        endpoint_url='https://sos-'+S3_REGION+'.'+S3_ENDPOINT,
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
    puObject(product, S3_BUCKET, S3_EXPORT_PATH_PRODUCTS+product['identifier']+".json")

def putPorductIndex(products):
    puObject(products, S3_BUCKET, S3_EXPORT_PATH_PRODUCTS+"index.json")

def load(products):
    print("Loading data to target")
    print(products)
    productIndex = []
    for product in products:
        print(product)
        puObject(product, S3_BUCKET, S3_EXPORT_PATH_PRODUCTS+product['identifier']+".json")
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
