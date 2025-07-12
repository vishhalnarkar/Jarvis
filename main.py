# To load environment variables from .env file
import os
from dotenv import load_dotenv
# For Gemini API
from google import genai 
# For Text-to-Speech
import pyttsx3
# For Speech-to-Text
import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer


# Ensure you have a .env file with GEMINI_API_KEY and optionally GEMINI_API_URL

print("Loading Environment Variables from .env file...")

# Check if .env file exists
if not os.path.exists('.env'):
    raise FileNotFoundError("The .env file is missing. Please create one with the required variables.")


# Load environment variables
load_dotenv()
GEMINI_API = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL", "https://generativelanguage.googleapis.com")

# Validate that the GEMINI_API_KEY is set
if not GEMINI_API:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
client = genai.Client(api_key=GEMINI_API)
print("Environment Variables Loaded Successfully.\n")

# Constants for Speech-to-Text
SAMPLE_RATE = 16000
BLOCK_SIZE = 8000
MODEL_PATH = "models/vosk-model-en-in-0.5"

# Loading the Vosk model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)
recognizer.SetWords(True)

# Queue for audio input
audio_queue = queue.Queue()

# Function to request Gemini API and handle the response
def RequestGeminiAPI(prompt):
    if not prompt:
        raise ValueError("Prompt is empty. Cannot send an empty request to the Gemini API.")
    print(f"Sending Request to Gemini API with prompt: {prompt}\n")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    print("Sent Request to Gemini API:\nResponse:\n")
    print(response.text)
    if not response.text:   
        raise ValueError("No text response received from the Gemini API.")
    return response.text

# Function to speak the response using Text-to-Speech using pyttsx3 Library
def say(text):
    if not text:
        raise ValueError("Text is empty. Cannot speak an empty response.")
    print("Initializing Text-to-Speech Engine & Speaking...\n")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print("End response...\n")

def audio_callback(indata, frames, time, status):
    if status:
        print(f"Audio input status: {status}")
    audio_queue.put(bytes(indata))

def listen(timeout: int = 5) -> str:
    # result_text = ""
    result_text = "Error: No speech detected."
    with sd.RawInputStream(samplerate=SAMPLE_RATE,
                           blocksize=BLOCK_SIZE,
                           dtype='int16',
                           channels=1,
                           callback=audio_callback):
        print("Listening...")

        total_chunks = int((timeout * SAMPLE_RATE) / BLOCK_SIZE)
        for _ in range(total_chunks):
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                result_text = result.get("text", "")
                break  

        if not result_text:
            partial = json.loads(recognizer.PartialResult())
            result_text = partial.get("partial", "")
    print(f"Recognized Text: {result_text}\n")
    return result_text.strip()

say(listen(timeout=5))