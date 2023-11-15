import torch
from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "facebook/bart-large-cnn"

# Load model and tokenizer
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer1 = BartTokenizer.from_pretrained(model_name)


def generate_summary(text):

    text_to_summarize = text
    # Encode text to summarize
    inputs = tokenizer1(text_to_summarize, return_tensors="pt")

    # Generate summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=512, early_stopping=True)
    summary = tokenizer1.batch_decode(summary_ids, skip_special_tokens=True)[0]

    return summary



from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "sshleifer/distilbart-cnn-12-6"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
def gen_sum(chunks):
    # inputs to the model
    strr=""
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]
    for input in inputs:
        output = model.generate(**input)
        strr+=tokenizer.decode(*output, skip_special_tokens=True)
    return strr
