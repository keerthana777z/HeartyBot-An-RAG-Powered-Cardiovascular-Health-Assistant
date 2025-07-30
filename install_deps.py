#!/usr/bin/env python3

import subprocess
import sys

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install {package}: {e}")
        return False

def main():
    packages = [
        "langchain",
        "langchain-community", 
        "langchain-text-splitters",
        "sentence-transformers",
        "chromadb",
        "llama-cpp-python",
        "huggingface_hub",
        "pymupdf",
        "python-dotenv",
        "faiss-cpu",
        "streamlit"
    ]
    
    print("Installing required packages...")
    
    failed_packages = []
    for package in packages:
        if not install_package(package):
            failed_packages.append(package)
    
    if failed_packages:
        print(f"\nFailed to install: {', '.join(failed_packages)}")
        return False
    else:
        print("\n✓ All packages installed successfully!")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
