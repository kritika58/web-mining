from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize

def create_index (data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
        for token in tokens:
            index[token].append(i)
    print(index)

stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
with open('sample.txt', 'r') as myfile:
    text=myfile.read().replace('\n', '')
myfile.close()
f_text = []
tokens = word_tokenize(text)
for i in tokens:
    if i in stop_words:
        continue
    else:
        f_text.append(i)
answer = ''
for i in f_text:
    answer+=i + ' '
#print(answer)  
li = list(answer.split(" "))
print(li)
print("BREAK BREAK BREAK \n\n\n")
with open('sample1.txt', 'r') as myfile:
    text1=myfile.read().replace('\n', '')
#print(text1)
f_text1 = []
tokens1 = word_tokenize(text1)
for i in tokens1:
    if i in stop_words:
        continue
    else:
        f_text1.append(i)
answer1 = ''
for i in f_text1:
    answer1+=i + ' '
#print(answer)  
li1 = list(answer1.split(" "))
print(li1)
f_list=[li,li1]
create_index(f_list)

