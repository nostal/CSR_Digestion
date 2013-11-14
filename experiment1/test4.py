from nltk.tokenize import RegexpTokenizer
stopwords = []
for line in open('stopwords.txt'):
    if line != '\n':
        stopwords.append(line.strip('\n'))

stopwords = set(stopwords)
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
stopwords = [tokenizer.tokenize(item)[0] for item in stopwords]
stopwords = sorted(stopwords)
a = open('stopwordslist.txt', 'w')
for item in stopwords:
    a.write(item + '\n')
a.close()