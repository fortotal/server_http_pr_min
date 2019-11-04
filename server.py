#!/usr/bin/env python3
import json
import socket

from flask import Flask
from flask import jsonify
from flask import request

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65430        # Port to listen on (non-privileged ports are > 1023)

hash = {}

appf = Flask(__name__)

@appf.route("/get", methods = ["GET"])
def post():
    resp = request.data.decode("utf-8")
    resp = json.loads(resp)
    try:
        datafrHash = hash[resp["key"]]
        return json.dumps({"status": "Ok", "message": datafrHash}).encode("utf-8")
    except KeyError:
        return json.dumps({"status": "Not Found"}).encode("utf-8"), '404'
    except:
        return "Internal Server Error".encode("utf-8"), '403'

@appf.route("/delete", methods = ["DELETE"])
def delete():
    resp = request.data.decode("utf-8")
    resp = json.loads(resp)
    try:
        del hash[resp["key"]]
        return json.dumps({"status":"OK"}).encode("utf-8")
    except KeyError:
        return json.dumps({"status": "Not Found"}).encode("utf-8"), '404'
    except:
        return "Internal Server Error".encode("utf-8"), '403'

@appf.route("/put", methods = ["PUT"])
def put():
    resp = request.data.decode("utf-8")
    resp = json.loads(resp)
    try:
        hash[resp["key"]] = resp["message"]
        return json.dumps({"status":"Create"}).encode("utf-8")
    except:
        return "Internal Server Error".encode("utf-8"), '403'

appf.run(host = HOST, port = PORT)
