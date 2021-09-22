from flask import Flask, app, json, render_template, request, redirect, url_for, flash, jsonify
import requests

app = Flask(__name__)

url = 'https://api.covid19api.com/summary'

payload = {}

headers = {}

# GET request a covid19api

response = requests.request("GET", url, headers=headers, data = payload)
print(response.text.encode('utf8'))


#almacenamos en un json 
with open('data.json', 'w') as file:
    json.dump(response.json(), file, indent=4)

#leemos el json
covidfile = open('data.json', 'r')
jsondata = covidfile.read()
obj = json.loads(jsondata)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


    