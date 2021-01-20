from flask import Flask
from PythonApps import iplocator
from flask import jsonify

app = Flask(__name__)

FLASK_ENV = '-i 1.1.1.1'


@app.route("/ip", methods=['GET', 'POST'])
def ip():
    return jsonify("IP:" + iplocator.ip, "City:" + iplocator.city,
                   "Region:" + iplocator.region, "Country:" + iplocator.country)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
