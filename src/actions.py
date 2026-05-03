import datetime
import webbrowser

def perform_action(tag):

    if tag == "greeting":
        return "Hello! How can I help you?"

    elif tag == "time":
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif tag == "open_app":
        webbrowser.open("https://www.google.com")
        return "Opening Chrome..."

    else:
        return "I am not sure how to help with that."