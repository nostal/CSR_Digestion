import layout
from nltk.tokenize import sent_tokenize
pages = layout.get_pages('Coffee Bean International.pdf')
text = []
for i in pages:
    text.append(i)
print type(text)
print text
