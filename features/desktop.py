# TODO: GO through the code specially open_app and iterate_shortcuts, integrate them, to tired and confused to do it now.

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
def open_app(path: str):
    if not path:
        print("path is empty. Cannot open applications.")
        return
    try:
        subprocess.Popen(path)
        say(f"Opening {os.path.basename(path)}...")
        print(f"Opening : {os.path.basename(path)}...\n")
    except Exception as e:
        print(f"Failed to open {path}: {e}")
        say(f"Failed to open {os.path.basename(path)}.")
    return
    
# Takes shortcut (.lnk) file path and returns the target path (.exe)
def resolve_shortcut(path_to_lnk: str) -> str:
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(path_to_lnk)
    path = shortcut.TargetPath.lower()
    if path.endswith(".exe") and "install" not in path and "uninstall" not in path and "unins" not in path:
        print(f"Resolved shortcut: {path}")
        return path
    return None

def index_shortcuts(root_folder: str, output_csv: str)  -> None:
    
    seen = set()
    if os.path.exists(output_csv) and os.path.getsize(output_csv) > 0:
        with open(output_csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                seen.add(row["path"].lower())

    new_entries = []
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

            if not target or target in seen:
                continue

            exe_name = fname[:-4] + ".exe"
            new_entries.append((exe_name, target))

    if not new_entries:
        print("No new shortcuts to index.")
        return

    write_header = not os.path.exists(output_csv) or os.path.getsize(output_csv) == 0
    with open(output_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["filename", "path"])
        writer.writerows(new_entries)

    print(f"Appended {len(new_entries)} new shortcuts to '{output_csv}'.")

def iterate_shortcuts(file: str, word: str):
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["filename"].lower() == (word + ".exe").lower():
                print(f"Found: {row["filename"]} at {row["path"]}")
                say(f"Found {word}")
                open_app(row["path"])
                return
            