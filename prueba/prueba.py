# from itertools import chain
# from nltk import FreqDist, sent_tokenize, word_tokenize # $ pip install nltk
# import linecache

# # with open('prueba/input.txt') as file:
# #     text = file.read()
# # words = chain.from_iterable(map(word_tokenize, sent_tokenize(text)))
# # freq = FreqDist(map(str.casefold, words))
# # freq.pprint()
# filename='prueba/input.txt'
# line = linecache.getline(filename, 2)
# print(line)

import pandas as pd

df=pd.read_json("out2/0tf_df.json",  nrows = 10, lines = True)
print(df)
# self.orderedList = (pd.read_csv(tableName,skiprows = self.iteration, nrows = self.sizeOfChunk)).values.tolist()
#{ 107 : {DocA : freq}, {DocB: freq}
#
#
#}

#{
#   {107 : freq}
#   {102 : freq}
#   {103 : freq}
#}