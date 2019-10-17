import PyPDF2 
import os
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append("./pdfs/"+pdf)
    merger.write('./pdfs/super.pdf')
pdf_combiner(inputs)