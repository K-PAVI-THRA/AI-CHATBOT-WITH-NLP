import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's response patterns
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?']),
    (r'how are you?', ['I am doing great, thank you for asking! How about you?']),
    (r'what is your name?', ['I am a chatbot created by Codtech. You can call me Codbot!']),
    (r'bye|goodbye', ['Goodbye! Have a great day!']),
    (r'what is (.*)', ['I am sorry, I do not have information about "%1". Can you ask something else?']),
    (r'help', ['Sure, how can I help you?']),
    (r'(.*) your (.*)', ['Please refrain from asking that kind of question.']),
    (r'(.*)', ['Sorry, I did not understand that. Can you ask again?']),
]

# Function to initiate the chatbot
def chatbot():
    print("Hello, I am Codbot. Type 'bye' to end the conversation.")  # Initial greeting
    chat = Chat(pairs, reflections)  # Create a Chat object
    chat.converse()  # Start the conversation

# Run the chatbot
if __name__ == "__main__":
    chatbot()
