import streamlit as st
import time

if "status" not in st.session_state:
    st.session_state.status = "Idle"

st.write(f"Status: {st.session_state.status}")

if st.button("Start Task"):
    st.session_state.status = "Processing..."
    with st.spinner("Working..."):
        time.sleep(2)  # Simulate a long task
    st.session_state.status = "Completed"

st.write(f"Updated Status: {st.session_state.status}")
