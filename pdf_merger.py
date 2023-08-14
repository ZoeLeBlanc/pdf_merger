from PyPDF2 import PdfMerger
import os
import glob
import argparse
from rich.progress import track

def merge_files(dir_path, file_name):
    os.chdir(dir_path)
    files = glob.glob("./*")
    files.sort(key=os.path.getmtime)
    pdf_files = [os.fsdecode(file) for file in files if file.endswith('.pdf')]

    merger = PdfMerger()

    for pdf in track(pdf_files, description="Merging PDFs..."):
        merger.append(pdf)

    merger.write(file_name)
    merger.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge PDF files')
    parser.add_argument('-d', '--dir', help='Directory path', required=True)
    parser.add_argument('-f', '--file', help='File name', required=True)
    args = parser.parse_args()
    merge_files(args.dir, args.file)
