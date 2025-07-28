# For Text-to-Speech
import pyttsx3

# Init  the Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak the response using Text-to-Speech using pyttsx3 Library
def say(text):
    print(f"Speaking: \'{text}\'")
    engine.say(text)
    engine.runAndWait()
    print("End response...\n")
