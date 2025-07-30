# Importing the necessary modules from the features package
# features/gemini_api.py
from features import RequestGeminiAPI 
# features/tts.py
from features import say 
# features/stt.py
from features import listen 
# features/online.py
from features import open_website 
# features/online.py
from features import google_search
# features/desktop.py
from features import open_app

# Testing the Code after updates
if __name__ == "__main__":
    while True:
        say("Hello, How may I assist you?")
        command = listen()
        if "open" in command:
            open_app(command.replace("open ", ""))
        elif "search" in command:
            google_search(command.replace("search ", ""))
        elif "exit" in command:
            break