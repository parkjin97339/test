import streamlit as st
import openai
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

assistant = client.assistants.create(
  name="똑똑한 비서",
  description="당신은 똑똑한 비서입니다.",
  model="gpt-3.5-turbo"
)
assistant

thread = client.threads.create(
  messages=[
    {
      "role": "user",
      "content": msg
    }
  ]
)

response = f"Echo: {prompt}"
