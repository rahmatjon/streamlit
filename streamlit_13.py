import streamlit as st
import sqlite3
import hashlib

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Hash passwords for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user
def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users_1 (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists

# Authenticate user
def authenticate(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users_1 WHERE username = ?", (username,))
    stored_password = cursor.fetchone()
    conn.close()
    
    if stored_password and stored_password[0] == hash_password(password):
        return True
    return False

# Logout function
def logout():
    st.session_state.authenticated = False
    st.session_state.username = None
    # st.experimental_rerun()
    st.rerun()

# Initialize database
init_db()

# Session state initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Authentication flow
if not st.session_state.authenticated:
    st.title("🔐 Login / Register")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:  # Login tab
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"✅ Logged in as {username}")
                # st.experimental_rerun()
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    with tab2:  # Sign Up tab
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            if register_user(new_username, new_password):
                st.success("✅ Account created! You can now log in.")
            else:
                st.error("⚠️ Username already taken. Choose a different one.")

else:
    # User Dashboard
    st.sidebar.write(f"👤 Logged in as: **{st.session_state.username}**")
    st.sidebar.button("Logout", on_click=logout)

    st.title("🏠 User Dashboard")
    st.write("Welcome to the secure dashboard!")

    # Example: Show users in the database (admin feature)
    if st.session_state.username == "admin":
        st.subheader("🔧 Admin Panel")
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users_1")
        users = cursor.fetchall()
        conn.close()

        st.write("Registered Users:")
        for user in users:
            st.write(f"🆔 {user[0]} | 👤 {user[1]}")
