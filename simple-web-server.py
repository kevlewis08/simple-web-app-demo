from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("simple-web-page.html")
# end index()

@app.route("/home")
def home():
    return render_template("home.html")
# end home()


app.run(host="0.0.0.0", port=80)


