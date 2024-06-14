import streamlit as st
from PIL import Image
import pandas as pd

st.image("https://www.pknu.ac.kr/imageView.do?target=campus&cd=B0000024")

df = pd.read_excel('https://github.com/toracle/python-basic-lecture/raw/master/assets/%EC%97%91%EC%85%80%EA%B3%BC%EC%A0%95%EC%8B%A4%EC%8A%B5%EC%83%9D.xlsx', sheet_name='Sheet1')
df

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

