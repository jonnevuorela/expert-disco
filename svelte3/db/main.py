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


@app.route("/osallistujat/", methods=["GET"])
@app.route("/osallistujat/<int:id>", methods=["GET", "PATCH", "POST","DELETE"])
def osallistujat(id=None):
    if request.method == "GET":
        try:
            print('Hello')
            cursor = db.cursor()
            if id is None:
                cursor.execute('SELECT * FROM osallistujat')
            else:
                cursor.execute("SELECT * FROM osallistujat WHERE id=%s" % id)
            results = cursor.fetchall()
            columns = get_column_names(cursor)
            data = create_dict_data(results, columns)
            cursor.close()
            return jsonify(results)
        except Exception as e:
            return jsonify(format(e), 500)
    elif request.method == "PATCH":
        try:
            cursor = db.cursor()
            data = request.get_json()
            print("data",data)
            values=[]
            columns = []
            for column, value in data.items():
                columns.append(f"{column} = %s")
                values.append(value)
            values.append(id)
            query=f"UPDATE osallistujat SET {', '.join(columns)} WHERE id = %s"
            print("query",query)
            print("values",values)
            cursor.execute(query, values)
            db.commit()
            return jsonify({"message": "Tietokannan päivitys onnistui"}), 200
        except Exception as e:
            return jsonify(format(e), 500)
    elif request.method == "POST":
        try:
            cursor = db.cursor()
            data = request.get_json()
            print("data",type(data),data)
            for item in data:
                values=[]
                columns = []
                for column, value in data.items():
                    columns.append(column)
                    values.append(value)
            query=f"INSERT INTO osallistujat ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(values))})"
            print("query",query)
            print("values",values)
            cursor.execute(query, values)
            db.commit()
            return jsonify({"message": "Tietokannan päivitys onnistui"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM osallistujat WHERE id = {id}")
            db.commit()
            return jsonify({"message": "Osallistuja poistettu"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

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
