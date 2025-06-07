from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate

from langchain_community.llms import 


INDEX_DIR = "faiss_index"

CUSTOM_PROMPT = """You are an expert automotive diagnostic assistant.
Answer the question based on the following documentation and logs.

Context:
{context}

Question: {question}
Answer:"""

def load_vectorstore():
    embeddings = OllamaEmbeddings(model = "nomic-embed-text")
    return FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)

def get_rag_pipeline():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_type = "similarity", k=2)
    
    llm = Ollama(model = "mistral")
    
    prompt = PromptTemplate(
        input_variables = ["context", "question"],
        template = CUSTOM_PROMPT
    )
    
    rag_chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        chain_type = "stuff",
        return_source_documents = True,
        chain_type_kwargs = {"prompt": prompt}
        )
    
    return rag_chain

def ask_question(query: str) -> str:
    rag = get_rag_pipeline()
    result = rag({"query": query})
    return result["result"]