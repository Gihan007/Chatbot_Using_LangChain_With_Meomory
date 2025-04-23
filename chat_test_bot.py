import os
from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables (make sure .env file has GOOGLE_API_KEY)
load_dotenv()

# Initialize the Google Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    convert_system_message_to_human=True
)

# Define prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the questions to the best of your ability."),
    MessagesPlaceholder(variable_name="message")
])

# Combine prompt and model into a chain
chain = prompt | model

# Setup Streamlit page
st.set_page_config(page_title="Memory Chatbot", page_icon="🤖")
st.title("🤖 Chat with Memory")

# Initialize chat history if not in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = InMemoryChatMessageHistory()

# Create the memory-aware chain
memory_model = RunnableWithMessageHistory(
    chain,
    lambda _: st.session_state.chat_history
)

# Input box for user
user_input = st.text_input("You:", placeholder="Type your message here...")

# Process user input
if user_input:
    response = memory_model.invoke(
        [HumanMessage(content=user_input)],
        config={"configurable": {"session_id": "streamlit_user"}}
    )
    # Display response
    st.markdown(f"**Bot:** {response.content}")

    # Optionally: show chat history
    with st.expander("🔍 Conversation History"):
        for msg in st.session_state.chat_history.messages:
            role = "You" if msg.type == "human" else "Bot"
            st.markdown(f"**{role}:** {msg.content}")
