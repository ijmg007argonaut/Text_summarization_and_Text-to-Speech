import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pathlib import Path
from textblob import TextBlob
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import imageio
import numpy as np
from PIL import Image

# function to gernerate top 10 word counts
def text_top_word_finder(filename, stopwords=None):
    # for when stopwords are not needed
    if stopwords is None:
        stopwords=[]
    # read text
    blob = TextBlob(Path(filename).read_text())
    items = blob.word_counts.items()
    items = [item for item in items if item[0] not in stop_words]
    sorted_items = sorted(items, key=itemgetter(1), reverse=True)
    top10 = sorted_items[1:11]
    df = pd.DataFrame(top10, columns=['word', 'count'])
    print (df)
    axes = df.plot.bar(x='word', y='count', legend=False)
    plt.gcf().tight_layout()

# generate wordclouds
text1 = Path('Shark_Original.txt').read_text()
text2 = Path('Shark_Abstract_Sum.txt').read_text()
text3 = Path('Shark_Extract_Sum.txt').read_text()
wordcloud = WordCloud(width= 2500, height= 1500, max_font_size= 500, max_words= 100, colormap='prism', background_color='white')
wordcloud.generate(text1)
wordcloud.to_file('Shark_Original.png')
wordcloud.generate(text2)
wordcloud.to_file('Shark_Abstract.png')
wordcloud.generate(text3)
wordcloud.to_file('Shark_Extract.png')

# gernerate top 10 word counts
stop_words = stopwords.words('english')
print("\nORIGINAL TEXT TOP 10 WORDS:\n")
text_top_word_finder('Shark_Original.txt', stop_words)
print("\nABSTRACT SUMMARIZED TEXT TOP 10 WORDS:\n")
text_top_word_finder('Shark_Abstract_Sum.txt')
print("\nEXTRACT SUMMARIZED TEXT TOP 10 WORDS:\n")
text_top_word_finder('Shark_Extract_Sum.txt')
