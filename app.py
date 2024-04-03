from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'dbteste'

@app.route("/")
def index():
    return "ERIC ERIC ERIC"

if __name__ == "__main__":
    app.run()
