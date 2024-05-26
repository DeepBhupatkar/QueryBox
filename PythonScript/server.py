import openai
from flask import Flask, jsonify, request, send_file

# Create a Flask application instance
app = Flask(__name__)

# Your OpenAI API key for authentication
api_key = 'YOURAPIKEY'

# Define a route for the root of the API that responds to GET requests
@app.route('/api', methods=['GET'])
def hello1():
    # Return a JSON response with a greeting message
    return jsonify({'message': 'Hello, this is your REST API!'})

# Define a route for the ChatGPT API that takes a question as a URL parameter
@app.route('/api/chatgpt/<question>', methods=['GET'])
def hello(question):
    # Generate a response to the given question using the ChatGPT model
    response = generate_response(question)
    # Return the generated response as a JSON object
    return jsonify({'message': response})

# Function to generate a response from the ChatGPT model
def generate_response(question):
    # Set the OpenAI API key for authentication
    openai.api_key = api_key
    # Create a chat completion request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # System message to set the context
            {"role": "user", "content": question},  # User message containing the question
        ]
    )
    # Return the generated response content from the API
    return response.choices[0].message['content']

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all network interfaces (0.0.0.0) and port 5000
