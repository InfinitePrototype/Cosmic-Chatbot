\# 🌌 Cosmic Agent



> An intelligent desktop AI assistant capable of conversation, document analysis, system monitoring, and voice interaction through a futuristic space-themed command center.



\---


## 🚀 Live Demo

🌐 https://cosmic-chatbot-de9rqjaxebritytjxi7wcn.streamlit.app/


\## 🚀 Overview



Cosmic Agent is a desktop AI assistant built using Google's Gemini models and Python.



The goal of the project was to move beyond a traditional chatbot and create an AI agent that can actively interact with the user's local environment.



Instead of simply generating text, Cosmic Agent can:



\- Access real-time system information

\- Read and analyze local PDF documents

\- Speak responses aloud

\- Maintain conversational context

\- Execute tool calls when external information is required



The project combines modern Large Language Models with traditional software engineering techniques to create an assistant that is both intelligent and practical.



\---



\# 🎯 Motivation



Most AI chatbots operate inside a closed environment.



They can answer questions, but they cannot interact with your computer or access live information unless explicitly programmed to do so.



Cosmic Agent was developed to explore the concept of AI Tool Calling, where a language model can intelligently decide when it needs external information and automatically invoke Python functions to retrieve it.



This transforms the chatbot from a simple conversational model into an AI-powered assistant capable of performing useful tasks.



\---



\# ✨ Core Features



\## 🤖 Conversational AI



Powered by Google's Gemini 3.1 Flash Lite model.



Capabilities include:



\- Natural language conversations

\- Context-aware responses

\- Multi-turn dialogue

\- Tool-assisted reasoning



\---



\## 🖥️ System Monitoring



Cosmic Agent can retrieve live information directly from the operating system.



\### Supported Metrics



\- CPU Usage

\- Battery Percentage

\- Power Status



Example:



```text

User:

How much CPU is my computer currently using?



Assistant:

Your CPU usage is currently 12%.

```



\---



\## 📄 PDF Document Analysis



The assistant can read local PDF files and answer questions about them.



Supported actions:



\- Extract text

\- Generate summaries

\- Explain technical concepts

\- Answer document-specific questions

\- Create concise notes



Example:



```text

Read the file:



C:\\Research\\AI\_Paper.pdf



and summarize the main findings.

```



\---



\## 🔊 Voice Output



Every AI response can be converted into speech.



Implemented using:



\- gTTS

\- playsound3



Benefits:



\- Hands-free interaction

\- Accessibility support

\- More natural user experience



\---



\## 🌠 Cosmic User Interface



The Streamlit dashboard was designed around a futuristic space theme.



\### Visual Features



\- Animated Solar System

\- Dynamic Orbital Motion

\- Glowing Star Effects

\- Glassmorphism Chat Windows

\- Dark-Space Color Palette



The interface was intentionally designed to make the assistant feel like a futuristic command center rather than a traditional chatbot.



\---



\## ⚡ Intelligent Tool Calling



One of the most important features of the project.



Instead of guessing system information, the AI can:



1\. Detect when a tool is required.

2\. Call a Python function.

3\. Retrieve real data.

4\. Continue the conversation using the tool result.



Example Flow:



```text

User:

What is my battery percentage?



Gemini:

Calls get\_system\_status()



Python:

Returns battery data



Gemini:

Uses returned information to generate answer

```



This dramatically improves reliability compared to standard chatbot responses.



\---



\# 🏗️ System Architecture



```text

┌────────────────────────────┐

│         User Input         │

└─────────────┬──────────────┘

&#x20;             │

&#x20;             ▼

┌────────────────────────────┐

│      Gemini 3.1 Flash      │

└─────────────┬──────────────┘

&#x20;             │

&#x20;             ▼

┌────────────────────────────┐

│ Function Call Detection    │

└─────────────┬──────────────┘

&#x20;             │

&#x20;     ┌───────┴────────┐

&#x20;     │                │

&#x20;     ▼                ▼



System Tool       PDF Tool

(psutil)          (PyPDF2)



&#x20;     │                │

&#x20;     └───────┬────────┘

&#x20;             │

&#x20;             ▼



&#x20;     Tool Response



&#x20;             │

&#x20;             ▼



&#x20;     Gemini Response



&#x20;             │

&#x20;             ▼



&#x20;      Voice Output

```



