# To load environment variables from .env file
import os
from dotenv import load_dotenv

# For Gemini API
from google import genai 

# Lazy initialization of the Gemini client
client = None

# Inilialize the Gemini client
def init_gemini_client():

    # Ensure you have a .env file with GEMINI_API_KEY and optionally GEMINI_API_URL
    print("Loading Environment Variables from .env file...")

    # Check if .env file exists
    if not os.path.exists('.env'):
        raise FileNotFoundError("The .env file is missing. Please create one with the required variables.")

    # Load environment variables
    load_dotenv()
    GEMINI_API = os.getenv("GEMINI_API_KEY")
    GEMINI_API_URL = os.getenv("GEMINI_API_URL", "https://generativelanguage.googleapis.com")

    # Validate that the GEMINI_API_KEY is set
    if not GEMINI_API:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    
    # Set API Key
    print("Environment Variables Loaded Successfully.")
    client = genai.Client(api_key=GEMINI_API)
    print("Initialized Gemini Client...\n")
    
    return client

# Function to request Gemini API and handle & return the response
def RequestGeminiAPI(prompt):

    global client
    #Initialize the first time & only when needed
    if client is None:
        client = init_gemini_client()  

    # Validate that the prompt is not empty
    if not prompt:
        raise ValueError("Prompt is empty. Cannot send an empty request to the Gemini API.")
    print(f"Sending Request to Gemini API with prompt: {prompt}\n")
    
    # Send request to Gemini API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    # Print the response
    print("Sent Request to Gemini API:\nResponse:")
    print(response.text)
    # Validate that the response is not empty
    if not response.text:   
        raise ValueError("No text response received from the Gemini API.")
    
    return response.text