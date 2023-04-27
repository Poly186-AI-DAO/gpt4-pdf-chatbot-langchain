import re
import fitz  # PyMuPDF
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Define a function to clean the text
def clean_text(text):
    # Remove irregular characters (non-printable ASCII characters)
    cleaned_text = re.sub(r'[^\x20-\x7E]+', ' ', text)
    return cleaned_text

# Load the PDF file
pdf_path = 'C:\\Users\\eagle\\OneDrive\\Documents\\Dev\\gpt4-pdf-chatbot-langchain\\docs\\combined_text.pdf'
pdf_document = fitz.open(pdf_path)

# Create the output directory if it doesn't already exist
output_dir = 'C:/Users/eagle/OneDrive/Documents/Dev/gpt4-pdf-chatbot-langchain/docs/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Extract and clean the text from the PDF, and split into multiple PDF files
max_pages_per_file = 1000
file_count = 0
page_count = 0
line_count = 0
c = None
for page in pdf_document:
    if page_count == 0:
        # Start a new PDF file
        file_count += 1
        output_pdf_path = os.path.join(output_dir, f'cleaned_output_{file_count}.pdf')
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        print(f'Starting new PDF file: {output_pdf_path}')
        line_count = 0

    # Extract and clean text from the current page
    page_text = page.get_text()
    cleaned_page_text = clean_text(page_text)

    # Split the cleaned text into lines
    lines = cleaned_page_text.split('\n')

    # Add the cleaned text to the current PDF file
    for line in lines:
        c.drawString(50, 750 - (line_count * 14), line)  # Adjust the position as needed
        line_count += 1
        if line_count >= 50:  # Approximately 50 lines per page
            c.showPage()  # Start a new page
            line_count = 0

    page_count += 1
    if page_count == max_pages_per_file:
        # Save the current PDF file and reset the page count
        c.save()
        print(f'Finished PDF file: {output_pdf_path}')
        page_count = 0

# Save the last PDF file if it has content
if page_count > 0:
    c.save()
    print(f'Finished PDF file: {output_pdf_path}')

print('Cleaned PDF files created.')
