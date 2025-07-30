from document_parser import extract_text
from analyzer import analyze_text
from report_generator import generate_report
import os
 

def analyze_text(text):
    risks = []
    text_lower = text.lower()
    
    # Example risk detection 
    if "world-class" in text_lower:
        weak_section = extract_weak_phrase(text, "world-class")
        fixed_version = rewrite_section(weak_section, "Generic Language")  
        risks.append((
            "Generic Language", 
            f"Subjective term: 'world-class'",
            "Medium",
            fixed_version  
        ))
    
    return risks

def extract_weak_phrase(text, phrase):
    """Extracts 50 characters around the weak phrase"""
    index = text.lower().find(phrase)
    return text[max(0,index-25):min(len(text),index+25)]

def rewrite_section(section, risk_type):
    """
    Returns a rewritten version of the section to address the risk.
    This is a placeholder implementation.
    """
    if risk_type == "Generic Language":
        return section.replace("world-class", "highly accomplished")
    return section

def main():
    print("\n=== VisaCompanion RFE Analyzer ===")
    
    # 1. Load document
    input_path = os.path.join("input", "sample_petition.docx")
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        return
    
    # 2. Process document
    print("Analyzing petition...")
    text = extract_text(input_path)
    risks = analyze_text(text)
    
    # 3. Generate report
    output_path = os.path.join("output", "risk_report.docx")
    generate_report(risks, output_path)
    print(f"Report generated at: {output_path}")

if __name__ == "__main__":
    main()