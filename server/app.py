from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def root():
    return send_file('index.html')
