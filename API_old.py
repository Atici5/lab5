from flask import Flask, request, jsonify
from backend.chatbot_v2 import get_bot_response

app = Flask(__name__, template_folder='templates')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')

    # Şimdilik sadece gelen mesajı geri döndürüyoruz
    response = get_bot_response(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
