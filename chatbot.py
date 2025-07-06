print("Hello! I'm ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hi there! How can I help you today?")
    elif "your name" in user_input:
        print("Bot: I'm ChatBot, your virtual assistant.")
    elif "help" in user_input:
        print("Bot: I can answer simple questions. Ask me anything!")
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day 😊")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
