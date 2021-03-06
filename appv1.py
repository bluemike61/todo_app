from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def list():
    return render_template('list.html')

@app.route("/base")
def home():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)