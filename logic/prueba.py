# import json
# with open('prueba/tweets_2018-08-07.json') as infile:
#   o = json.load(infile)
#   chunkSize = 1000
#   for i in range(0, len(o), chunkSize):
#     with open('file_' + str(i//chunkSize) + '.json', 'w') as outfile:
#       json.dump(o[i:i+chunkSize], outfile)


# import pandas as pd
# # import json 
# chunk=pd.read_json('prueba/prueba.json', lines=True, chunksize=5)
# # data=next(x,None)
# while(data is not None):
#     print(data)
#     data=next(x,None)
    

# print(chunk.__next__)
# d1=pd.read_json('out2/0tf_df.json', lines=True, chunksize=100)

# import math
# from io import StringIO
# #source https://bit.ly/38HXSoU
# def show_tree(tree, total_width=60, fill=' '):
#     """Pretty-print a tree.
#     total_width depends on your input size"""
#     output = StringIO()
#     last_row = -1
#     for i, n in enumerate(tree):
#         if i:
#             row = int(math.floor(math.log(i+1, 2)))
#         else:
#             row = 0
#         if row != last_row:
#             output.write('\n')
#         columns = 2**row
#         col_width = int(math.floor((total_width * 1.0) / columns))
#         output.write(str(n).center(col_width, fill))
#         last_row = row
#     print (output.getvalue())
#     print ('-' * total_width)
#     return


# import heapq

# heap = []
# heapq.heappush(heap, (0,'one', 1))
# heapq.heappush(heap, (1,'two', 11))
# heapq.heappush(heap, (1, 'two', 2))
# heapq.heappush(heap, (1, 'one', 3))
# heapq.heappush(heap, (1,'two', 3))
# heapq.heappush(heap, (1,'one', 4))
# heapq.heappush(heap, (1,'two', 5))
# heapq.heappush(heap, (1,'one', 1))

# show_tree(heap)
from process import *
import collections

def CountFrequency(arr): 
    return collections.Counter(arr)


file="chunk/tweets_2018-09-15-2.json"
df=pd.read_json(file)
diccionario={}

docid="121212121"
text="hola hola como estas me llamo llamo javier costa y yo soy juan gablriel"
data=treatData(text)
freq = CountFrequency(data)
for (key, value) in freq.items():
        my_dict = {}
        my_dict["tweet"] = docid
        my_dict["frec"] = value
        if key not in diccionario:
            diccionario[key]=[my_dict]
        else:
            diccionario[key].append(my_dict)
# print(diccionario)
data_to_print = sorted(diccionario.items())
print(data_to_print)
result=""
for data in data_to_print:
    result+=json.dumps(data)+"\n"

with open('logic/data.json', 'w') as outfile:
    print(result,file=outfile)





# name=(os.path.splitext(os.path.basename(file))[0])
# for i, r in df.iterrows():
#     idi = r.values[0]
#     text = r.values[2]
#     print(text)
#     print(treatData(text))
    # words = chain.from_iterable(map(word_tokenize, treatData(text)))
    # freq = FreqDist(map(str.casefold, words))
    # for w1,w2 in freq.items():
    #     obj={"tweet":idi,"fre":w2}
    #     if w1 in diccionario:
    #         diccionario[w1].append(obj)
    #     else:
    #         diccionario[w1] = [obj]

# print(diccionario)




