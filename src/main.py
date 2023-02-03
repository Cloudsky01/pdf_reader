
# importing required modules
from PyPDF2 import PdfReader
import pandas as pd
import csv
import os
 
def iterate_over_text(text):
    list = text.split('\n')
    dict = {}
    for i in list:
        if ':' in i:
            sub = i.split(':')
            dict[sub[0]] = sub[1]
    return dict

def create_excel(list):
    df = pd.DataFrame(list)
    df.to_excel('output.xlsx')
                

def openPDF(path):
    # creating a pdf reader object
    reader = PdfReader(path)
    
    # printing number of pages in pdf file
    print(len(reader.pages))
    
    # getting a specific page from the pdf file
    page = reader.pages[0]
    
    # extracting text from page
    text = page.extract_text()
    return iterate_over_text(text)
    



# Function that iterate through the pdf directory
def main_sub_routine():
    directory = 'pdf'
    finalList = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        print("Opening file: {}".format(f))
        finalList.append(openPDF(f))
    create_excel(finalList)

if __name__ == '__main__':
    main_sub_routine()

# with open('test.txt', 'r') as f:
#     stripped = (line.strip() for line in f)
#     lines = (line.split(",") for line in stripped if line)
#     with open('./csv/out.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)
