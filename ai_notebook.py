import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Notebook",
    layout="wide"
)

NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)

st.title("📄 AI Notebook")

# Sidebar
st.sidebar.header("Documents")

files = sorted(NOTES_DIR.glob("*.txt"))

file_names = [f.stem for f in files]

selected_file = st.sidebar.selectbox(
    "Open Document",
    ["New Document"] + file_names
)

if selected_file == "New Document":
    document_name = st.sidebar.text_input(
        "Document Name",
        "Untitled"
    )
    content = ""
else:
    document_name = selected_file

    with open(NOTES_DIR / f"{selected_file}.txt", "r") as f:
        content = f.read()

# Main editor
text = st.text_area(
    "",
    value=content,
    height=600,
    label_visibility="collapsed"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("💾 Save"):
        with open(
            NOTES_DIR / f"{document_name}.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(text)

        st.success("Document saved!")

with col2:
    st.download_button(
        "⬇ Download",
        text,
        file_name=f"{document_name}.txt"
    )