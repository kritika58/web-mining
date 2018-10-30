# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:38:47 2018

@author: Kritika Mishra
"""
import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize




url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)






#example_sent = news_soup.text
#stop_words = set(stopwords.words('english'))
#word_tokens = word_tokenize(example_sent)
#filtered_sentence = []
#for w in word_tokens:
#    if w not in stop_words:
#        filtered_sentence.append(w)
#print("TOKENISED PAGE\n\n\n\n\n")
#print(word_tokens)
#print("\n\n\n\\nFILTERED PAGE\n\n\n\n\n")
#print(filtered_sentence)