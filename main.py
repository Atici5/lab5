import nltk
from nltk.tokenize import word_tokenize
import datetime

# Function to get bot responses
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings responses
    greetings = ["hello", "hi", "hey", "greetings", "good morning", "good evening"]
    for word in word_tokenize(user_input):
        if word in greetings:
            return "Hello! How can I assist you today?"

    # Thank you responses
    if "thank" in user_input:
        return "You're welcome! Can I help you with anything else?"

    # Goodbye responses
    if "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Have a great day!"

    # Refund or Return
    elif "refund" in user_input or "return" in user_input:
        return "Can you please provide your order number?"

    # Order Number Handling
    elif user_input.startswith("my order number is"):
        return "Thank you! We are processing your return request."

    # Problem or Issue
    elif "problem" in user_input or "issue" in user_input:
        return "I'm sorry to hear that. Could you please describe the problem?"

    # Emotional responses based on user sentiment
    elif "angry" in user_input or "frustrated" in user_input:
        return "I'm really sorry you're feeling this way. How can I help to resolve this?"

    elif "happy" in user_input or "great" in user_input:
        return "I'm glad to hear you're happy! How can I assist you further?"

    # Handling unrecognized input
    return "I’m not sure I understand. Can you please rephrase your question?"

# Function to log the conversation to a text file
def log_conversation(user_input, bot_response):
    with open("backend/chat_log.txt", "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] You: {user_input}\n")
        log_file.write(f"[{timestamp}] Bot: {bot_response}\n\n")

# Main function to start the chatbot
def main():
    print("AI Customer Service Chatbot - Type 'exit' to quit")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Thank you for contacting us. Goodbye!")
            break

        # Get the bot's response and print it
        response = get_bot_response(user_input)
        print("Bot:", response)

        # Log the conversation
        log_conversation(user_input, response)

# Run the chatbot
if __name__ == "__main__":
    main()




