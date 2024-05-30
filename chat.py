import streamlit as st

st.header("Chat")
msg = st.chat_input("")

if "msg" not in st.session_state: 
 st.session_state.messages = [] 
 
st.chat_message("user").markdown(msg)
st.session_state.messages.append({"role": "user", "content": msg}) 

for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
 st.markdown(msg["content"])
