from flask import Flask, jsonify, request, render_template
import requests
import logging
import os
from utils.logger import CustomFormatter

app = Flask(__name__)
messages = []

# Logger setup
log_level = 'INFO'
logger = logging.getLogger(__name__)
logger.setLevel(log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

@app.route('/')
def index():
    messages.clear()
    return render_template('index2.html')

@app.route('/get_messages')
def get_messages():
    return jsonify(messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    messages.clear()
    message = request.form['message']
    logger.info(f'Received user message: {message}')
    response = requests.post('http://localhost:8000/assistant/', json={'user_id' : 1, 'message': message})
    messages.append(response.json()['message'])
    return jsonify(success=True)

@app.route('/login')
def login():
    logger.info('Detected sign in attempt')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)