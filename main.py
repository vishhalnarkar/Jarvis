from features import gemini_api as gemini
from features.tts import *
from features.stt import online_listen, offline_listen
from features.web_open import open_website

# Testing After Organizing the Code
if __name__ == "__main__":
    while True:
        open_website(offline_listen())