print("Hello! I am a simple Python chatbot.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello":
        print("Bot: Hi!")

    elif user_input == "how are you" or user_input == "how are u":
        print("Bot: I'm fine, thanks!")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")