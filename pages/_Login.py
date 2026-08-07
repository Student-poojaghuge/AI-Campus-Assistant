import streamlit as st
from utils.auth_manager import login_user

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    success, result = login_user(email, password)

    if success:

        st.session_state["logged_in"] = True
        st.session_state["user"] = result

        st.success("Login Successful!")

    else:

        st.error(result)
        