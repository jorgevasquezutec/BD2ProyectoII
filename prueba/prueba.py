from itertools import chain
from nltk import FreqDist, sent_tokenize, word_tokenize # $ pip install nltk
import linecache 

# with open('prueba/input.txt') as file:
#     text = file.read()
# words = chain.from_iterable(map(word_tokenize, sent_tokenize(text)))
# freq = FreqDist(map(str.casefold, words))
# freq.pprint()
filename='prueba/input.txt'
line = linecache.getline(filename, 2)
print(line)