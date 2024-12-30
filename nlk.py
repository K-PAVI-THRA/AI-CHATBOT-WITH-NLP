def chatbot():
    print("Hello, I am Codbot. Type 'bye' to end the conversation.")  # Initial greeting
    chat = Chat(pairs, reflections)  # Create a Chat object
    chat.converse()  # Start the conversation
