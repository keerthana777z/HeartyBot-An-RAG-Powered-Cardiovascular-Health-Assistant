# ❤️ HeartyBot: An RAG-Powered Cardiovascular Health Assistant

**HeartyBot** is an intelligent AI assistant built to assist in **cardiovascular health queries** using both **medical PDFs** and **advanced biomedical language models**. It leverages **Retrieval-Augmented Generation (RAG)** to provide **citation-backed, page-specific responses** — using **BioMistral-7B**, **PubMedBERT**, and **LangChain** over **ChromaDB**.

---

## 🚀 Features

-  **PDF Upload**: Upload one or multiple medical PDFs (e.g., WHO reports, clinical guidelines).
-  **Bio-Aware LLM Responses**: Uses **BioMistral-7B** fine-tuned for biomedical knowledge.
-  **Citation & Page Tracking**: Answers are linked with the page numbers and document names.
-  **Domain-specific Embeddings**: Generated via **PubMedBERT** for enhanced medical accuracy.
-  **LangChain RAG Pipeline**: Structured document QA via chunking, embedding, retrieval, and generation.
-  **Future Scope - ECG Analysis**: Extendable for ECG CSV data for arrhythmia classification.
- 🖥 **Streamlit Interface**: Simple and responsive UI for users to chat with HeartyBot.

---

## 🧪 Components Overview

| **Component**         | **Tool/Model**                  |
|-----------------------|---------------------------------|
| LLM                   | BioMistral-7B                   |
| Embedding Model       | PubMedBERT                      |
| Embedding Store       | ChromaDB                        |
| Pipeline Framework    | LangChain                       |
| Chunking              | LangChain's Text Splitter       |
| PDF Parser            | PyMuPDF / LangChain PDF Loader  |
| UI                    | Streamlit                       |

---

## 🖼️ Example Output

**Question**: *What are the main behavioral risk factors for cardiovascular diseases globally?*

**Answer**:  
The main behavioral risk factors mentioned for cardiovascular diseases globally are cigarette smoking, high blood pressure, high blood cholesterol, overweight, physical inactivity, and diabetes. These can be prevented by eating a healthy diet, exercising regularly, not smoking, and managing existing health conditions.

**Based on**:  
→ *World-Heart-Vision-2030.pdf* → Page 13  
→ *healthyheart.pdf* → Page 8

---

## 💡 Future Scope: ECG Classification

HeartyBot can be extended into a hybrid health assistant that:

-  Accepts ECG data files (`.csv`, `.json`)
-  Uses ML/DL to classify conditions like Atrial Fibrillation, Tachycardia, Bradycardia, etc.
-  Cross-references structured signal data with unstructured knowledge (e.g., PDF guidelines)
-  Potential to evolve into a **smart diagnostic assistant**

---

## 🧑‍💻 Tech Stack

- **Python 3.10+**
- [LangChain](https://www.langchain.com/)
- [BioMistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)

---

## Author
AR Keerthana

