from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = 'increase increases increased increasing'
stemmer = PorterStemmer() 
lemmatizer = WordNetLemmatizer()
for i in text.split(' '):
    print(stemmer.stem(i))
print('---')
for i in text.split(' '):
    print(lemmatizer.lemmatize(i))
