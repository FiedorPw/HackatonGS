from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    messages.clear()
    return render_template('index2.html')

@app.route('/get_messages')
def get_messages():
    print(messages)
    return jsonify(messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    messages.clear()
    message = request.form['message']
    print("request: " + str(request))
    response = requests.post('http://localhost:8000/assistant/', json={'user_id' : 1, 'message': message})
    print(response.json())
    messages.append(response.json()['message'])
    print(messages)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)