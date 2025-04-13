import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Dummy bot response function
def get_bot_response(user_input):
    if "order" in user_input.lower():
        return "Can you please provide your order number?"
    elif "refund" in user_input.lower():
        return "Sure, I can help with a refund. What is your order number?"
    elif "hello" in user_input.lower():
        return "Hi there! How can I assist you today?"
    else:
        return "I'm not sure I understand. Can you rephrase your question?"

# Save conversation to file
def log_conversation(user_input, bot_response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] You: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_response}\n")

# Send message function
def send_message():
    user_input = input_field.get()
    if user_input.strip() == "":
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_input}\n")
    response = get_bot_response(user_input)
    chat_area.insert(tk.END, f"Bot: {response}\n\n")
    chat_area.config(state='disabled')
    input_field.delete(0, tk.END)
    log_conversation(user_input, response)

# GUI Setup
window = tk.Tk()
window.title("AI Customer Service Chatbot")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, font=("Helvetica", 12))
chat_area.pack(padx=10, pady=10)
chat_area.config(state='disabled')

input_field = tk.Entry(window, width=50, font=("Helvetica", 12))
input_field.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(window, text="Send", command=send_message, font=("Helvetica", 12))
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

window.mainloop()
def get_bot_response(message):
    return f"Sen dedin ki: {message}"




