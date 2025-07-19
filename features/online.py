# Open websites in browser
import webbrowser

# For Text-to-Speech
from features.tts import say

# To Check Internet Connection
import socket

# Mapping of website names to URLs
website_map = {
    "youtube": "https://www.youtube.com",
    "whatsapp": "https://web.whatsapp.com",
    "spotify": "https://www.spotify.com",
    "google drive": "https://drive.google.com",
    "my github": "https://github.com/vishhalnarkar",
    "my linkedin": "https://www.linkedin.com/in/vishhalnarkar/",
    "this repo": "https://github.com/vishhalnarkar/Jarvis",
    "github": "https://github.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "gemini": "https://gemini.google.com/app",
    "chatgpt": "https://chat.openai.com",
    "google maps": "https://www.google.com/maps",
    "x": "https://x.com",
    "twitter": "https://x.com",
    "stack overflow": "https://stackoverflow.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "netflix": "https://www.netflix.com",
    "quora": "https://www.quora.com",
    "wikipedia": "https://www.wikipedia.org",
    "pinterest": "https://www.pinterest.com",
}

# Function to open a website based on the command
def open_website(command: str):
    if not command:
        print("Command is empty. Cannot search for websites.")
        return
    command = command.lower()
    for keyword, url in website_map.items():
        if keyword in command:
            say(f"Opening {keyword.capitalize()}...")
            print(f"Opening website: {url}\n")
            webbrowser.open(url)
            return
    else:
        print(f"Didn't find any relevant website for '{command}'.")
        say(f"Didn't find any relevant website for '{command}'.")
        google_search(command)

# Function to perform a Google search      
def google_search(query: str):
    if not query:
        print("Query is empty. Cannot perform Google search.")
        return
    say(f"Searching Google for {query}...")
    print(f"Searching Google search for: {query}\n")
    webbrowser.open("https://www.google.com/search?q=" + query)

# Check if the internet connection is available
def check_internet_connection(hosts="8.8.8.8", port=53, timeout=3):
    try:
        socket.create_connection((hosts, port), timeout)
        print("Internet Available")
        return True
    except OSError:
        print("Internet Not Available")
        return False
