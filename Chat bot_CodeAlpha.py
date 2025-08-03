def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "name" in user_input:
        return "I'm ChatBot, I here to help you"
    elif "help" in user_input:
        return "Sure! Ask me anything simple."
    else:
        return "I'm not sure how to respond to that."
def start_chat():
    print("Welcome to the Basic ChatBot!")
    print("Let's start the conversation. Type 'exit' to end.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("ChatBot: Bye! See you again.")
            break
        if not user_input.strip():
            print("ChatBot: Please enter something.")
            continue
        response = chatbot_response(user_input)
        print("ChatBot:", response)
# Run the chatbot
start_chat()