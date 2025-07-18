from features import gemini_api as gemini
from features.tts import *
from features.stt import listen
from features.online import open_website

# Testing After Organizing the Code
if __name__ == "__main__":
    while True:
        open_website(listen())