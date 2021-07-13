from flask import Flask
import requests
import os
import json

TW_KEY = os.environ.get('TW_API_KEY')
TW_URL = os.environ.get('TW_API_URL')

app = Flask(__name__)

@app.route("/starred")
def starred():
    '''
    https://developer.teamwork.com/projects/api-v3/ref/projects/get-projects-api-v3-projects-starredjson
    '''
    url = TW_URL + "/projects/api/v3/projects/starred.json"
    resp = requests.get(url, auth=(TW_KEY,"d"))
    starred = resp.content
    starred = starred.decode()
    with open('starred.json', 'w') as outfile:
        json.dump(starred, outfile)
    return('200')
    