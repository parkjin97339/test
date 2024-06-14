import streamlit as st
from PIL import Image
pip install xlrd
pip install openpyxl
pip install pandas
import pandas as pd

st.image("https://www.pknu.ac.kr/imageView.do?target=campus&cd=B0000024")

file_name = 'test1.xlsx'
df = pd.read_excel(file_name)
print(df)

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

