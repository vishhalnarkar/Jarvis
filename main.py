# Importing the necessary modules from the features package
# features/gemini_api.py
from features import RequestGeminiAPI 
# features/tts.py
from features import say 
# features/stt.py
from features import listen 
# features/online.py
from features import open_website 
# features/online.py
from features import google_search
# features/desktop.py
from features import open_app
# features/desktop.py
from features import index_shortcuts, iterate_shortcuts
import os

# Testing the Code after updates
if __name__ == "__main__":
    # say(RequestGeminiAPI(listen()))
    # open_website("weather today")

    # start_menu = os.path.join(os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs")
    # start = os.path.join(os.environ['ProgramData'], "Microsoft", "Windows", "Start Menu", "Programs")
    output_csv = "features/shortcut_index.csv"
    # print(start_menu,"\n",start,"\n",output_csv)
    # index_shortcuts(start, output_csv)
    iterate_shortcuts(output_csv, "telegram")


