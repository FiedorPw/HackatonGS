from flask import Flask, jsonify, request, render_template

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
    message = request.form['message']
    messages.append(message)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)