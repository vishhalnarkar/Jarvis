# For Offline Speech-to-Text using Vosk
import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# For Online Speech-to-Text 
import speech_recognition as sr

# For Text-to-Speech
from features.tts import say

# Constants and global variables for Vosk model (initialized later)
SAMPLE_RATE, BLOCK_SIZE, MODEL_PATH = 16000, 8000, "models/vosk-model-en-in-0.5"
vosk_model, vosk_recognizer = None, None
audio_queue = queue.Queue()  # Define once globally

# Function to initialize the Vosk model for offline speech-to-text
def offline_stt_init():
    global vosk_model, vosk_recognizer
    if vosk_model is not None and vosk_recognizer is not None:
        return  # Already initialized

    print("Initializing Vosk Model for Offline Speech-to-Text...")

    # Load the Vosk model
    vosk_model = Model(MODEL_PATH)
    vosk_recognizer = KaldiRecognizer(vosk_model, SAMPLE_RATE)
    vosk_recognizer.SetWords(True)

    print("Vosk Model Initialized Successfully...\n")

# Callback function to handle audio input
def audio_callback(indata, frames, time, status):
    if status:
        print(f"Audio input status: {status}")
    audio_queue.put(bytes(indata))

# Function to listen and convert voice to text using Vosk (Offline)
def offline_listen(timeout: int = 5) -> str:
    # Ensure model is initialized before listening
    offline_stt_init()  

    # Start Listening
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
            if vosk_recognizer.AcceptWaveform(data):
                result = json.loads(vosk_recognizer.Result())
                result_text = result.get("text", "")
                break  

        if not result_text:
            partial = json.loads(vosk_recognizer.PartialResult())
            result_text = partial.get("partial", "")

    print(f"Recognized Text: {result_text}\n")
    return result_text.strip()

# Function to listen and convert voice to text using Google API (Online)
google_recognizer = sr.Recognizer()  
def online_listen():
    with sr.Microphone() as source:
        try:
            print("Listening...")
            google_recognizer.adjust_for_ambient_noise(source) 
            audio = google_recognizer.listen(source)
            print(audio)
            return google_recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
