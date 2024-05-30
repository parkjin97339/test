import streamlit as st
import openai
import os
from openai import OpenAI

st.header("Chat")

if msg := st.chat_input("What is up?"): 
 st.chat_message("user").markdown(msg);
 st.session_state.messages.append({"role": "user", "content": msg}) ;
 
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
  st.markdown(msg["content"])

response = msg

with st.chat_message("assistant"): 
 st.markdown(response) 

st.session_state.messages.append({"role": "assistant", "content": response})

