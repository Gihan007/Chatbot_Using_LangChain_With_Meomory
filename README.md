## To run this project just run "streamlit run chat_test_bot.py"  in your terminal
markdown
Copy
Edit
# 🤖 Chatbot with Memory using Streamlit, LangChain, and Gemini

This is a memory-enabled chatbot built with **Streamlit**, **LangChain**, and **Google Gemini API**. The chatbot remembers the context of the conversation within a session using in-memory chat history. 

---

## 🚀 Features

- 💬 Chat with natural conversation flow
- 🧠 Memory support: Remembers what you said earlier in the session
- 🌐 Powered by **Google Gemini (gemini-2.0-flash)**
- 🛠️ Built with **LangChain** and **Streamlit**
- ⚙️ Easily extendable to support long-term memory or storage
- 👨‍💻 Real-time display of chat history

---

## 🧠 Why Memory?

In real-world chatbot applications, **memory** is crucial for:
- Tracking user preferences or names during the session
- Maintaining context in multi-turn conversations
- Avoiding repetitive questions and responses
- Enabling more human-like, intelligent conversations

We use **LangChain's `RunnableWithMessageHistory`** combined with `InMemoryChatMessageHistory` to implement memory.

---

## 📁 Project Structure

weatherchatbot_using_DialogFlow_And_AWS_CI-CD/ │ ├── chat_test_bot.py # Main Streamlit chatbot file ├── .env # Environment variables (API Key) └── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Requirements

- Python 3.9+
- `streamlit`
- `langchain`
- `langchain-google-genai`
- `python-dotenv`

Install using:

```bash
pip install -r requirements.txt
🔑 Environment Setup
Create a .env file with your Google API key:

env
Copy
Edit
GOOGLE_API_KEY=your_actual_google_api_key
🧪 Run Locally
bash
Copy
Edit
streamlit run chat_test_bot.py
Then open the provided localhost URL in your browser.

🧬 Technologies Used

Tool	Purpose
Streamlit	UI and interaction
LangChain	Chaining logic and memory support
Gemini API (Google)	LLM responses
dotenv	Environment management
📌 Extending the Bot
You can upgrade this bot with:

🔄 Persistent memory using Redis or a database

🎤 Voice input/output

🌍 Web scraping abilities

📦 CI/CD pipeline (e.g., GitHub Actions + AWS)

💡 Inspiration
This project is part of a larger Weather Chatbot integrated with DialogFlow and CI/CD pipelines using AWS. This module focuses on adding natural chat capabilities and context retention using modern LLM techniques.

🧑‍💻 Author
Bope Ranasinghe Gihan Lakmal
University of Kelaniya – BSc in Computer Science (AI Specialization)
📞 0769919877
📍 Colombo 08
🖥️ GitHub: [your-link]

📜 License
MIT License. Use freely and responsibly.
