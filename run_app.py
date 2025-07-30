#!/usr/bin/env python3

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    requirements = [
        "streamlit",
        "pymupdf",
        "python-dotenv"
    ]
    
    for req in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
            print(f"✓ Installed {req}")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install {req}")

def run_streamlit():
    """Run the Streamlit app"""
    try:
        # Install requirements first
        print("Installing requirements...")
        install_requirements()
        
        print("Starting Streamlit app...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except Exception as e:
        print(f"Error running app: {e}")

if __name__ == "__main__":
    run_streamlit()
