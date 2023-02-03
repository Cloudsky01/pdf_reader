
# importing required modules
from PyPDF2 import PdfReader
import pandas as pd
import csv
 
# creating a pdf reader object
reader = PdfReader('./pdf/Test.pdf')
 
# printing number of pages in pdf file
print(len(reader.pages))
 
# getting a specific page from the pdf file
page = reader.pages[0]
 
# extracting text from page
text = page.extract_text()

with open('test.txt', 'w') as f:
    f.write(text)

with open('test.txt', 'r') as f:
    stripped = (line.strip() for line in f)
    lines = (line.split(",") for line in stripped if line)
    with open('./csv/out.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
