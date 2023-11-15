from goose3 import Goose
from PyPDF2 import PdfReader
import docx
my_goose = Goose()
def scrape_text(url):
    text=my_goose.extract(url)
    return text.cleaned_text

def scrape_pdf_text(inputfile):
    reader = PdfReader(str(inputfile))
    number_of_pages = len(reader.pages)
    strr=""
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        strr+=text
    return strr

def scrape_txt_file(inputfile):
    file = open(inputfile, "r")
    FileContent = file.read().strip()
    return str(FileContent)

def scrape_docx_file(inputfile):
    doc = docx.Document(inputfile)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)