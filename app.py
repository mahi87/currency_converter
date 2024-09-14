from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def health():
    return jsonify({"message": "Hello World"})


@app.route("/convert")
def currency_convert():

    return jsonify({"message": "converting currency"})
