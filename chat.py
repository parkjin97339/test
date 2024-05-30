import streamlit as st

st.header("Chat")
messages = st.chat_input("")

if "messages" not in st.session_state: 
 st.session_state.messages = [msg] 
 
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
 st.markdown(msg["content"])
 
st.chat_message("user").markdown(messages)
st.session_state.messages.append({"role": "user", "content": prompt}) 


