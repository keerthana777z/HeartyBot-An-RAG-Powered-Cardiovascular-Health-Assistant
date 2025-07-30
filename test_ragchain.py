#!/usr/bin/env python3

import os
from ragchain import load_and_index_pdf, ask_question

def test_ragchain():
    print("Testing simplified ragchain...")
    
    # Check if we have any PDF files to test with
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found for testing")
        return False
    
    test_pdf = pdf_files[0]
    print(f"Testing with PDF: {test_pdf}")
    
    try:
        # Test loading and indexing
        print("Loading and indexing PDF...")
        db, retriever = load_and_index_pdf(test_pdf)
        print("✓ PDF loaded and indexed successfully")
        
        # Test asking a question
        print("Testing question answering...")
        question = "What is this document about?"
        answer, sources = ask_question(question, retriever)
        
        print(f"Question: {question}")
        print(f"Answer: {answer}")
        print(f"Sources: {sources}")
        print("✓ Question answering works")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_ragchain()
    if success:
        print("\n✓ All tests passed! The ragchain module is working.")
    else:
        print("\n✗ Tests failed.")
