from flask import Flask
app = Flask(__name__)

@app.route("/ip", methods=["GET", "POST"])

def hello():
 return "Here we will check geolocation from an IP address"

if __name__ == "__main__":
    app.run()