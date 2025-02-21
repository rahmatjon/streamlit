import streamlit as st
import pandas as pd

df = pd.read_csv('purchases.csv', sep = ';')
st.title("Анализ данных по покупкам")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.header("Статическая таблица")
    st.table(df)
with tab2:
    st.header("Интерактивная таблица")
    st.dataframe(df)
