import streamlit as st
import os
import psutil
import PyPDF2
from google import genai
from google.genai import types
from gtts import gTTS
from playsound3 import playsound

# 1. Page Config
st.set_page_config(page_title="Cosmic Agent", page_icon="icon.png", layout="wide")

# 2. Interactive Space CSS
st.markdown("""
    <style>
    .stApp { background: #000; color: white; }
    .solar-system { position: fixed; top: 50%; left: 50%; width: 100vw; height: 100vh; transform: translate(-50%, -50%); pointer-events: none; z-index: 0; }
    .sun { position: absolute; top: 50%; left: 50%; width: 100px; height: 100px; background: radial-gradient(circle, #FFD700, #FF4500); border-radius: 50%; transform: translate(-50%, -50%); box-shadow: 0 0 60px #FF8C00; }
    .planet { position: absolute; top: 50%; left: 50%; border: 1px solid rgba(255,255,255,0.1); border-radius: 50%; animation: rotate linear infinite; }
    @keyframes rotate { from { transform: translate(-50%, -50%) rotate(0deg); } to { transform: translate(-50%, -50%) rotate(360deg); } }
    .main { z-index: 1; }
    .stChatMessage { background: rgba(255, 255, 255, 0.1) !important; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); }
    </style>
    <div class="solar-system">
        <div class="sun"></div>
        <div class="planet" style="width: 250px; height: 250px; animation-duration: 20s;"></div>
        <div class="planet" style="width: 450px; height: 450px; animation-duration: 40s;"></div>
    </div>
    """, unsafe_allow_html=True)

# 3. Tool Logic
def get_system_status():
    """Returns the current system stats, ensuring no 'None' results."""
    cpu = psutil.cpu_percent(interval=1)
    battery = psutil.sensors_battery()
    bat_str = f"{battery.percent}%" if battery else "Not detected (Desktop/Plugged in)"
    return f"CPU Usage: {cpu}%, Battery Status: {bat_str}"

def read_pdf(file_path: str):
    """Reads the text content of a PDF file."""
    try:
        # Strip quotes if user included them in path
        clean_path = file_path.strip('"').strip("'")
        if not os.path.exists(clean_path): return "File not found."
        with open(clean_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join([page.extract_text() for page in reader.pages])[:4000]
    except Exception as e: return f"Error reading PDF: {e}"

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
    except Exception as e: st.error(f"Speech error: {e}")

# 4. Session Setup
if "chat" not in st.session_state:
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful space-themed assistant. Always provide concrete system data when asked.",
        tools=[get_system_status, read_pdf]
    )
    st.session_state.chat = client.chats.create(model="gemini-3.1-flash-lite", config=config)

# 5. UI
with st.sidebar:
    if os.path.exists("icon.png"): st.image("icon.png", width=120)
    st.title("Cosmic Agent")
    if st.button("Clear History"): st.session_state.chat = None; st.rerun()

st.title("✨ Cosmic Command Center")

for message in st.session_state.chat.get_history():
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role): st.markdown(message.parts[0].text)

if prompt := st.chat_input("Ask about your system or a PDF file..."):
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.status("Navigating the galaxy...", expanded=True):
            response = st.session_state.chat.send_message(prompt)
            while response.function_calls:
                for call in response.function_calls:
                    func = {"get_system_status": get_system_status, "read_pdf": read_pdf}.get(call.name)
                    result = func(**call.args)
                    response = st.session_state.chat.send_message(
                        types.Part.from_function_response(name=call.name, id=call.id, response={"result": result})
                    )
        st.markdown(response.text)
        speak(response.text)