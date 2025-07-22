def chatbot(user_input):
    if "hi" in user_input.lower():
        return "Hello! how can i help you?"
    elif "bye" in user_input.lower():
        return "Bye"
    else:
        return "Do not understand"
    
user_input = input("Want to chat with chatbot\n")
print(chatbot(user_input))