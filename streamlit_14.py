import streamlit as st
import sqlite3

# Database initialization
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# Insert a new user
def add_user(name, age, email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users_2 (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()
        st.success("✅ User added successfully!")
    except sqlite3.IntegrityError:
        st.error("⚠️ Email already exists! Choose a different one.")
    conn.close()

# Read all users
def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users_2")
    users = cursor.fetchall()
    conn.close()
    return users

# Update user details
def update_user(user_id, name, age, email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users_2 SET name=?, age=?, email=? WHERE id=?", (name, age, email, user_id))
    conn.commit()
    conn.close()
    st.success("✅ User updated successfully!")

# Delete a user
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users_2 WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    st.success("✅ User deleted successfully!")

# Initialize database
init_db()

# Streamlit UI
st.title("📝 User Management System (CRUD)")

# Tabs for different operations
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add User", "📋 View Users", "✏️ Update User", "❌ Delete User"])

# Add User
with tab1:
    st.subheader("➕ Add New User")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    email = st.text_input("Email")
    if st.button("Add User"):
        if name and email:
            add_user(name, age, email)
        else:
            st.error("⚠️ Name and Email are required!")

# View Users
with tab2:
    st.subheader("📋 All Users")
    users = get_users()
    if users:
        st.table(users)
    else:
        st.info("No users found.")

# Update User
with tab3:
    st.subheader("✏️ Update User")
    users = get_users()
    user_dict = {f"{u[1]} ({u[3]})": u[0] for u in users}  # Create a dropdown map
    selected_user = st.selectbox("Select User to Update", list(user_dict.keys()))
    
    if selected_user:
        user_id = user_dict[selected_user]
        new_name = st.text_input("New Name", value=selected_user.split(" (")[0])
        new_age = st.number_input("New Age", min_value=1, max_value=120, value=[u[2] for u in users if u[0] == user_id][0])
        new_email = st.text_input("New Email", value=[u[3] for u in users if u[0] == user_id][0])
        
        if st.button("Update User"):
            update_user(user_id, new_name, new_age, new_email)

# Delete User
with tab4:
    st.subheader("❌ Delete User")
    users = get_users()
    user_dict = {f"{u[1]} ({u[3]})": u[0] for u in users}
    selected_user = st.selectbox("Select User to Delete", list(user_dict.keys()))

    if selected_user:
        user_id = user_dict[selected_user]
        if st.button("Delete User"):
            delete_user(user_id)
            # st.experimental_rerun()
            st.rerun()

