import socket

# =================================
IN_MAINTENANCE = False
# IN_MAINTENANCE = False
# =================================

print(" ++ Configuration Setting ++")
host_name = socket.gethostname()
IP_address = socket.gethostbyname(host_name)

print(f" * --{IP_address}")
# A very simple Flask Hello World app for you to get started with...
from flask_cors import CORS,cross_origin
from flask import Flask, render_template,request, jsonify
import json, os
import path_finder

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key="blebleblebleble"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False

@app.route('/path_finder',methods=["POST","GET"])
def path_finder_():
    return jsonify(path_finder.find_())

@app.route('/usermode',methods=["POST","GET"])
def index():
    return render_template("home.html",beacons = ls_ble())

@app.route('/adminmode',methods=["POST","GET"])
def admin():
    return render_template("admin.html",beacons = ls_ble())

def ls_ble():
    res = []
    dir_path = "assets/"
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            f = open(f"assets/{path}","r")
            res.append(json.loads(f.read()))
            f.close()
    return(res)

@app.route('/save_ble',methods=["POST","GET"])
def save_ble():
    codes = request.form['f_code']
    f = open(f"assets/{codes}","w")
    f.write(json.dumps(dict(request.form)))
    return "finished"

@app.route('/status',methods=["POST","GET"])
def status():
    res = []
    f = open("status/status.json","r")
    res = f.read()
    f.close()
    return res

@app.route('/del_ble/<code>',methods=["POST","GET"])
def del_ble(code):
    os.remove("assets/"+code)
    return "finished"

@app.route('/sample',methods=["POST","GET"])
def sample():
    return jsonify([
        {
            "latlong" : "7.069281, 125.622102",
            "name": "Danger construction",
            "description" : "sample description"
        },
        {
            "latlong" : "7.076725, 125.623693",
            "name": "Road Rage ahead",
            "description" : "sample description"
        },
    ])

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0")
	# app.run(debug=True,host="0.0.0.0",ssl_context='adhoc')