# import json
# with open('prueba/tweets_2018-08-07.json') as infile:
#   o = json.load(infile)
#   chunkSize = 1000
#   for i in range(0, len(o), chunkSize):
#     with open('file_' + str(i//chunkSize) + '.json', 'w') as outfile:
#       json.dump(o[i:i+chunkSize], outfile)


import pandas as pd
# import json 
chunk=pd.read_json('out2/0tf_df.json', lines=True, chunksize=5,nrows=100)
print(chunk.open_stream)
# d1=pd.read_json('out2/0tf_df.json', lines=True, chunksize=100)

