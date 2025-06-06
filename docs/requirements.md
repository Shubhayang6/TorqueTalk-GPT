# 📋 Project Requirements – TorqueTalk

## 🧠 Project Name
**TorqueTalk: Custom GPT for Automotive Fault Troubleshooting**

## 🚀 Objective
Build an offline AI assistant that helps mechanics, engineers, and enthusiasts understand OBD-II fault codes, root causes, and suggest repair actions using a locally hosted LLM and RAG pipeline.

---

## ✅ Functional Requirements

1. Accept and parse:
   - OBD-II fault logs (`.txt`, `.json`)
   - Fault code descriptions
   - Service manuals (`.pdf`, `.docx`)

2. Answer user queries such as:
   - "Why did fault P0302 occur?"
   - "How can I fix P0171?"

3. Perform similarity search over embedded documents using:
   - FAISS or other local vector DB

4. Use a local LLM (via Ollama) to respond in natural language

5. Provide a web-based chatbot UI using Streamlit

6. Include metadata in retrieval (e.g., affected subsystem, severity)

---

## 🚫 Non-Functional Requirements

- Entire system must work **completely offline** after setup
- Should run on:
  - Windows or Linux
  - 8–16 GB RAM (ideally 16 GB for smooth experience)
- Inference time: ≤ 5 seconds per query
- Modular codebase with clearly separated concerns
- CLI or Streamlit UI for demo

---

## 🎯 Stretch Goals (Optional)

- Voice input/output interface
- Upload and auto-parse OBD logs from mobile
- Offline Whisper integration for audio-to-text

---
<!-- YYYY-MM-DD -->
_Last updated: 2025-06-06_    
