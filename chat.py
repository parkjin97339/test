install streamlit-chat 
from streamlit_chat import message 
import streamlit as st

st.header("Chat")

if "msg" not in st.session_state: 
 st.session_state.messages = [] 
 
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
  st.markdown(msg["content"])

if msg := st.chat_input("What is up?"): 
 st.chat_message("user").markdown(msg);
 st.session_state.messages.append({"role": "user", "content": msg}) ;

response = f"Echo: {prompt}"
