from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/gatos')
def gatos():
    return render_template("Gatos.html") 

@app.route('/peces')
def peces():
    return render_template("Peces.html")  

@app.route('/perros')
def perros():
    return render_template("Perros.html")

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
