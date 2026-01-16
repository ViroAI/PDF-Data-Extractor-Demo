import pdfplumber
import pandas as pd

def extract_basic_data(pdf_path):
    
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        print("PDF Text Extracted Successfully!")
        return text

print("Tool initialized for data extraction...")
