import streamlit as st

st.title("Interactive Streamlit App")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 48)

if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")
    st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
    )
    st.html(
    "<table border='1'><tr><td>Раҳматҷон</td></tr></table>"
    )    