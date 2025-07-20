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

# Testing the Code after updates
if __name__ == "__main__":
    # say(RequestGeminiAPI(listen()))
    # open_website("weather today")
    
    sentence = "Open YouTube and search".lower()
    if "open" in sentence:
        open_website(sentence)
    elif "search" in sentence:
        google_search(sentence.replace("search", "").strip())
    else:
        print("No valid command found in the command.")
        say("No valid command found in the command.")

'''
open websites 
search google
open desktop files 
delete files
open applications

'''
