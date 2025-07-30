import streamlit as st
import os
from pathlib import Path
from ragchain import load_and_index_pdf, ask_question  # <- your own module

st.set_page_config(page_title="Heart Health RAG", layout="wide")
st.title("💓 Ask Questions About Your Health PDFs")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Indexing your PDF..."):
        # Save uploaded PDF temporarily
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        # Load + index
        db, retriever = load_and_index_pdf(temp_path)

        st.success("✅ PDF indexed!")

        # --- Question Asking Section ---
        question = st.text_input("Ask a question about your document")

        if question:
            with st.spinner("Thinking..."):
                answer, sources = ask_question(question, retriever)
                st.markdown("### 🧠 Answer")
                st.write(answer)

                if sources:
                    st.markdown("### 🔗 Citations")
                    for s in sources:
                        st.write(f"→ {s}")

        # Clean up
        os.remove(temp_path)
