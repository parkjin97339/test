import streamlit as st
from openai import OpenAI

st.header("비밀번호를 적어주세요.")
prompt1 = st.text_input(label="비밀번호를 입력하세요.", type="password", key="123")


if st.button("입력하기"):
  st.session_state.123
  client = OpenAI(api_key="prompt1")
  
if client == "sk-proj-JMjUVeuWPGFC6G0FIOzFT3BlbkFJVdIKAYD2bQZSehJxMcpZ":
  st.text_input("123")
  
st.divider()

st.header("무엇이든 물어보세요.")
prompt2 = st.text_input("질문")

if st.button("질문하기"):
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "prompt2"}
    ]
  )
  response
  print(response.choices[0].message.content)
