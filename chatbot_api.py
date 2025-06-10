from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample chatbot responses (You can replace this with an actual chatbot API later)
responses = {
    "hello": ["Hello! How can I help you?", "Hi there! Need any assistance?"],
    "electricity bill": ["You can check your insights for bill details.", "Try reducing appliance usage to save on bills."],
    "usage": ["Your electricity usage details are available in the insight section."],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase?"]
}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_message = data.get("message", "").lower()

    # Find a response or use a default one
    reply = responses.get(user_message, responses["default"])
    
    return jsonify({"response": random.choice(reply)})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
