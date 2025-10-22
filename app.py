import streamlit as st
from pathlib import Path
import main  # this is your backend file, e.g., backend.py

st.set_page_config(page_title="RAG PDF Summarizer", page_icon="📝")

st.title("📝 RAG PDF Summarizer")

st.sidebar.header("Upload & Query")
uploaded_file = st.sidebar.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
query = st.sidebar.text_input(
    "Enter your summarization query",
    value="Summarize this text, focusing on definitions and examples."
)
run_button = st.sidebar.button("Generate Summary")
# -----------------------------
# 1️⃣ File uploader
# -----------------------------
if uploaded_file and run_button:
    # Save file temporarily
    file_path = Path("temp_uploaded_file") / uploaded_file.name
    file_path.parent.mkdir(exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🧩 Generating summary..."):
        try:
            summary = main.generate_summary(file_path, query)
            st.subheader("🧠 Summary")
            st.write(summary.content)
        except Exception as e:
            st.error(f"❌ Error: {e}")

elif not uploaded_file:
    st.info("📌 Please upload a PDF or TXT file from the sidebar to generate summary.")