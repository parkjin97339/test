import streamlit as st
import openai
import os
from openai import OpenAI

st.header("Chat")

if "msg" not in st.session_state: 
 st.session_state.messages = [] 
 
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
  st.markdown(msg["content"])

if msg := st.chat_input("What is up?"): 
 st.chat_message("user").markdown(msg);
 st.session_state.messages.append({"role": "user", "content": msg}) ;

client = OpenAI(api_key="sk-proj-ayiAG3gbanA8KDeThPGcT3BlbkFJJyE8PDgSiDiEkJvfHl4m")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "LangChain은 무엇을 하는 라이브러리지?"}
  ]
)

st.write(response.choices[0].message.content)
