from src.predict import predict_class
from src.actions import perform_action

print("Smart Task Executor started (type 'quit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    tag = predict_class(user_input)

    if tag == "unknown":
        print("Bot: I didn't understand that.")
        continue

    response = perform_action(tag)
    print("Bot:", response)