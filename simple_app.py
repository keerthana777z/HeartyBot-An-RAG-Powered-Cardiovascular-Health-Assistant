import streamlit as st
import os

st.set_page_config(page_title="Heart Health RAG", layout="wide")
st.title("💓 Ask Questions About Your Health PDFs")

# Test if we can import our ragchain module
try:
    from ragchain import load_and_index_pdf, ask_question
    st.success("✅ RAG chain module loaded successfully!")
    
    # --- File Upload ---
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    
    if uploaded_file:
        with st.spinner("Indexing your PDF..."):
            # Save uploaded PDF temporarily
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())
            
            try:
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
                
            except Exception as e:
                st.error(f"Error processing PDF: {str(e)}")
            finally:
                # Clean up
                if os.path.exists(temp_path):
                    os.remove(temp_path)

except ImportError as e:
    st.error(f"❌ Failed to import ragchain module: {str(e)}")
    st.info("Please install the required dependencies:")
    st.code("pip install pymupdf streamlit")
    
    # Show available PDF files for testing
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    if pdf_files:
        st.info(f"Available PDF files in directory: {', '.join(pdf_files)}")
    else:
        st.warning("No PDF files found in the current directory.")

except Exception as e:
    st.error(f"❌ Unexpected error: {str(e)}")
    st.info("Please check your Python environment and dependencies.")
