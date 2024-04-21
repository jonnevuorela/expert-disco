from flask import Flask, jsonify, request
import pymysql
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

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
@app.route("/osallistujat/<int:id>", methods=["GET", "PATCH"])
def osallistujat(id):
    if request.method == "GET":
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM osallistujat WHERE id=%s", (id,))
            results = cursor.fetchall()
            columns = get_column_names(cursor)
            data = create_dict_data(results, columns)
            cursor.close()
            return jsonify(data)
        except Exception as e:
            return jsonify(format(e), 500)
    elif request.method == "PATCH":
        try:
            cursor = db.cursor()
            data = request.get_json()
            values=[]
            columns = []
            for column, value in data.items():
                columns.append(f"{column} = %s")
                values.append(value)
            values.append(id)
            query=f"UPDATE osallistujat SET {', '.join(columns)} WHERE id = %s"
            cursor.execute(query, values)
            db.commit()
            return jsonify({"message": "Tietokannan päivitys onnistui"}), 200
        except Exception as e:
            return jsonify(format(e), 500)

def get_column_names(cursor):
    description = cursor.description
    columns = []
    for d in description:
        column_name = d[0]
        columns.append(column_name)
    return columns

def create_dict_data(results):
    dict_data = []
    for r in results:
        dict_data.append(dict(r))
    return dict_data

