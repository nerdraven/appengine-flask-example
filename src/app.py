import json
import ipdb
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    headers = request.headers
    params = request.query_string

    # ipdb.set_trace(context=5)

    return jsonify({
        "headers": {k:v for k, v in headers.items()}
    })