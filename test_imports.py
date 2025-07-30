#!/usr/bin/env python3

print("Testing imports...")

try:
    from langchain_community.document_loaders import PyPDFLoader
    print("✓ PyPDFLoader imported successfully")
except ImportError as e:
    print(f"✗ PyPDFLoader import failed: {e}")

try:
    from langchain_text_splitters import CharacterTextSplitter
    print("✓ CharacterTextSplitter imported successfully")
except ImportError as e:
    print(f"✗ CharacterTextSplitter import failed: {e}")

try:
    from langchain_community.vectorstores import FAISS
    print("✓ FAISS imported successfully")
except ImportError as e:
    print(f"✗ FAISS import failed: {e}")

try:
    from langchain_community.embeddings import HuggingFaceEmbeddings
    print("✓ HuggingFaceEmbeddings imported successfully")
except ImportError as e:
    print(f"✗ HuggingFaceEmbeddings import failed: {e}")

try:
    from langchain.chains import RetrievalQA
    print("✓ RetrievalQA imported successfully")
except ImportError as e:
    print(f"✗ RetrievalQA import failed: {e}")

try:
    from langchain_community.chat_models import ChatOpenAI
    print("✓ ChatOpenAI imported successfully")
except ImportError as e:
    print(f"✗ ChatOpenAI import failed: {e}")

print("Import test completed!")
