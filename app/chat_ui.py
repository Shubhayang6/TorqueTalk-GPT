import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.rag_pipeline import ask_question

st.set_page_config(page_title="TorqueTalk - GPT", page_icon = "🚗", layout = "centered")

st.title("🔧 TorqueTalk – Automotive Fault Chatbot")
st.markdown("Ask me anything about OBD-II fault codes, service issues or repair suggestions.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
query = st.chat_input("Ask me a question like 'What is P0171?'")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": "query"})
    
    with st.spinner("Thinking..."):
        response = ask_question(query)
        
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role":"assistant", "content": response})
