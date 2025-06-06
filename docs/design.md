# 🧩 Software Design – TorqueTalk

## 📁 Folder Structure

---

torquetalk/
├── app/
│ ├── chat_ui.py
│ └── rag_pipeline.py
├── data/ 
├── models/
├── scripts/
│ ├── parse_obd_logs.py
│ ├── extract_faults.py
├── faiss_index/
├── requirements.txt
├── .env
├── .gitignore
└── README.md



---

## 🧠 Core Modules

### 1. `chat_ui.py`
- Renders chatbot in Streamlit
- Sends query to LangChain interface
- Displays answer from Ollama

### 2. `rag_pipeline.py`
- Loads vector DB (FAISS)
- Performs similarity search for relevant docs
- Constructs prompt with retrieved context
- Sends to Ollama and returns response

### 3. `parse_obd_logs.py`
- Accepts raw logs from diagnostic tools
- Extracts fault codes, timestamps, descriptions
- Converts to structured JSON for vector indexing

### 4. `extract_faults.py`
- Parses PDF/DOCX service manuals
- Extracts fault-related sections
- Stores text chunks and metadata

---

## 🔄 Data Flow

1. 🧾 User uploads an OBD log or asks a question
2. 🧠 LangChain RAG pipeline:
   - Vector search from FAISS using query embedding
   - Constructs a prompt with top-K relevant chunks
3. 🤖 Ollama responds using local LLaMA2
4. 💬 Response displayed in Streamlit chat interface

---

## 🛠 Technologies Used

| Component      | Technology        |
|----------------|-------------------|
| UI             | Streamlit         |
| Orchestration  | LangChain         |
| Vector DB      | FAISS             |
| LLM Runtime    | Ollama (LLaMA2)   |
| File Parsing   | PyMuPDF, `docx`, custom parsers |

---

_Last updated: 2025-06-06_
