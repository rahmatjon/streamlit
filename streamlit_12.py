import streamlit as st
import time

# Simulated user database
USER_CREDENTIALS = {
    "user1": "password123",
    "admin": "adminpass"
}

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = None


# Function to authenticate user
def authenticate(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    return False


# Function to log out
def logout():
    st.session_state.authenticated = False
    st.session_state.username = None
    st.experimental_rerun()


# Login form (only shown if not authenticated)
if not st.session_state.authenticated:
    st.title("🔒 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        with st.spinner("Authenticating..."):
            time.sleep(1)  # Simulate delay
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"✅ Welcome, {username}!")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password. Try again.")

else:
    st.sidebar.write(f"👤 Logged in as: **{st.session_state.username}**")
    st.sidebar.button("Logout", on_click=logout)

    st.title("🏠 Dashboard")
    st.write("Welcome to the secure area of the app!")

    # Example of showing admin-only content
    if st.session_state.username == "admin":
        st.subheader("🔧 Admin Panel")
        st.write("This is a restricted section for administrators.")

    # Regular user content
    st.subheader("📊 User Content")
    st.write("This content is visible to all logged-in users.")

