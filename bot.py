import streamlit as st
import pandas as pd


df = pd.read_excel(url='https://github.com/parkjin97339/test/blob/main/menu.xlsx', sheet_name='Menu')
df
