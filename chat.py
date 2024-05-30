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

openai.api_key="sk-proj-ayiAG3gbanA8KDeThPGcT3BlbkFJJyE8PDgSiDiEkJvfHl4m")

user_input = st.text_input("user:", "")
openai.Completion.create
