import streamlit as st
import time

@st.cache_data
def expensive_computation(n):
    time.sleep(3)  # Simulating a long computation
    return n * 2

st.write("Result:", expensive_computation(5))
