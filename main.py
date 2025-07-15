from features import gemini_api as gemini
from features.tts import *
from features.stt import online_listen, offline_listen
from features.web_open import open_website

# Testing After Organizing the Code
if __name__ == "__main__":
    say(gemini.RequestGeminiAPI("What is the capital of India ?"))
    open_website(online_listen())