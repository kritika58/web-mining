from nltk.tokenize import sent_tokenize, word_tokenize

stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
text = "Hello Adam, how are you? I hope everything is going well.  Today is a good day, see you dude."
f_text = []
tokens = word_tokenize(text)
for i in tokens:
    if i in stop_words:
        print("Found!")
    else:
        f_text.append(i)

answer = ''

for i in f_text:
    answer+=i + ' '

print(answer)