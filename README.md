# TorqueTalk-GPT
A fully offline AI assistant that takes in OBD-II logs and service manuals, and answers: “Why did this fault occur?” | “How to fix this P0xxx code?”


# 🔧 TorqueTalk – Custom GPT for Automotive Fault Troubleshooting

> **An offline, AI-powered assistant for automotive diagnostics.**  
> Built with LLaMA2, LangChain, FAISS & Streamlit. Runs fully offline via [Ollama](https://ollama.com).

---

## 🚗 Why TorqueTalk?

Modern vehicles generate thousands of diagnostic codes — but understanding the root cause or correct fix isn't always straightforward.  
**TorqueTalk** leverages domain-specific documents (OBD logs, fault descriptions, service manuals) and GenAI to answer:

- “🔍 Why did code P0300 occur?”
- “🛠 How do I fix P0171 on a diesel engine?”
- “📚 What does the service manual say for P0420?”

---

## 📦 Features

✅ Completely offline (no cloud calls)  
✅ Accepts OBD-II logs, PDF manuals, fault code data  
✅ Uses RAG (Retrieval-Augmented Generation) to enhance LLM output  
✅ Natural language Q&A with Streamlit chatbot  
✅ Powered by LangChain + Ollama + FAISS + LLaMA2

---

## 🧠 Architecture
[ Streamlit UI ]
↓
[ LangChain RAG Pipeline ]
↓
[ FAISS Vector DB + Ollama LLM ]

---

👉 See `docs/architecture.puml` for full system diagram.

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
git clone https://github.com/yourusername/torquetalk.git
cd torquetalk
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/macOS

pip install --upgrade pip
pip install -r requirements.txt
```
### 2. Install Ollama (LLM Backend)

Download: https://ollama.com/download

Run:

```bash
ollama run llama2
```
### 3. Start the App

```bash
streamlit run app/chat_ui.py
```

---

## 👨‍🔧 Maintainer
Shubhayan Ghosh
🔗 LinkedIn : [https://www.linkedin.com/in/ghoshshubhayan/]

📫 Email : shubhayan.tech@gmail.com

---

## 🪪 License
This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.

Model weights used (e.g., LLaMA2) are subject to their respective licenses, such as Meta’s [LLaMA license](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).
