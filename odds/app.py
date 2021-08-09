from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/odds")
def index():
    return jsonify({"data": "Connection had been made"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
