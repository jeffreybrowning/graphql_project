from flask import Flask

app = Flask(__name__)

@app.route('/')
def loans():
    return 'Hello World!'
