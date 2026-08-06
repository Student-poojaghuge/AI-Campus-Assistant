import streamlit as st

st.set_page_config(
    page_title="AI Campus Assistant",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 AI Campus Assistant")
st.subheader("Welcome to the Smart AI-Based College Assistant")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
### Features

- 🤖 AI Chatbot
- 📄 PDF Question Answering
- 📝 Notes Generator
- ❓ Quiz Generator
- 📚 PDF Summary
- 📢 Notice Search
- 👨‍🎓 Student Dashboard
- 👨‍💼 Admin Dashboard

---

### How It Works

1. Admin uploads college PDFs.
2. AI processes documents.
3. Students ask questions.
4. AI answers using uploaded documents.
""")

with col2:
    st.info("🎓 AI Campus Assistant")
    st.success("Reusable for any college")