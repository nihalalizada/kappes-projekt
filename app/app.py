from contextlib import _RedirectStream
from typing import List, Dict
from urllib.request import Request
from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__, static_folder='static')

""" Abfrage proxy server verbunden oder nicht
@app.route('/')
def index():
    # Request zum Proxy Server
    proxy_server_url = "http://localhost:8080"
    try:
        r = Request.get(proxy_server_url)
        # wenn Requenst stimmt
        return render_template('index.html')
    except:
        # wenn Request nicht stimmt
        return _RedirectStream("http://localhost:5000/unauthorized")
 """

@app.route('/transfer.html', methods =['GET', 'POST'])
def register():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'projekt'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    if request.method == 'POST':
        name = request.form.get('name')
        iban = request.form.get('iban')
        amount = request.form.get('amount')
        purpose = request.form.get('purpose')
        if not name or not iban or not amount or not purpose:
            msg = 'Please fill out the form!'
            return render_template('transfer.html', msg=msg)
        if not re.match(r'^[A-Z]{2}(?:[ ]?[0-9]){18,20}$', iban):
            msg = 'Invalid IBAN!'
            return render_template('transfer.html', msg=msg)
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s)', (name, iban, amount, purpose))
        connection.commit()
        msg = 'You have successfully transferred'
        return render_template('transfer.html', msg=msg)
    else:
        msg = 'Please fill out the form !'
        return render_template('transfer.html', msg=msg)

@app.route('/index.html', methods=['POST', 'GET'])
def home():
    msg = ''
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
  
       if username =='test' and password == 'test':
         return render_template('transfer.html')
       msg='Invalid Login Details'
    return render_template('index.html', msg = msg)


@app.route('/unauthorized')
def unauthorized():
    return render_template('/unauthorized.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)