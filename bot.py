import streamlit as st
import pandas as pd


df = pd.read_excel(io='menu.xlsx', sheet_name='Menu')
df
