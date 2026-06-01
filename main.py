def chatbot():
    print("=" * 40)
    print("🤖 Welcome to Smart ChatBot")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")
    print("=" * 40)

    while True:
        user = input("\nYou: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great. Thanks for asking!")

        elif user == "what is your name":
            print("Bot: I am Smart ChatBot.")

        elif user == "who created you":
            print("Bot: I was created as a Python internship project.")

        elif user == "time":
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is", current_time)

        elif user == "date":
            from datetime import date
            print("Bot: Today's date is", date.today())

        elif user == "help":
            print("\nAvailable Commands:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- who created you")
            print("- date")
            print("- time")
            print("- bye")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")

chatbot()