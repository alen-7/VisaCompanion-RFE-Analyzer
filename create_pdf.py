import fitz  # PyMuPDF

# Create PDF with sample content
doc = fitz.open()
page = doc.new_page()

# Add EB-1A test content
text = """EB-1A TEST PETITION
Applicant: John Doe
Field: Artificial Intelligence

Original Contributions:
- Developed innovative algorithms (no patent numbers)

Publications:
- 3 conference papers (no journal citations)

Critical Role:
- Team lead at TechCorp (no org charts provided)"""

page.insert_text((50, 50), text)
doc.save("input/sample.pdf")
print("Created test PDF at: input/sample.pdf")