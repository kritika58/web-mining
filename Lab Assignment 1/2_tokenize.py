from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
from bs4 import BeautifulSoup

url = "https://python.org"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,"lxml")
for script in soup(["script", "style"]):
    script.extract()    # rip it out

text = soup.get_text()
tokens = word_tokenize(text)

text_2 = []
stopwords_total = 0

stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
for i in tokens:
    if i in stop_words:
        stopwords_total+=1
    else:
        text_2.append(i)
print(text_2)

