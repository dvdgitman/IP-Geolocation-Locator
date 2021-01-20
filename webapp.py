import sys
from flask import Flask
import iplocator
from flask import jsonify
import argparse

app = Flask(__name__)

sys.path.append('/var/jenkins_home/workspace/DockerNode/')


@app.route("/ip", methods=['GET', 'POST'])
def ip():
    return jsonify("IP:" + iplocator.ip, "City:" + iplocator.city,
                   "Region:" + iplocator.region, "Country:" + iplocator.country)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, help="write an IP address", required=True)
    args = parser.parse_args()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
