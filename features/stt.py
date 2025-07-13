# For Speech-to-Text
import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
# For Text-to-Speech
from features.tts import say

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

