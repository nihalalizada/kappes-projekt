from contextlib import _RedirectStream
from typing import List, Dict
from urllib.request import Request
from flask import Flask, render_template, request
import mysql.connector
import json

app = Flask(__name__, static_folder='static')

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
def index():
    # Make a request to the proxy server
    proxy_server_url = "http://localhost:8080"
    try:
        r = Request.get(proxy_server_url)
        # If the request is successful, render the template
        return render_template('index.html', users=users())
    except:
        # If the request is not successful, redirect the user to the unauthorized page
        return _RedirectStream("http://localhost:5000/unauthorized")


@app.route('/index.html', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
  
       if username =='test' and password == 'test':
         return render_template('loggedIn.html')
       
    return render_template('index.html', error=True)

@app.route('/unauthorized')
def unauthorized():
    return render_template('/unauthorized.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)