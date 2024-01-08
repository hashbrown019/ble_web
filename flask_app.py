
# A very simple Flask Hello World app for you to get started with...
from flask_cors import CORS,cross_origin
from flask import Flask, render_template,request

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key="blebleblebleble"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False

@app.route('/_test_',methods=["POST","GET"])
def index():
    return render_template("home.html")

@app.route('/',methods=["POST","GET"])
def admin():
    return render_template("admin.html")


@app.route('/admin',methods=["POST","GET"])
def admin():
    return render_template("admin.html")


@app.route('/save_ble',methods=["POST","GET"])
def save_ble():
    codes = request.form['code']
    f = open(f"assets/{codes}","w")
    f.write(dict(request.form))
    return "finished"
    # heheh
