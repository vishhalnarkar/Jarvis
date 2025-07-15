# Jarvis 🧠🎙️

**Jarvis** is a desktop-based AI voice assistant built in Python. It supports both **online and offline speech recognition**, integrates with **Gemini (Google's LLM)**, and can perform tasks like speaking responses, opening websites, fetching news, and more.

---

## 🚀 Features

- ✅ **Offline Speech-to-Text** via [Vosk](https://alphacephei.com/vosk/)
- ✅ **Online Speech-to-Text** using Google's API via `SpeechRecognition`
- ✅ **Text-to-Speech** using `pyttsx3` (offline)
- ✅ **Gemini LLM Integration** for intelligent responses
- ✅ **Website & Music Commands**
- ✅ **Multi-threaded Text-to-Speech**
- ✅ `.env`-based API key handling

---

## 📦 Python Packages Used

| Package             | Purpose                                      |
|---------------------|----------------------------------------------|
| `google-genai`      | Gemini API (Google Generative AI)            |
| `python-dotenv`     | Load sensitive data from `.env`              |
| `pyttsx3`           | Offline Text-to-Speech engine                |
| `vosk`              | Offline Speech Recognition                   |
| `sounddevice`       | Real-time microphone input capture           |
| `SpeechRecognition` | Online STT using Google Web Speech API       |
| `pyaudio`           | Required by `SpeechRecognition` as backend   |
| `webbrowser`        | Standard library to open URLs in browser     |

---

## 📥 Installation

Install all required packages using pip:

```bash
pip install google-genai python-dotenv pyttsx3 vosk sounddevice SpeechRecognition pyaudio
```

---

## ⚠️ Note on PyAudio Installation

`pyaudio` may require system-level dependencies depending on your operating system. If you face errors during installation, follow the instructions below:

### 🪟 Windows

Use `pipwin`, a wrapper for installing precompiled Windows binaries:

```bash
pip install pipwin
pipwin install pyaudio
```

### 🐧 Linux

Use your package manager to install required libraries before installing `pyaudio`:

```bash
sudo apt update
sudo apt install portaudio19-dev python3-pyaudio
pip install pyaudio
```

### 🍎 macOS

Install `portaudio` using Homebrew:

```bash
brew install portaudio
pip install pyaudio
```

> 💡 **Tip:** Still having issues? Try using a virtual environment and ensure Python headers are available (`python3-dev`, `build-essential`, etc.).

---

## 🔐 .env Setup

Create a `.env` file in your project directory with your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
GEMINI_API_URL=https://generativelanguage.googleapis.com  # optional
```

---

## 🏁 Getting Started

Run your assistant using:

```bash
python main.py
```

Say the wake word (e.g., “Nova”) and start giving commands.

---

## 🧠 Tips

- Use **offline STT** (Vosk) when privacy or speed matters.
- Use **online STT** when accuracy is more important.
- Test microphone input before running.
- Threading is used for smooth TTS playback.

---

## 📄 License

MIT License – Feel free to use, modify, and share.

---

Made with ❤️ in Python
[AI Generated README]