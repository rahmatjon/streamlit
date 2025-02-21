import streamlit as st
import sqlite3

@st.cache_resource
def get_db_connection():
    return sqlite3.connect("database.db")

conn = get_db_connection()
st.write("Connected to DB!")
