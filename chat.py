import streamlit as st
import pandas as pd
from PIL import Image


st.image("https://www.pknu.ac.kr/imageView.do?target=campus&cd=B0000024")
def main(): 
  df = pd.read_excel('test1.xlsx')
  st.dataframe(df)
  st.table(df)
  st.table(df())
  st.write(df())
  st.text(df())

main()

st.header("무엇이든 물어보세요.")
prompt = st.text_input("질문?")

