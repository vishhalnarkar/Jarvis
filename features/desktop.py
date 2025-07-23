# To Search, Join Path, etc. 
import os 
# To Open Applications
import subprocess
# To use Text-to-Speech
from features.tts import say
# To handle CSV files
import csv
# To resolve Windows shortcuts
import win32com.client


# To handle desktop applications
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

# To Open Desktop Applications
def open_app(command: str):
    if not command:
        print("Command is empty. Cannot open applications.")
        return
    command = command.lower().replace("open ", "")
    for keyword, app in desktop_apps.items():
        if keyword in command:
            try:
                subprocess.Popen(app)
                say(f"Opening {keyword.capitalize()}...")
                print(f"Opening application: {keyword.capitalize()}...\n")
            except Exception as e:
                print(f"Failed to open {keyword}: {e}")
                say(f"Failed to open {keyword}. Please check if it is installed or check path.")
            return
    
# Takes shortcut (.lnk) file path and returns the target path (.exe)
def resolve_shortcut(path_to_lnk: str) -> str:
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(path_to_lnk)
    return shortcut.TargetPath

# Cleans the CSV file
def remove_empty_rows(file_path):

    print("Cleaning File ...")
    cleaned_rows = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if all(cell.strip() == '' for cell in row):
                continue
            cleaned_rows.append(row)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_rows)

    print(f"Cleaned file saved: {file_path}")

def index_shortcuts(root_folder: str, output_csv: str):

    entries = []

    for dirpath, _, filenames in os.walk(root_folder):
        for fname in filenames:
            if not fname.lower().endswith(".lnk"):
                continue

            lnk_path = os.path.join(dirpath, fname)
            try:
                target = resolve_shortcut(lnk_path)
            except Exception as e:
                print(f"Warning: could not resolve {lnk_path}: {e}")
                continue

            exe_name = os.path.basename(target).strip()
            entries.append((exe_name, target))

    # write header + all found entries
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "path"])
        writer.writerows(entries)
    remove_empty_rows(output_csv)

    