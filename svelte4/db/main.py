import requests
import xmltodict
import json
from datetime import date
from flask_cors import CORS
from flask import Flask, make_response, request
from config import API_KEY

app = Flask(__name__)
CORS(app)

api_key_headers = {
    'x-api-key': API_KEY
}

@app.route("/testi")
def makeRequest():
    PARAMS = {
    'securityToken': '0c79fd8c-40c4-49fe-916d-7d420abf45ad',
    'documentType': 'A44', # This is the document for the electricity prices
    'In_Domain': '10YFI-1--------U', # prices in Finland
    'Out_Domain': '10YFI-1--------U',
    'periodStart': '202404130100',
    'periodEnd': '202404130100'
    }
    current_date = date.today()
    args = request.args
    start_date = args.get("startDate", default=current_date, type=str)
    end_date = args.get("endDate", default=current_date, type=str)
    if start_date:
        start_date = start_date.replace("-","") + "0100"
        PARAMS['periodStart'] = start_date
    if end_date:
        end_date = end_date.replace("-","") + "0100"
        PARAMS['periodEnd'] = end_date
    r = requests.get(url="https://web-api.tp.entsoe.eu/api", params=PARAMS)
    content = r.content.replace(b"price.amount", b"price")
    json_obj = json.dumps(xmltodict.parse(content))
    print(json_obj)
    return make_response(json_obj, 200)

@app.route("/<path:data_type>")
def doRequest(data_type):
    if data_type == "production":
        URL = "https://data.fingrid.fi/api/datasets/74/data?format=json"
    elif data_type == "windgeneration":
        URL = "https://data.fingrid.fi/api/datasets/75/data?format=json"
    elif data_type == "consumption":
        URL = "https://data.fingrid.fi/api/datasets/124/data?format=json"
    elif data_type == "temperature" or data_type == "temperature2":
        URL = "https://data.fingrid.fi/api/datasets/196/data?format=json"
    else:
        return "Invalid data type", 400

    current_date = date.today()
    args = request.args
    if data_type == "temperature2":
        start_date = args.get("startTime", default=f"{current_date}T12:00:00Z",
        type=str)
    else:
        start_date = args.get("startTime", default=f"{current_date}T00:00:00Z",
    type=str)
    end_date = args.get("endTime", default=f"{current_date}T23:50:00Z",
    type=str)

    params = {
        'sortBy': 'startTime',
        'sortOrder': 'asc',
        'pageSize': 254,
        'startTime': start_date,
        'endTime': end_date
    }

    r = requests.get(url=URL, params=params, headers=api_key_headers)
    data = r.json()
    print(data)
    response = make_response(data, 200)
    print(response)
    return response
