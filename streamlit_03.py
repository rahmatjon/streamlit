import streamlit as st
import pandas as pd

st.title("Анализ данных по покупкам")

df = pd.read_csv('purchases.csv', sep = ';')

st.header("Статическая таблица")
st.table(df)

st.header("Интерактивная таблица")
st.dataframe(df)
