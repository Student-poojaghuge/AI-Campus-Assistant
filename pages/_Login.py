import streamlit as st

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success("Login feature coming tomorrow!")