# first need to import Nltk

import nltk
# Need to download  stopword

# Fromm corpus class import functinon stopwords

from nltk.corpus import stopwords
 
 #downloaded the Stopwords for the english
 
n=stopwords.words("english")
print(n)
#text processing using Lemmitization
# from nltk.stem import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize("going"))
