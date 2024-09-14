from flask import Flask, render_template, request
from convert_handler import convert_handler

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def currency_convert():
    if request.method == "GET":
        return render_template("app.html")
    input_text = request.form["input_text"]
    result = convert_handler(input_text)
    return render_template("app.html", result=result)
