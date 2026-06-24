import time
import os
import geocoder
import psutil
from google import genai
from google.genai import types
from gtts import gTTS
from playsound3 import playsound

# 1. Setup API Client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

client = genai.Client(api_key=api_key)

# 2. Tools & Context
def get_system_status():
    """Returns the current CPU usage and battery percentage."""
    cpu = psutil.cpu_percent(interval=1)
    battery = psutil.sensors_battery()
    bat_str = f"{battery.percent}%" if battery else "Plugged in/No battery"
    return f"CPU Usage: {cpu}%, Battery: {bat_str}"

try:
    g = geocoder.ip('me')
    location_context = f"The user is currently located in {g.city}, {g.state}, {g.country}."
except:
    location_context = "Location could not be determined."

# 3. Configuration
config = types.GenerateContentConfig(
    system_instruction=f"You are a helpful assistant. {location_context} You have access to a tool 'get_system_status'.",
    tools=[get_system_status]
)

def speak(text):
    """Converts text to speech and plays it."""
    try:
        tts = gTTS(text=text, lang='en')
        filename = "response.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Speech error: {e}")

def start_chatbot():
    print("Chatbot active. Type 'quit' to exit.")
    chat = client.chats.create(model="gemini-3.1-flash-lite", config=config)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit': break
        
        # Retry logic loop
        for attempt in range(3):
            try:
                response = chat.send_message(user_input)
                
                # Handle Tool Calls
                while response.function_calls:
                    for call in response.function_calls:
                        if call.name == "get_system_status":
                            result = get_system_status()
                            response = chat.send_message(
                                types.Part.from_function_response(
                                    name="get_system_status",
                                    id=call.id,
                                    response={"result": result}
                                )
                            )
                
                print(f"Chatbot: {response.text}")
                speak(response.text)
                break 
                
            except Exception as e:
                if "503" in str(e) and attempt < 2:
                    print("Server busy, retrying...")
                    time.sleep(2)
                else:
                    print(f"An error occurred: {e}")
                    break

if __name__ == "__main__":
    start_chatbot()