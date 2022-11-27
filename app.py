from flask_mysqldb import MySQL
from flask import Flask,render_template
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'php_docker'
mysql = MySQL(app)


@app.route("/")
def hello_world():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM php_docker")
    result = cursor.fetchall()
    cursor.close()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)