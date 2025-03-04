import nltk
import random
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-matching
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you", ["I'm good, thank you!", "Doing well, about you?"]],
    [r"what is your name", ["I'm a chatbot created with NLP."]],
    [r"quit|bye", ["Goodbye!", "See you later!"]]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    """Generate a response from the chatbot."""
    response = chatbot.respond(user_input)
    return response if response else "I'm not sure how to respond to that."

if __name__ == "__main__":
    print("AI Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
