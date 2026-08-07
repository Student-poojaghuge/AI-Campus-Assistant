import streamlit as st
from utils.auth_manager import register_user

st.title("📝 Signup")

name = st.text_input("Full Name")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Create Account"):

    if name == "" or email == "" or password == "":
        st.warning("Please fill all fields.")

    else:

        success, message = register_user(
            name,
            email,
            password
        )

        if success:
            st.success(message)

        else:
            st.error(message)