import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0  # Initialize session variable

if st.button("Increase Counter"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

name = st.text_input("Enter your name:", key="username")
st.write("Hello", st.session_state.username)
