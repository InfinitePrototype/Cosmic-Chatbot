import time
import os
import geocoder
import psutil
import PyPDF2
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

# 2. Tools
def get_system_status():
    """Returns the current CPU usage and battery percentage."""
    cpu = psutil.cpu_percent(interval=1)
    battery = psutil.sensors_battery()
    bat_str = f"{battery.percent}%" if battery else "Plugged in/No battery"
    return f"CPU Usage: {cpu}%, Battery: {bat_str}"

def read_pdf(file_path: str):
    """Reads the text content of a PDF file from a local path."""
    try:
        if not os.path.exists(file_path):
            return "File not found."
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = "\n".join([page.extract_text() for page in reader.pages])
            return text[:4000] # Limit size for the model
    except Exception as e:
        return f"Error reading PDF: {e}"

# Map functions so the SDK can find them
tools_map = {
    "get_system_status": get_system_status,
    "read_pdf": read_pdf
}

# 3. Configuration
config = types.GenerateContentConfig(
    system_instruction="You are a helpful assistant. You have tools to check system status and read local PDFs.",
    tools=[get_system_status, read_pdf]
)

def speak(text):
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
        
        for attempt in range(3):
            try:
                response = chat.send_message(user_input)
                
                # Manual loop to handle automatic execution of tools
                while response.function_calls:
                    for call in response.function_calls:
                        tool_func = tools_map.get(call.name)
                        if tool_func:
                            # Execute the tool and send result back
                            tool_result = tool_func(**call.args)
                            response = chat.send_message(
                                types.Part.from_function_response(
                                    name=call.name,
                                    id=call.id,
                                    response={"result": tool_result}
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