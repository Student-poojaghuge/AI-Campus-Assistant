import streamlit as st
from utils.db_manager import create_tables

create_tables()

st.set_page_config(
    page_title="AI Campus Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Campus Assistant")

st.success("Database Connected Successfully ✅")