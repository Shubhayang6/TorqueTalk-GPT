import json
from pathlib import Path
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.docstore.document import Document

CHUNKS_PATH = "data/manual_chunks.json"
INDEX_DIR = "faiss_index"

def load_chunks(path: str):
    with open(path, 'r') as f:
        chunks = json.load(f)
        
    return chunks

def create_documents(chunks):
    return [Document(page_content=chunk, metadata = {"source":f"chunk_{i}"}) for i, chunk in enumerate(chunks)]

def build_faiss_index(docs, index_dir):
    print("🔄 Generating embeddings and building FAISS index...")
    embeddings = OllamaEmbeddings(model = "nomic-embed-text")
    vectorstore = FAISS.from_documents(docs,embeddings)
    vectorstore.save_local(index_dir)
    print(f"✅ FAISS index saved to '{index_dir}'")\
        
def main():
    chunks = load_chunks(CHUNKS_PATH)
    documents = create_documents(chunks)
    build_faiss_index(documents, INDEX_DIR)
    
if __name__ == "__main__":
    main()
    