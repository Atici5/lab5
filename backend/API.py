from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../frontend/templates"))
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower().strip()
    print("Kullanıcı mesajı:", message)

    if "hello" in message:
        response = "Hi there! How can I help you?"
    elif "how are you" in message:
        response = "I'm just a bot, but I'm doing great!"
    elif "bye" in message:
        response = "Goodbye! Have a wonderful day!"
    elif "python" in message:
        response = "Python is a popular programming language used for AI, web development, and more."
    elif "flask" in message:
        response = "Flask is a lightweight Python web framework."
    elif "joke" in message:
        response = "Why did the computer go to therapy? Because it had too many bugs!"
    elif "your name" in message:
        response = "I'm MehmetBot, your friendly assistant."
    elif "who created you" in message:
        response = "I was created by Mehmet, using Python and a lot of coffee!"
    elif "ai" in message or "artificial intelligence" in message:
        response = "AI means machines that can think and learn like humans."
    else:
        response = "Hmm... I don't know how to answer that. Can you rephrase?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5002)




