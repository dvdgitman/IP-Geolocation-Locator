from flask import Flask
from PythonApps import iplocator
from flask import jsonify
from flask import json

app = Flask(__name__)


@app.route("/ip", methods=['GET', 'POST'])
def ip():
    return jsonify("IP:" + iplocator.ip, "City:" + iplocator.city,
                   "Region:" + iplocator.region, "Country:" + iplocator.country)


@app.route("/ip2", methods=['GET', 'POST'])
def ip2():
    return iplocator.response


if __name__ == "__main__":
    app.run(debug=True, port=5000)
