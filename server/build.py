from flask import Flask, send_file
from flask_frozen import Freezer

app = Flask(__name__)

@app.route('/')
def root():
    return send_file('index.html')

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()