import os

from flask import Flask, send_from_directory, jsonify

from loans import get_total_amount_24_hour_exp_loans
from flask_cors import CORS

app = Flask(__name__, static_folder='frontend/build')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('frontend/build', 'index.html')


@app.route('/loans')
def loans():
    data, total_remaining_amount, total_amount = get_total_amount_24_hour_exp_loans()
    return jsonify(data)

@app.route('/<path:path>')
def api(path):
    if os.path.exists("frontend/build/" + path):
        return send_from_directory('frontend/build', path)
    else:
        return send_from_directory('frontend/build', 'index.html')


if __name__ == '__main__':
    app.run(port=5000)