\---



\# 🧩 Technology Stack



| Component | Technology |

|------------|------------|

| AI Model | Gemini 3.1 Flash Lite |

| Programming Language | Python |

| Frontend | Streamlit |

| System Monitoring | psutil |

| PDF Processing | PyPDF2 |

| Text-to-Speech | gTTS |

| Audio Playback | playsound3 |

| Geolocation | geocoder |

| AI SDK | Google GenAI |



\---



\# 📂 Project Structure



```text

Cosmic-Agent/

│

├── app.py

├── chatbot.py

├── main.py

├── model\_test.py

├── icon.png

├── Project\_log.txt

├── requirements.txt

└── README.md

```



\### app.py



Main Streamlit dashboard implementation.



Contains:



\- UI Rendering

\- Session Management

\- Tool Execution Engine

\- Gemini Integration

\- Voice Response System



\---



\### chatbot.py



Terminal-based implementation of Cosmic Agent.



Features:



\- Gemini Integration

\- Location Context

\- System Monitoring

\- Voice Output



\---



\### main.py



Advanced terminal version with:



\- PDF Reading

\- Tool Calling

\- Voice Interaction

\- Retry Logic



\---



\### model\_test.py



Utility used to enumerate available Gemini models.



Useful for testing and development.



\---



\### Project\_log.txt



Detailed development journal documenting:



\- Engineering challenges

\- Design decisions

\- Tool-calling implementation

\- Streamlit architecture

\- Bug fixes



\---



\# ⚙️ Installation



\## Clone Repository



```bash

git clone https://github.com/YOUR\_USERNAME/Cosmic-Agent.git



cd Cosmic-Agent

```



\## Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Configure API Key



\### Windows



```powershell

setx GEMINI\_API\_KEY "YOUR\_API\_KEY"

```



\### Linux / macOS



```bash

export GEMINI\_API\_KEY="YOUR\_API\_KEY"

```



\---



\# ▶️ Running Cosmic Agent



\### Streamlit Dashboard



```bash

streamlit run app.py

```



\---



\### Terminal Version



```bash

python chatbot.py

```



or



```bash

python main.py

```



\---



\# 💡 Example Queries



\### System Monitoring



```text

What is my CPU usage?

```



```text

How much battery do I have remaining?

```



\### PDF Analysis



```text

Read C:\\Books\\Physics.pdf

```



```text

Summarize the uploaded research paper.

```



```text

Explain chapter 5 in simple terms.

```



\### General Conversation



```text

What are the latest advancements in AI?

```



\---



\# 🔬 Technical Challenges



\## Tool Synchronization



The largest challenge was ensuring that Gemini correctly executed Python tools and incorporated the returned results into its responses.



This was solved through a manual function execution loop that continuously processes tool calls until the model generates a final response.



\---



\## Streamlit Session Persistence



Because Streamlit reruns the application after every interaction, chat history was repeatedly lost.



Session State was used to preserve:



\- Chat Memory

\- Gemini Session

\- Tool Configuration



\---



\## Fault-Tolerant System Monitoring



Some desktop systems do not provide battery information.



Defensive programming was added to prevent crashes when battery sensors return null values.



\---



\## PDF Path Compatibility



Windows users frequently copy paths containing quotation marks.



Input sanitation was implemented to ensure file paths are correctly interpreted before processing.



\---



\# 🔮 Future Roadmap



\### Planned Features



\- 🌐 Internet Search Integration

\- 🧠 Long-Term Memory

\- 📁 Drag-and-Drop Document Uploads

\- 📸 Image Understanding

\- 🎥 Video Analysis

\- 📊 System Analytics Dashboard

\- ☁️ Cloud Deployment

\- 📱 Mobile Application

\- 🎙️ Real-Time Voice Assistant

\- 🤖 Autonomous Multi-Agent Workflows



\---



\# 📜 License



Released under the MIT License.



\---



\# ⭐ Final Thoughts



Cosmic Agent demonstrates how Large Language Models can be combined with traditional software tools to create assistants that do more than generate text.



By integrating system access, document analysis, voice interaction, and intelligent tool calling, the project explores the next step toward practical AI-powered desktop agents.



> "Navigate information. Understand documents. Explore your digital universe."

