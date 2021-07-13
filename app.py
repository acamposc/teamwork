from flask import Flask
import requests
import os
import json
from google.cloud import storage


TW_KEY = os.environ.get('TW_API_KEY')
TW_URL = os.environ.get('TW_API_URL')

'''
Cloud Storage Env vars.
'''
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
STORAGE_BUCKET_NAME = os.environ.get('STORAGE_BUCKET_NAME')
bucket_name = STORAGE_BUCKET_NAME

app = Flask(__name__)

@app.route("/starred")
def starred():
    '''
    https://developer.teamwork.com/projects/api-v3/ref/projects/get-projects-api-v3-projects-starredjson
    starred() gets starred projects for a single user.
    response from TW request is decoded from bytes and written as a json file at root.
    '''
    url = TW_URL + "/projects/api/v3/projects/starred.json"
    resp = requests.get(url, auth=(TW_KEY,"d"))
    starred = resp.content
    starred = starred.decode()
    with open('starred.json', 'w') as outfile:
        json.dump(starred, outfile)
    

    '''
    initiallize cloud storage
    '''
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    '''
    Upload files to bucket in Storage.
    '''
    def upload(blob_name,file_path,bucket_name):
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(file_path)
            return True
        
        except Exception as e:
            print(e)
            return False

    file_path = 'starred.json'
    upload(
        blob_name = 'test',
        file_path = file_path,
        bucket_name = bucket

    )




    return('200')
    
