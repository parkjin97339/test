import streamlit as st

st.header("Chat")
message1 = st.chat_input("")

if "messages" not in st.session_state: 
 st.session_state.messages = [] 

st.chat_message("user").markdown(prompt)

prompt1 = st.text_input(label="비밀번호를 입력하세요.", type="password", key="name")


