# at command line use "pip install transformers"
# at command line use "pip install torch" (890.2 MB)
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, T5Config
device = torch.device('cpu')

def read_text_file(file_name):
    input_file_object = open(file_name, "r")
    text_as_single_line = input_file_object.readlines()
    #split input file into separate lines
    text_as_separate_sentences = text_as_single_line[0].split(". ")
    #a list to hold separate sentences
    sentences = []
    for sentence in text_as_separate_sentences:
        sentences.append(sentence)
    return sentences

# start here
# enter file name
file_name =  "Shark_Original.txt"
# read text and split into sentences
sentences =  read_text_file(file_name)

# Initialize the tokenizer model:
model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base', model_max_length=100)
# Supply tokenizer the sentences joined as single string
# no need to define or remove stop words
tokenized_text = tokenizer.encode("summarize: " + str(sentences), return_tensors='pt', max_length=512, truncation=True).to(device)
summary_ids = model.generate(tokenized_text, max_length=150, min_length=80, length_penalty=5., num_beams=2, early_stopping=True)
summary = tokenizer.decode(summary_ids[0])
# remove unwanted text added by tokenizer model
summary = summary.replace("<pad> ","")
summary = summary.replace("</s>","")
# display the summary
print("\nABSTRACT SUMMARIZED TEXT:\n")
print(summary)
print("\n")
# make the summary into a text file
with open('Shark_Abstract_Sum.txt', 'w') as output_object:
    output_object.write(summary)
