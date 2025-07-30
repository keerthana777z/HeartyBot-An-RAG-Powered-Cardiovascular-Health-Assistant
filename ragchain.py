import fitz  # PyMuPDF
import re
from typing import List, Tuple

class SimpleRetriever:
    def __init__(self, text_chunks: List[str], pdf_path: str):
        self.text_chunks = text_chunks
        self.pdf_path = pdf_path

    def get_relevant_documents(self, query: str) -> List[dict]:
        """Simple keyword-based retrieval"""
        query_words = set(query.lower().split())
        relevant_chunks = []

        for i, chunk in enumerate(self.text_chunks):
            chunk_words = set(chunk.lower().split())
            # Simple overlap scoring
            overlap = len(query_words.intersection(chunk_words))
            if overlap > 0:
                relevant_chunks.append({
                    'content': chunk,
                    'score': overlap,
                    'metadata': {'source': self.pdf_path, 'chunk_id': i}
                })

        # Sort by relevance score and return top 3
        relevant_chunks.sort(key=lambda x: x['score'], reverse=True)
        return relevant_chunks[:3]

def load_and_index_pdf(pdf_path: str) -> Tuple[None, SimpleRetriever]:
    """Load PDF and create simple text-based retriever"""
    try:
        # Open PDF with PyMuPDF
        doc = fitz.open(pdf_path)
        text_chunks = []

        # Extract text from each page
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()

            # Simple text chunking (split by paragraphs)
            paragraphs = text.split('\n\n')
            for para in paragraphs:
                para = para.strip()
                if len(para) > 50:  # Only keep substantial paragraphs
                    text_chunks.append(para)

        doc.close()

        if not text_chunks:
            raise ValueError("No text content found in PDF")

        retriever = SimpleRetriever(text_chunks, pdf_path)
        return None, retriever  # Return None for db to match expected interface

    except Exception as e:
        raise RuntimeError(f"Failed to load PDF: {str(e)}")

def ask_question(question: str, retriever: SimpleRetriever) -> Tuple[str, List[str]]:
    """Simple question answering using keyword matching"""
    try:
        relevant_docs = retriever.get_relevant_documents(question)

        if not relevant_docs:
            return "I couldn't find relevant information in the document to answer your question.", []

        # Simple answer generation - just return the most relevant chunk
        best_chunk = relevant_docs[0]['content']

        # Create a simple answer by taking the first few sentences
        sentences = re.split(r'[.!?]+', best_chunk)
        answer_sentences = []

        for sentence in sentences[:3]:  # Take first 3 sentences
            sentence = sentence.strip()
            if len(sentence) > 20:  # Only substantial sentences
                answer_sentences.append(sentence)

        if not answer_sentences:
            answer = best_chunk[:300] + "..." if len(best_chunk) > 300 else best_chunk
        else:
            answer = '. '.join(answer_sentences) + '.'

        # Extract sources
        sources = [doc['metadata']['source'] for doc in relevant_docs]
        unique_sources = list(set(sources))  # Remove duplicates

        return answer, unique_sources

    except Exception as e:
        return f"Error processing question: {str(e)}", []
