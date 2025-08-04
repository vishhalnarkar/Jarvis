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
from features import search
# features/desktop.py
from features import open_app

# TODO: Not Saying "Opening" when opening apps & Websites, likely a problem in online.py.
if __name__ == "__main__":
    while True:
        say("Hello, How may I assist you?")
        command = listen()
        if command:
            if "open" in command:
                if "website" in command:
                    open_website(command.replace("open website ", ""))
                else:
                    open_app(command.replace("open ", ""))
            elif "search" in command:
                search(command.replace("search ", "").lower())
            elif "close" in command:
                break