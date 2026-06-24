from google import genai
import os

# The script now looks for 'GEMINI_API_KEY' in your environment variables
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable not found.")
else:
    client = genai.Client(api_key=api_key)

    # List all models
    print("Fetching available models...")
    for model in client.models.list():
        print(f"Name: {model.name}, Display Name: {model.display_name}")