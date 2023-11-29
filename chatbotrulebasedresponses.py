# Define a set of rules and responses
rules = {
    "hey hi": "Hello,who can i help you!",
    "which programming languages are important in this generation": " core java,python !",
    "why an ai is useful?": "ai is the future ,it decreases the human work and increases the technology !",
    "do you know about the codsoft company?": " yeah,codsoft company is provides alot of jobs and interships!",
    "bye": "Goodbye! Have a great day!"
}

# Function to generate responses based on user input
def generate_response(user_input):
    user_input = user_input.lower()
    for pattern, response in rules.items():
        if pattern in user_input:
            return response
    return "I'm  really sorry, can you please repeat the sentence."

# Main loop to interact with the chatbot
while True:
    user_input = input("HUMAN: ")
    response = generate_response(user_input)
    print("Chatterbox: " + response)
