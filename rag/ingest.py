import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

RAW_DOCS_DIR = "RAW_DOCS_DIR"
CHROMA_DIR = "chroma_db"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

def ingest_documents():
    loader = DirectoryLoader(RAW_DOCS_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
    raw_docs = loader.load()
    print(f"Loaded {len(raw_docs)} pages from source documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = splitter.split_documents(raw_docs)
    print(f"Split into {len(chunks)} chunks")

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )
    print(f"ChromaDB persisted to {CHROMA_DIR}")
    return vectorstore

if __name__ == "__main__":
    ingest_documents()
