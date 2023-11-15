from flask import Flask, render_template, request
from preprocess import preprocess_text,chunk_documents
from model import generate_summary,gen_sum
from scrape import scrape_text,scrape_pdf_text,scrape_txt_file,scrape_docx_file
import os

os.environ['CURL_CA_BUNDLE'] = ''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text-summarization', methods=["POST"])
def output():

    if request.method == "POST":
        option=request.form.get('options')
        if option=='url':
            inputurl=request.form['urlinput']
            inputtext=scrape_text(str(inputurl))
            original_text=preprocess_text(inputtext)
            chunks=chunk_documents(original_text)
            summary=gen_sum(chunks)
        elif option=='document':
            inputfile=request.form["fileinput"]
            print(inputfile)
            if inputfile.endswith('.pdf'):
                inputtext=scrape_pdf_text(inputfile)
                original_text=preprocess_text(inputtext)
                chunks=chunk_documents(original_text)
                summary=gen_sum(chunks)
                print(inputtext)
            elif inputfile.endswith('.docx'):
                inputtext=scrape_docx_file(inputfile)
                original_text=preprocess_text(inputtext)
                chunks=chunk_documents(original_text)
                summary=gen_sum(chunks)
                print(inputtext)
            else:
                inputtext=scrape_txt_file(inputfile)
                original_text=preprocess_text(inputtext)
                chunks=chunk_documents(original_text)
                summary=gen_sum(chunks)
                print(inputtext)
        else:
            inputtext = request.form["inputtext_"]
            original_text=preprocess_text(inputtext)
            summary=generate_summary(original_text)
    return render_template("output.html", data = {"input": original_text,"summary":summary})

if __name__ == '__main__': # It Allows You to Execute Code When the File Runs as a Script
    app.run(debug=True)

