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
    # say(RequestGeminiAPI(listen()))
    # open_website("weather today")
    
    open_app("visual studio code")

'''
open websites 
search google
open desktop files 
delete files
open applications

'''
