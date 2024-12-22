import nltk 

#define corpus (corpus means sentances)

corpus= """ This is Nikhil Anil Warge. and I am learnign NLP. Also I am learnign Gen AI, I want to be a gerat man """
#print(corpus)

##  Tokinization Tokenization
## Tokinization is the process of splitting the text into the smaller units called tokens.which can be words phrase or even character
## Sentence-->paragraphs


from nltk.tokenize import sent_tokenize
#sent_tokenize  convert whole the paragraph in to  sentence i.e split all sentencies using fullstop
para=sent_tokenize(corpus)
#print(para)

#for sentence in para:
 #   print(sentence)

from nltk.tokenize import word_tokenize

#convert sentences in to words by identifing tab diff

word=word_tokenize(corpus)

#print(word)

#for words in word:
 #   print(words)

from nltk.tokenize import TreebankWordTokenizer

indiv_char=TreebankWordTokenizer()

#tokenize is the method present in treebanktokenize classg
new=indiv_char.tokenize(corpus)

print(new)
