import pdfplumber

import pandas as pd

import os



def extract_basic_data(pdf_path):

    full_text = ""



    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                full_text += page_text + "\n"



    return full_text





print("Tool initialized for data extraction...")



# Folder where main.py is located

current_folder = os.path.dirname(os.path.abspath(__file__))



data = []



# Loop through all files in the folder

for file_name in os.listdir(current_folder):

    if file_name.lower().endswith(".pdf"):

        pdf_path = os.path.join(current_folder, file_name)

        print(f"Extracting data from: {file_name}")



        text = extract_basic_data(pdf_path)



        data.append({

            "PDF File": file_name,

            "Extracted Text": text

        })



# Create Excel file

df = pd.DataFrame(data)

df.to_excel("pdf_extracted_data.xlsx", index=False)



print("Extraction completed! File 'pdf_extracted_data.xlsx' created successfully.")

