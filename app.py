from flask import Flask, flash, request, render_template
from flask_session import Session


# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")