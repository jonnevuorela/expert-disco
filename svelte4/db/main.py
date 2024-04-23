import requests

from datetime import date
from flask_cors import CORS
from flask import Flask, make_response, request
from config import API_KEY

app = Flask(__name__)
CORS(app)

URL = "https://data.fingrid.fi/api/datasets/242/data?format=json"
api_key_headers = {
    'x-api-key': API_KEY
}


@app.route("/e_production")
def doRequest():
    current_date = date.today()
    args = request.args
    start_date = f"{current_date}T00:00:00Z"
    end_date = args.get("endTime", default=f"{current_date}T23:00:00Z", type=str)

    params = {
        'sortBy': 'startTime',
        'sortOrder': 'asc',
        'pageSize': 100,
        'startTime': start_date,
        'endTime': end_date
    }

    r = requests.get(url=URL, params=params, headers=api_key_headers)
    data = r.json()
    print(data)
    return make_response(data, 200)
