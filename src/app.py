from flask import Flask, jsonify, render_template
import socket



app = Flask(__name__)


def fetch_specs():
    hostname = socket.gethostname()
    ip_host = socket.gethostbyname(hostname)
    return str(ip_host), str(hostname) 

@app.route("/")
def hello_world():
    return "<h1>Hello World </h1>"


@app.route("/health")
def health_checks():
    return jsonify(
        health = "Healthy"
        )

@app.route("/details")
def details():
    ip, hostname = fetch_specs()
    return render_template('index.html', IP=ip , HOSTNAME=hostname )


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)

