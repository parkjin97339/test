import streamlit as st
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

assistant = client.beta.assistants.create(
  instructions="당신은 부산 광안대교 전문가입니다. 첨부 파일의 정보를 이용해 응답하세요.",
  model="gpt-3.5-turbo",
  tools=[{"type": "file_search"}],
  tool_resources={
      "file_search":{
          "vector_store_ids": [vector_store.id]
      }
  }
)
assistant

response = f"Echo: {prompt}"
