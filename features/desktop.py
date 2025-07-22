import os 
import subprocess
from features.tts import say

desktop_apps = {
    "notepad": "notepad.exe", # Works 
    "calculator": "calc.exe", # Works
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "vlc": "vlc.exe",
    "spotify": "spotify.exe",
    "visual studio code": "Code.exe",
    "microsoft teams": "Teams.exe",
    "microsoft paint": "mspaint.exe", # Works
    "microsoft word": "winword.exe",
    "microsoft excel": "excel.exe",
    "microsoft powerpoint": "powerpnt.exe",
    "command prompt": "cmd.exe",
    "terminal": "cmd.exe",
    "task manager": "taskmgr.exe", # Works
    "file explorer": "explorer.exe", # Works
    "settings": "ms-settings:app",
}

def open_app(command: str):
    if not command:
        print("Command is empty. Cannot open applications.")
        return
    command = command.lower().replace("open ", "")
    for keyword, app in desktop_apps.items():
        if keyword in command:
            try:
                subprocess.Popen(app)
                # say(f"Opening {keyword.capitalize()}...")
                print(f"Opening application: {keyword.capitalize()}...\n")
            except Exception as e:
                print(f"Failed to open {keyword}: {e}")
                # say(f"Failed to open {keyword}. Please check if it is installed or check path.")
            return
    


