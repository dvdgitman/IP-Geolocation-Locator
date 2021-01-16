from flask import Flask

from PythonApps import iplocator

app = Flask(__name__)

@app.route("/ip")

def ip():
 return iplocator.response

if __name__ == "__main__":
    app.run(debug=True,port=5000)



