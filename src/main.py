
# importing required modules
from PyPDF2 import PdfReader
import pandas as pd
import csv
import os
 
def write_to_txt(text, path):
    with open(path, 'w') as f:
        f.write(text)

def modify_txt(path):
    with open(path) as f:
        for line in f:
            if ':' in line:
                line = line.replace(':', ',')
                
                

def openPDF(path):
    # creating a pdf reader object
    reader = PdfReader(path)
    
    # printing number of pages in pdf file
    print(len(reader.pages))
    
    # getting a specific page from the pdf file
    page = reader.pages[0]
    
    # extracting text from page
    text = page.extract_text()
    formatted_txt_path = path.replace('pdf', 'txt')
    write_to_txt(text, formatted_txt_path)
    modify_txt(formatted_txt_path)



# Function that iterate through the pdf directory
def iterate_through_dir():
    directory = 'pdf'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        print("Opening file: {}".format(f))
        openPDF(f)

if __name__ == '__main__':
    iterate_through_dir()

# with open('test.txt', 'r') as f:
#     stripped = (line.strip() for line in f)
#     lines = (line.split(",") for line in stripped if line)
#     with open('./csv/out.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)
