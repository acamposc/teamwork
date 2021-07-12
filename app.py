from flask import Flask
import requests
import os
import json

TW_KEY = os.environ.get('TW_API_KEY')
TW_URL = os.environ.get('TW_API_URL')

app = Flask(__name__)

@app.route("/projects")
def projects():
    url = TW_URL + "/projects.json"
    resp = requests.get(url, auth=(TW_KEY,"d"))
    projects = resp.content
    with open('projects.txt', 'w') as outfile:
        json.dump(projects, outfile)
    return("dumped")

@app.route("/tasks")
def tasks():
    url = TW_URL + "/tasks.json"
    resp = requests.get(url, auth=(TW_KEY,"d"))
    return(resp.content)

