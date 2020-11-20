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

import math
from io import StringIO
#source https://bit.ly/38HXSoU
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return


import heapq

heap = []
heapq.heappush(heap, (0,'one', 1))
heapq.heappush(heap, (1,'two', 11))
heapq.heappush(heap, (1, 'two', 2))
heapq.heappush(heap, (1, 'one', 3))
heapq.heappush(heap, (1,'two', 3))
heapq.heappush(heap, (1,'one', 4))
heapq.heappush(heap, (1,'two', 5))
heapq.heappush(heap, (1,'one', 1))

show_tree(heap)
