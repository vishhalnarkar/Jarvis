# To load environment variables from .env file
import os
from dotenv import load_dotenv
# For Gemini API
from google import genai 

# Loaded and Stored Environment Variables
# Ensure you have a .env file with GEMINI_API_KEY and optionally GEMINI_API_URL
load_dotenv()
GEMINI_API = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL", "https://generativelanguage.googleapis.com")
if not GEMINI_API:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain the concept of AI in a single sentence.",
)

print("Sent Request to Gemini API:\n")
print(response)
