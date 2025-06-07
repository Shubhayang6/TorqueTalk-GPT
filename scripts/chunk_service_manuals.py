import fitz
import json
from pathlib import Path
import re

def clean_text(text: str) -> str:
    """
    Basic cleanup: Removes the extra whitespaces, headers, footers, etc.
    """
    
    return re.sub(r'\n\s*\n', '\n', text).strip()

def chunk_text(text: str, max_tokens: int = 500) -> list:
    """
    Splits the texts into chunks of the approximately max_tokens.
    This uses simple sentence or newline boundaries for splitting.
    """
    
    sentences = text.split('\n')
    chunks =[]
    current_chunk = []
    
    token_estimate = lambda x: len(x.split())
    
    for sentence in sentences:
        if token_estimate(' '.join(current_chunk + [sentence])) <= max_tokens:
            current_chunk.append(sentence)
        else:
            chunks.append('\n'.join(current_chunk).strip())
            current_chunk = [sentence]
            
    if current_chunk:
        chunks.append('\n'.join(current_chunk).strip())
        
    return chunks

def extract_chunks_from_pdf(pdf_path: str, output_path: str = "data/manual_chunks.json"):
    """
    Extracts readable text from a PDF and chunks it into smaller actions
    """
    doc = fitz.open(pdf_path)
    all_text = []
    
    for page in doc:
        text = page.get_text()
        if text:
            all_text.append(clean_text(text))
            
    full_text = '\n'.join(all_text)
    chunks = chunk_text(full_text)
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(chunks, f, indent=2)
        
    print(f"✅ Extracted {len(chunks)} chunks from {pdf_path} into {output_path}")
    

if __name__ == "__main__":
    extract_chunks_from_pdf("data/sample_manual.pdf")