import sys
from flask import Flask
import iplocator
from flask import jsonify
from flask import request

app = Flask(__name__)

sys.path.append('/var/jenkins_home/workspace/DockerNode/')


@app.route("/ip", methods=['GET', 'POST'])
def ip():
    return jsonify("IP:" + iplocator.ip, "City:" + iplocator.city,
                   "Region:" + iplocator.region, "Country:" + iplocator.country)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
