#simple_chatbot.py
while True:
    msg = input("You: ").lower()

    if "hello" in msg:
        print("Bot: Hi!")
    elif "bye" in msg:
        break
    else:
        print("Bot: I don't understand")
