from model import tokenizer
import nltk
nltk.download('punkt')
import re

def preprocess_text(text):
    # Use a regular expression to find and remove text within square brackets.
    cleaned_text = re.sub(r'\[.*?\]', '', text)

    return cleaned_text

def chunk_documents(FileContent):
    sentences = nltk.tokenize.sent_tokenize(FileContent)
    length = 0
    chunk = ""
    chunks = []
    count = -1
    for sentence in sentences:
        count += 1
        combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

        if combined_length  <= tokenizer.max_len_single_sentence: # if it doesn't exceed
            chunk += sentence + " " # add the sentence to the chunk
            length = combined_length # update the length counter

            # if it is the last sentence
            if count == len(sentences) - 1:
                chunks.append(chunk.strip()) # save the chunk
            
        else: 
            chunks.append(chunk.strip()) # save the chunk
            
            # reset 
            length = 0 
            chunk = ""

            # take care of the overflow sentence
            chunk += sentence + " "
            length = len(tokenizer.tokenize(sentence))
    return chunks
