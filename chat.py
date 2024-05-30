import streamlit as st

st.header("Chat")
message1 = st.chat_input("")

if "messages" not in st.session_state: 
 st.session_state.messages = [] 
 
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
 st.markdown(msg["content"])
 
st.chat_message("user").markdown(message1)

prompt1 = st.text_input(label="비밀번호를 입력하세요.", type="password", key="name")


