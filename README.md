# Jarvis

Python Packages Used:  
google-genai - Gemini API
python-dotenv - Load data from .env
pyttsx3 - Text to Speech
vosk - Offline Speech to Text
sounddevice - Captures mic input in real-time
webbrowser - Open Websites in Browser 
SpeechRecognition - Online Speech to Text
pyaudio - Speech Recognition needs it ig, throwing an error without it

Command To Install 

```
pip install google-genai python-dotenv pyttsx3 vosk SpeechRecognition
```

# File Structure 

Jarvis
|- main.py
|- features
    |- __init__.py
    |- desktop.py
    |- online.py
    |- stt.py
    |- tts.py
    |- shortcut_index.csv 
|- models
    |- vosk-model-small-en-us-0.15
|- .gitignore
|- .env
|- README.md