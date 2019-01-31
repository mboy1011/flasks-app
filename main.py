from flask import Flask
from flask import render_template,request,session

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')