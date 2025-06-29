🧠 PyBot: A ChatGPT-Powered Desktop Chatbot
PyBot is a sleek desktop chatbot built with Python and Tkinter, powered by OpenAI’s GPT API. It mimics natural conversation and offers intelligent, friendly responses through a simple yet elegant GUI.
screenshot-placeholder

✨ Features
- 🪄 Intuitive Tkinter-based GUI
- 🤖 GPT-3.5/4 powered responses via OpenAI API
- 💬 Multi-turn conversation with scrollable chat history
- ⚠️ Gracefully handles API issues and rate limits
- 🛠 Easy to extend with custom prompts or functionality


🚀 Getting Started
1. Clone the Repo
git clone https://github.com/yourusername/pybot-chatbot.git
cd pybot-chatbot


2. Set Up Environment
It's recommended to use a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


4. Add OpenAI API Key
Create a file named .env or a Python module config.py and add your API key:
Option A: Using a .env file
OPENAI_API_KEY=your_openai_api_key_here


Option B: Using a Python module
# config.py
OPENAI_API_KEY = "your_openai_api_key_here"



💻 Run the App
Simply launch the chatbot from terminal:
python main.py



📁 Project Structure
pybot-chatbot/
├── main.py             # Tkinter GUI logic and API integration
├── config.py           # API key (alternatively use .env)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation



🧩 Customization Ideas
- Change the assistant’s tone or personality in the system prompt
- Add voice input/output using speech_recognition and pyttsx3
- Save conversation history to a file or database
- Make an offline fallback with simple logic

📜 License
This project is released under the MIT License.
