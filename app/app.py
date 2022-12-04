from typing import List, Dict
from flask import Flask, render_template
import mysql.connector
import json

app = Flask(__name__)


def users() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'students'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    results = [{name: id} for (name, id) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> dict:
    return {'users': users()}

@app.route('/index.html')
def home():
    title = 'Home'
    return render_template('index.html', title = title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)