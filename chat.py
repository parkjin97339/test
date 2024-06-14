import streamlit as st
from PIL import Image

st.image("https://www.pknu.ac.kr/imageView.do?target=campus&cd=B0000024")

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

