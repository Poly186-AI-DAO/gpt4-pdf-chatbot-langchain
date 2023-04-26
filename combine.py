import pdfplumber
import os
from fpdf import FPDF

# Define the directory containing the PDF files
pdf_directory = r'C:\Users\eagle\OneDrive\Documents\Dev\gpt4-pdf-chatbot-langchain\docs'

# Create a PDF object for the output file
pdf_output = FPDF()
pdf_output.set_auto_page_break(auto=True, margin=15)

# Add the "DejaVu Sans" font to the PDF object
pdf_output.add_font("DejaVu", style="", fname="DejaVuSans.ttf")

# Set the font to "DejaVu Sans"
pdf_output.set_font("DejaVu", size=12)

# Iterate over all the files in the directory
for filename in os.listdir(pdf_directory):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Open the PDF file
        with pdfplumber.open(os.path.join(pdf_directory, filename)) as pdf:
            # Iterate over all the pages in the PDF file
            for page in pdf.pages:
                # Extract the text from the page
                text = page.extract_text()
                if text:
                    # Add a new page to the output PDF
                    pdf_output.add_page()
                    # Write the extracted text to the output PDF
                    pdf_output.multi_cell(0, 10, text)  

# Create the output file
output_filename = os.path.join(pdf_directory, 'combined_text.pdf')
pdf_output.output(output_filename)

print('Text from PDF files has been successfully extracted and combined into', output_filename)
