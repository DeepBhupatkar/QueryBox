import openai
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

api_key = ‘YOURAPIKEY’

@app.route('/api', methods=['GET'])
def hello1():
    return jsonify({'message': 'Hello, this is your REST API!'})

@app.route('/api/chatgpt/<question>', methods=['GET'])
def hello(question):
    response = generate_response(question)
    return jsonify({'message': response})

def generate_response(question):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    return response.choices[0].message['content']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

