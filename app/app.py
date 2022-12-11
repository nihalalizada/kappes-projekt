from typing import List, Dict
from flask import Flask, render_template, request
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

@app.route('/index.html', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
  
       if username =='test' and password == 'test':
         return render_template('loggedIn.html')
       
    return render_template('index.html', error=True)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)