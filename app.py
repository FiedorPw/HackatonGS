from flask import Flask, jsonify, request, render_template
import requests
import logging
import os
from utils.logger import CustomFormatter

app = Flask(__name__)
messages = []
files = []

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

@app.route('/get_files')
def get_files():
    return jsonify(files)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    logger.info(f'Received user file: {file.filename}')
    file.save(os.path.join('uploads', file.filename))
    files.append(file.filename)
    return jsonify(success=True)

@app.route('/login')
def login():
    logger.info('Detected sign in attempt')
    return render_template('login.html')

@app.route('/about')
def about():
    logger.info('Detected about page request')
    return render_template('about.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app.run(debug=True)