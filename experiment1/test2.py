from __future__ import division
import string
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
text = open("1.txt").read().lower()
sents = sent_tokenize(text)
pattern = r'[a-z]+'
tokenizer = RegexpTokenizer(pattern)
print sents
print len(sents)
for i in range(len(sents)):
    sents[i] = tokenizer.tokenize(sents[i])
sents = filter(lambda sent: sent != [], sents)
print sents

