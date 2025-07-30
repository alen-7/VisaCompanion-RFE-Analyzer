from docx import Document
import fitz  # PyMuPDF
import os

def extract_text(file_path):
    """Extract text from PDF or DOCX files"""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return ""
    
    try:
        if file_path.lower().endswith('.pdf'):
            with fitz.open(file_path) as doc:
                return "\n".join([page.get_text() for page in doc])
                
        elif file_path.lower().endswith(('.docx', '.doc')):
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
            
        else:
            print(f"Unsupported file format: {file_path}")
            return ""
            
    except Exception as e:
        print(f"Error reading {file_path}: {str(e)}")
        return ""