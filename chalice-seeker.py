from flask import Flask, jsonify, render_template, request
from flask.ext.assets import Environment, Bundle
from threading import Thread
from io import StringIO
import requests
import csv

app = Flask(__name__)
assets=Environment(app)


css = Bundle(
    Bundle('assets/surface_styles.scss',
        filters='scss'),
    Bundle('custom.css'),
    filters='cssmin',
    output='all.css')

assets.register('css_all',css)


chalice_list = []

def fetch_chalice_list():
    global chalice_list
    chalice_list = []
    #response  = requests.get('https://docs.google.com/spreadsheets/d/18TVy5cDk6sNX0lc2dNQM2Q-SLv0_9QecQrtKR0sRb6Q/export?format=tsv&id=18TVy5cDk6sNX0lc2dNQM2Q-SLv0_9QecQrtKR0sRb6Q&gid=1095946635') 
    #http://stackoverflow.com/questions/3305926/python-csv-string-to-array
    #reader = csv.reader(StringIO(response.text),delimiter='\t')
    tsv_file = open('Chalice Dungeon Submission Form (Responses) - Form Responses 1.tsv','r')
    reader = csv.reader(tsv_file,delimiter='\t')
    next(reader)
    for row in reader:
        if row[0] != '':
            for i in range(4,12):
                if row[i]=='':
                    row[i]="None / Unsure"
            chalice_list.append(row)

@app.route("/")
def index():
    return render_template('index.html',data=chalice_list)

@app.route("/query")
def query():
    return "JSON query"

if __name__ == "__main__":
    fetch_chalice_list()
    app.run(debug=True,host='0.0.0.0')