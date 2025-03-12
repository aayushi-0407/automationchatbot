from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_URL = "http://localhost:5000/configure_ran"

@app.route("/chat", methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = requests.post(API_URL, json={"message": user_input})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=5001)
