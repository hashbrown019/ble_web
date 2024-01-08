
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/_test_')
def index():
    return render_template("home.html")

@app.route('/')
def hello_world():
    return "Running"
