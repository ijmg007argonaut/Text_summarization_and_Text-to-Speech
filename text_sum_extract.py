from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy
import networkx
import urllib.request
from bs4 import BeautifulSoup

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

def make_comparison_table(sentences, stop_words):
    # Create zero filled comparison table
    comparison_table = numpy.zeros((len(sentences), len(sentences)))
    for column in range(len(sentences)):
        for row in range(len(sentences)):
            #don't compare a sentence to itself
            if column == row:
                continue
            comparison_table[column][row] = sentence_comparer(sentences[column], sentences[row], stop_words)
    return comparison_table

def sentence_comparer(sentence1, sentence2, stopwords=None):
    if stopwords is None:
        stopwords = []
    sentence1 = [w.lower() for w in sentence1]
    sentence2 = [w.lower() for w in sentence2]
    # make a list from both sentences being compared
    all_words = list(set(sentence1 + sentence2))
    # an empty vector to hold each sentence
    vector1 = numpy.zeros( len(all_words) )
    vector2 = numpy.zeros( len(all_words) )
    # build the vector for the first sentence
    for w in sentence1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    # build the vector for the second sentence
    for w in sentence2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    """
    Use cosine similarity (aka cosine_distance) to compare vector representing first sentence
    to vector representing second sentence. Cosine similarity is a measure of similarity between
    two non-zero vectors of an inner product space that measures the cosine of the angle between them.
    """
    return 1 - cosine_distance(vector1, vector2)



# start here
# enter file name
file_name =  "Shark_Original.txt"
# enter number of lines in desired summary
# limit to 5 for reasonable comparison between abstracy and extract methods
top_N_ranked_sentences = 5
# get commonly known stop words
stop_words = stopwords.words('english')
# read text and split into sentences
sentences =  read_text_file(file_name)

# make a comparison table to compare sentences
sentence_similarity_martix = make_comparison_table(sentences, stop_words)

# rank sentences in comparison table
sentence_similarity = networkx.from_numpy_array(sentence_similarity_martix)
sentence_scores = networkx.pagerank(sentence_similarity)

# join and print top ranked sentences into proposed summary
ranked_sentence = sorted(((sentence_scores[index],score) for index,score in enumerate(sentences)), reverse=True)
# create list that will hold summarized text
summarize_text = []
for i in range(top_N_ranked_sentences):
  summarize_text.append("".join(str(ranked_sentence[i][1])))
# display the summary after preprocessing and conversion to a string
summary = str(summarize_text)
summary = summary.replace("', '", ". ")
summary = summary.replace("['", "")
summary = summary.replace("']", ".")
print("\nEXTRACT SUMMARIZED TEXT:\n")
print(summary)
print("\n")
# make the summary into a text file
with open('Shark_Extract_Sum.txt', 'w') as output_object:
    output_object.write(summary)
