from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    # INTENTIONAL BUG (KeyError if password missing)
    username = data["username"]
    password = data["password"]  # will crash if missing

    if username == "admin" and password == "admin":
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"}), 401

@app.route("/health")
def health():
    return "OK", 200

app.run(host="0.0.0.0", port=5000)

