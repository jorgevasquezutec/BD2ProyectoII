# import json
# with open('prueba/tweets_2018-08-07.json') as infile:
#   o = json.load(infile)
#   chunkSize = 1000
#   for i in range(0, len(o), chunkSize):
#     with open('file_' + str(i//chunkSize) + '.json', 'w') as outfile:
#       json.dump(o[i:i+chunkSize], outfile)


import pandas as pd
for index,chunk in enumerate(pd.read_json('0tf_df.txt', lines=True, chunksize=5),start=1):
    print(chunk)
