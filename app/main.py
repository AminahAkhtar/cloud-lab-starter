import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello from SE-490 Cloud Computing Lab!",
                   version=os.getenv("APP_VERSION", "dev"))


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/add")
def add():
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except ValueError:
        return jsonify(error="Provide numeric query params a and b"), 400
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
