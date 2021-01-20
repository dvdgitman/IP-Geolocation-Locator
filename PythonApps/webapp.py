import flask
from flask import Flask
from PythonApps import iplocator
from flask import jsonify
import argparse

app = Flask(__name__)

iplocator.py()

@app.route("/ip", methods=['GET', 'POST'])
def ip():
    return jsonify("IP:" + iplocator.ip, "City:" + iplocator.city,
                   "Region:" + iplocator.region, "Country:" + iplocator.country)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, help="write an IP address", required=True)
    args = parser.parse_args()


main()
# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
