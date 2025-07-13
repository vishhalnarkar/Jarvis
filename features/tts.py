# For Text-to-Speech
import pyttsx3

# Function to speak the response using Text-to-Speech using pyttsx3 Library
def say(text):
    if not text:
        raise ValueError("Text is empty. Cannot speak an empty response.")
    print("Initializing Text-to-Speech Engine & Speaking...\n")
    engine = pyttsx3.init()
    engine.say(text)
    print(f"Speaking: \'{text}\'\n")
    engine.runAndWait()
    print("End response...\n")