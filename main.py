# Importing the necessary modules from the features package
# features/gemini_api.py
from features import RequestGeminiAPI 
# features/tts.py
from features import say 
# features/stt.py
from features import listen 
# features/online.py
from features import open_website 

# Testing After Organizing the Code
if __name__ == "__main__":
    say(RequestGeminiAPI(listen()))
    open_website(listen())