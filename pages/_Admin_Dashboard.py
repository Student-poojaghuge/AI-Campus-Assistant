import streamlit as st
import os
from utils.file_manager import save_pdf

st.title("👨‍💼 Admin Dashboard")

st.subheader("Upload College PDF")

uploaded_file = st.file_uploader(
    "Choose PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    path = save_pdf(uploaded_file)

    st.success("PDF Uploaded Successfully!")

    st.write(path)

# -------------------------------
# Show Uploaded PDFs
# -------------------------------

st.divider()

st.subheader("Uploaded PDFs")

files = os.listdir("uploads")

if files:

    for file in files:

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write("📄", file)

        with col2:

            if st.button("Delete", key=file):

                os.remove(f"uploads/{file}")

                st.success("Deleted Successfully!")

                st.rerun()

else:

    st.info("No PDFs uploaded yet.")