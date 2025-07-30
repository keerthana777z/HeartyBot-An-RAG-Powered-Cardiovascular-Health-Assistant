# ❤️ HeartyBot: An RAG-Powered Cardiovascular Health Assistant

HeartyBot is an AI-powered assistant designed to answer questions related to cardiovascular health using your uploaded PDF documents. It uses **Retrieval-Augmented Generation (RAG)** with **LangChain**, **LLMs**, and **Chroma vector stores** to generate accurate, citation-backed responses — and tells you *exactly* which page and document each answer came from. 📄🔍

---

## 🚀 Features

-  **Document Upload**: Users can upload one or more PDFs related to cardiovascular health.
-  **Context-Aware Question Answering**: Ask questions, and HeartyBot will generate medically relevant answers using the uploaded documents.
-  **Citation + Page Number Highlighting**: Every response shows which document and page it was derived from.
-  **Streamlit UI**: Clean, user-friendly interface for uploading PDFs, asking questions, and viewing results.
- 🧾 **ECG Diagnosis (Future Scope)**: You can extend this to accept ECG signals and provide diagnoses like arrhythmia detection and condition classification.

---

## 🖼️ Example Output

**Question**: *What are the main behavioral risk factors for cardiovascular diseases globally?*

**Answer**:  
The main behavioral risk factors mentioned for cardiovascular diseases globally are cigarette smoking, high blood pressure, high blood cholesterol, overweight, physical inactivity, and diabetes. These can be prevented by eating a healthy diet, exercising regularly, not smoking, and managing existing health conditions.

**Based on**:  
→ World-Heart-Vision-2030.pdf → Page 13  
→ healthyheart.pdf → Page 8

---

## 🧑‍💻 Tech Stack

- **Python 3.10+**
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI GPT-3.5 or GPT-4](https://platform.openai.com/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [Streamlit](https://streamlit.io/) for the UI

---

🧠 Future Scope: ECG Data Classification
This project can be extended to support ECG data uploads (e.g., .csv, .json) and use machine learning or deep learning models to:

Detect abnormal heart rhythms (Arrhythmias)

Classify conditions like : Atrial Fibrillation, Tachycardia, etc.

Combine structured ECG data with unstructured medical knowledge from PDFs

Imagine a single bot that understands both your test results and your reports — and gives medically grounded insights. That's the future of HeartyBot.
