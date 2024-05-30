import streamlit as st
from streamlit_chat import message 

st.header("Chat")
msg = st.chat_input("")

if "messages" not in st.session_state: 
 st.session_state.messages = [] 
 
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]):
 st.markdown(msg["content"])
 
st.chat_message("user").markdown(msg)
st.session_state.messages.append({"role": "user", "content": prompt}) 


