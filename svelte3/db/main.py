from flask import Flask, jsonify, request
import pymysql
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

# Initialize PyMySQL using configuration variables
db = pymysql.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    db=MYSQL_DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
@app.route("/osallistujat/")
def get_osallistujat():
    try:
        print("Hello")
        cursor = db.cursor()
        cursor.execute('SELECT * FROM osallistujat')
        results = cursor.fetchall()
        columns = get_column_names(cursor)
        cursor.close()
        return jsonify(results)
    except Exception as e:
        return jsonify(format(e), 500)
@app.route("/osallistujat/<int:id>")
def get_numero(id):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM osallistujat WHERE id=%s" % id)
        results = cursor.fetchall()
        columns = get_column_names(cursor)
        data = create_dict_data(results, columns)
        cursor.close()
        return jsonify(data)
    except Exception as e:
        return jsonify(format(e), 500)
@app.route("/osallistujat/<int:id>", methods=["PUT"])
def replace(id):
    try:
        cursor = db.cursor()
        data = request.get_json()
        values=[]
        columns = []
        for column, value in data.items():
            values.append(value)

def get_column_names(cursor):
    description = cursor.description
    columns = []
    for d in description:
        column_name = d[0]
        columns.append(column_name)
    return columns

def create_dict_data(results, column_names):
    dict_data = []
    for r in results:
        row_zip = zip(column_names, r)
        row_dict = dict(row_zip)
        dict_data.append(row_dict)
    return dict_data

