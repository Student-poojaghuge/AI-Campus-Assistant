import streamlit as st

st.title("📝 Signup")

name = st.text_input("Full Name")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Create Account"):
    st.success("Signup feature coming tomorrow!")