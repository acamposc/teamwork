from flask import Flask
import requests
import os

TW_KEY = os.environ.get('TW_API_KEY')
TW_URL = os.environ.get('TW_API_URL')

app = Flask(__name__)

@app.route("/projects")
def projects():
    url = TW_URL + "/projects.json"
    resp = requests.get(url, auth=(TW_KEY,"d"))
    return(resp.content)

@app.route("/tasks")
def tasks():
    url = TW_URL + "/tasks.json"
    resp = requests.get(url, auth=(TW_KEY,"d"))
    return(resp.content)

