import streamlit as st
from openai import OpenAI

st.header("비밀번호를 적어주세요.")
prompt1 = st.text_input(label="비밀번호를 입력하세요.", type="password", key="API")
st.session_state.key

if st.button("입력하기"):
  client = OpenAI(api_key="{prompt1}")
