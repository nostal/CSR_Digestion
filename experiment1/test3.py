from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
import nltk
import os
from gensim import corpora, models, similarities

path = r"C:\mallet\sample-data\web\en"
documents = os.listdir(path)
texts = []
for i in range(len(documents)):
    texts.append(open(path + r'\\' + documents[i]).read().lower())
pattern = r"[a-zA-Z]+"
tokenizer = RegexpTokenizer(pattern)
texts = [tokenizer.tokenize(text) for text in texts]

stopwords = nltk.corpus.stopwords.words('english')
wnl = nltk.WordNetLemmatizer()
texts = [[wnl.lemmatize(word) for word in document if word not in stopwords] for document in texts]
allWords = sum(texts, [])
tokens_once = [word for word in set(allWords) if allWords.count(word) == 1]
texts = [[word for word in document if word not in tokens_once] for document in texts]
dic = corpora.Dictionary(texts)
dic.save('corpus.dict')
corpus = [dic.doc2bow(document) for document in texts]
model = models.LdaModel(corpus, id2word= dic, num_topics=100)
a = model.show_topics(topics=10, topn=10, log=False, formatted=False)
print model[dic.doc2bow('It seems to me that topics with a probability less than some threshold \
 (I observed 0.01 to be more specific) are omitted form the output.'.split())]

