import re
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Define a function to clean the text
def clean_text(text):
    # Remove irregular characters (non-printable ASCII characters)
    cleaned_text = re.sub(r'[^\x20-\x7E]+', ' ', text)
    return cleaned_text

# Load the PDF file
pdf_path = 'C:/Users/Shadow/Projects/AI Projects/gpt4-pdf-chatbot-langchain/docs/output.pdf'
pdf_document = fitz.open(pdf_path)

# Extract and clean the text from the PDF
cleaned_pdf_text = ''
for page in pdf_document:
    page_text = page.get_text()  # Use get_text instead of getText
    cleaned_page_text = clean_text(page_text)
    cleaned_pdf_text += cleaned_page_text

# Create a new PDF with the cleaned text
output_pdf_path = 'C:/Users/Shadow/Projects/AI Projects/gpt4-pdf-chatbot-langchain/docs/cleaned_output.pdf'
c = canvas.Canvas(output_pdf_path, pagesize=letter)
c.setFont("Helvetica", 12)
c.drawString(50, 750, cleaned_pdf_text)  # Adjust the position as needed
c.save()

print('Cleaned PDF created:', output_pdf_path)
