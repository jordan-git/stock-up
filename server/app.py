# save this as app.py
from flask import Flask, render_template

app = Flask(__name__, static_folder="../client/build", static_url_path="/")


@app.route("/")
def index():
    return app.send_static_file("index.html")
