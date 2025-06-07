import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.rag_pipeline import ask_question

query = "What does the P0171 fault mean and how to fix it?"
response = ask_question(query)

print("\n💡 GPT Response:\n", response)  