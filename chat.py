import streamlit as st

st.header("Chat")
msg = st.chat_input("")

if "messages" not in st.session_state: 
 st.session_state.messages = [] 
 
st.chat_message("user").markdown(msg)
st.session_state.messages.append({"role": "user", "content": msg}) 


