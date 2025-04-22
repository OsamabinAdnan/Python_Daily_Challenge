# A simple chatbot implementation that responds to user input based on predefined responses
def chatbot():
    # Dictionary containing predefined responses for various user inputs
    # Keys are user inputs (in lowercase) and values are the chatbot's responses
    response = {
        'hi': "Hello! How can I assist you today?",
        'hello': "Hi there! How can I help you?",
        'how are you?': "I'm just a computer program, but I'm here to help you!",
        'bye': "Goodbye! Have a great day!",
        'what is your name?': "I'm a chatbot created to assist you.",
        'tell me a joke': "Why don't scientists trust atoms? Because they make up everything!",
    }

    # Display welcome message when the chatbot starts
    print('\nChatbot: Hello! I am a simple chatbot. Ask me something!\n')
    
    # Main conversation loop
    while True:
        # Get user input and convert to lowercase for case-insensitive matching
        user_input = input('You: ').lower()
        
        # Check if the user input matches any predefined responses
        if user_input in response:
            # Print the corresponding response from the dictionary
            print(f'Chatbot:, {response[user_input]}\n')
            # Exit the loop if user says 'bye'
            if user_input == 'bye':
                break
        else:
            # Default response for unrecognized inputs
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")

# Main function to start the chatbot
def main():
    chatbot()

# Entry point of the program
if __name__ == "__main__":
    main()
