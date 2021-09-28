import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


url = "https://corona.lmao.ninja/v2/all?yesterday"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data_dict = response.json()




@app.route('/')
def index():
    return render_template('main.html', data=data_dict)


@app.route('/about')
def about():
    return render_template('about.html')