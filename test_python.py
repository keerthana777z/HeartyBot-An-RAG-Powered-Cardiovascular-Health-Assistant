print("Python is working!")
print("Testing imports...")

try:
    import fitz
    print("✓ PyMuPDF (fitz) is available")
except ImportError:
    print("✗ PyMuPDF (fitz) not available")

try:
    import streamlit
    print("✓ Streamlit is available")
except ImportError:
    print("✗ Streamlit not available")

print("Test completed!")
