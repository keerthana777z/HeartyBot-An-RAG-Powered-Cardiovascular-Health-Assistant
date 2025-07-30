import os
from dotenv import load_dotenv
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from glob import glob

# Load HuggingFace token
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Load PDF and chunk it
#loader = PyMuPDFLoader("HealthyHeart.pdf")
#documents = loader.load()
#splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#chunks = splitter.split_documents(documents)


pdf_files = glob("*.pdf")  # loads all PDFs in folder
all_docs = []

for file in pdf_files:
    loader = PyMuPDFLoader(file)
    all_docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)



# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="NeuML/pubmedbert-base-embeddings"
)

# Create vector store
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_store"
)
vectordb.persist()

# Load LLM
llm = LlamaCpp(
    model_path="./BioMistral-7B.Q4_K_M.gguf",
    temperature=0.5,
    max_tokens=512,
    top_p=0.95,
    n_ctx=2048,
    verbose=True
)

# RAG pipeline
retriever = vectordb.as_retriever(search_type="similarity", k=3)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)


# Start interaction
print("Hi, I'm HeartyBot — your personal heart health assistant! ❤️")

while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        print("Byeeew! Stay heart-healthy. 💓")
        break

    result = rag_chain({"query": query})
    print("\nAnswer:", result["result"])

    # Display source citations with correct filenames and page numbers
    print("\nBased on:")
    seen = set()
    for doc in result["source_documents"]:
        metadata = doc.metadata
        source = os.path.basename(metadata.get("source", "Unknown file"))  # Extract filename only
        page = metadata.get("page", "Unknown page")
        citation = f"→ {source} → Page {page}"
        if citation not in seen:
            print(citation)
            seen.add(citation)
