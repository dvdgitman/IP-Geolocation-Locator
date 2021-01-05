from flask import Flask

from PythonApps import iplocator

app = Flask(__name__)

@app.route("/ip", methods=["GET", "POST"])

def hello():
 return "Here we will check geolocation from an IP address"

if __name__ == "__main__":
    app.run(debug=True,port=5000)

set FLASK_APP=iplocator.py

