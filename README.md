# PDF Merger Script

Very quick little utility for merging pdfs since Mac borked its PDF automator action with its removal of Python https://discussions.apple.com/thread/253764288 😅

I imagine there are thousands of these but figured I would still share mine. Full disclosure, some of this was written using ChatGPT so I imagine I'm "copying" someone else's code unintentionally - if you see something that looks like yours, let me know and I'll credit you!

Finally, you can always avoid the command line and use a GUI like https://www.sejda.com/merge-pdf or https://www.adobe.com/acrobat/online/merge-pdf.html 

## Usage

```bash
python3 pdf_merger.py -i <input_dir> -o <output_dir>
```

input_dir: Directory containing PDFs to merge
output_dir: Directory to output merged PDFs

### Example Usage

```bash
python3 pdf_merger.py -i "../example_data/pdf_files" -o "../example_data/merged_pdfs/merged.pdf"
``` 

The example is *Data Feminism* by Catherine D'Ignazio and Lauren F. Klein, which is a great read if you're interested in data science and social justice. The book is available open access from MIT Press Direct https://direct.mit.edu/books/oa-monograph/4660/Data-Feminism. There is a full book download option for this one, but that is rarely the case I've found for many e-books.

## Requirements

- Python 3.6+
- PyPDF2
- rich

## Installation

```bash
pip3 install -r requirements.txt
```
