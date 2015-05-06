from flask import Flask
from threading import Thread
from io import StringIO
import requests
import csv

app = Flask(__name__)

chalice_list = 0

def fetch_chalice_list():
    global chalice_list
    response  = requests.get('https://docs.google.com/spreadsheets/d/18TVy5cDk6sNX0lc2dNQM2Q-SLv0_9QecQrtKR0sRb6Q/export?format=tsv&id=18TVy5cDk6sNX0lc2dNQM2Q-SLv0_9QecQrtKR0sRb6Q&gid=1095946635') 
    #http://stackoverflow.com/questions/3305926/python-csv-string-to-array
    chalice_list = csv.reader(StringIO(response.text),delimiter='\t')


@app.route("/")
def index():
    return "Hello World!"

@app.route("/query")
def query():
    return "JSON query"

if __name__ == "__main__":
    fetch_chalice_list()
    for row in chalice_list:
        print(row)
    app.run(debug=True)