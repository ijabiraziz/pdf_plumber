import pdfplumber

# Open the PDF file
with pdfplumber.open('test.pdf') as pdf:
    # Iterate over each page in the PDF
    for page in pdf.pages:
        # Extract the text from the page
        text = page.extract_text()
       
        # Print the extracted text
        print(text)
        