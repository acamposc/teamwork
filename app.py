from flask import Flask
import requests
import os
import json
from fn import fn


TW_KEY = os.environ.get('TW_API_KEY')
TW_URL = os.environ.get('TW_API_URL')

'''
- STORAGE_BUCKET_NAME abstracted for protection.
'''
STORAGE_BUCKET_NAME = os.environ.get('STORAGE_BUCKET_NAME')

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
    
    
    '''
    creates json file at root directory.
    '''
    file_path = 'starred.json'
    with open(file_path, 'w') as outfile:
        json.dump(starred, outfile)
    

    '''
    calls function from directory fn
    '''
    fn.upload(
        blob_name = file_path,
        file_path = file_path,
        bucket_name = STORAGE_BUCKET_NAME
    )



    '''
    confirmation screen could improve.
    '''
    return('200')
    
