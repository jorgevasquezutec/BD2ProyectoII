import heapq
import json
import linecache
import math
import os
from io import StringIO
from itertools import chain
from os.path import isfile, join

import pandas as pd
from nltk import FreqDist, sent_tokenize, word_tokenize  # $ pip install nlt

from constants import *
from tokenpy import *
import collections


# line = linecache.getline(filename, 2)
# print(line)

# W1,(idf(W1)  	Doc1: tf(W1,Doc1), Doc2: tf(W1,Doc2)
#temp= 000  [[twe1][tw1]]
#calcular lso tf y df
#blokc=20000
# W2,(idf(W1)  	Doc1: tf(W2,Doc1), Doc7: tf(W2,Doc7)

def countFrequency(arr):
    return collections.Counter(arr)


def buildFinalIndex(d,index_file):
    # word, data
    text=""
    for i,data in enumerate(d.items()):
        w = {data[0] : {}}
        w[data[0]]["idf"] = math.log10(TWEETCOUNT/len(data[1]))
        w[data[0]]["tweets"] = {}
        for tweet in data[1]:
            w[data[0]]["tweets"][tweet["tweet"]] = math.log10(1 + tweet['fre'])
        text+=json.dumps(w,ensure_ascii=False)
        text+="\n" if i!=len(d.items())-1 else ""
    finalOutput(index_file,text)


def getFiles(FILES,EXTENSION,BEGIN):
    archivos_txt = []
    for base, dirs, files in os.walk(FILES):
        for file in files:
            fich = join(base, file)
            if fich.endswith(EXTENSION) and BEGIN in fich:
                archivos_txt.append(fich)
    return archivos_txt

def createChunks(file):
    name=(os.path.splitext(os.path.basename(file))[0])
    with open(file) as infile:
        o = json.load(infile)
        chunkSize = CHUNKSIZE
        for i in range(0, len(o), chunkSize):
            with open(CHUNKFILE+ name+"-"+str(i//chunkSize)+".json", 'w') as outfile:
                json.dump(o[i:i+chunkSize], outfile)

def createIndex(file):
    diccionario={}
    df = pd.read_json(file)
    name=(os.path.splitext(os.path.basename(file))[0])
    for i, r in df.iterrows():
        idi = r.values[0]
        text = r.values[2]
        data=treatData(text)
        freq = countFrequency(data)
        for (key, value) in freq.items():
            my_dict = {}
            my_dict["tweet"] = idi
            my_dict["fre"] = value
            if key not in diccionario:
                diccionario[key]=[my_dict]
            else:
                diccionario[key].append(my_dict)

    outputData(OUTPUTFILE+name+".json", diccionario)


class IndexFile:

    def __init__(self, nameFile):
        self.name = nameFile
        self.iterator = iter(pd.read_json(nameFile, lines=True, chunksize=BLOCK))
        self.data = next(self.iterator,None)#dataframe
        self.current = 0

    def getCurrentData(self):
        return self.data.iloc[self.current]

    def getCurrentDataTuple(self):
        data = self.getCurrentData()
        return (data[1], data[0])

    def updateCurrent(self):
        self.current += 1
        if self.current >= len(self.data.index):
            self.current = 0
            self.data = next(self.iterator, None)
            if self.data is None:
                return False
        return True

    def getWord(self):
        return self.getCurrentData()[0]

    def __lt__(self, other):
        return self.getCurrentData()[0] < other.getCurrentData()[0]



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
        output.write(str(n.getWord()).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

def main():
    # files = getFiles(FILES,EXTENSION,BEGIN)
    # for file in files:
    #     createChunks(file)
    # chunks=getFiles(CHUNKFILE,EXTENSION,BEGIN)
    # for cnt,file in enumerate(chunks):
    #     createIndex(file)

    indexFile=getFiles(OUTPUTFILE,EXTENSIONOUT,"tweets")
    # print(len(indexFile))
    objectIndex=[]
    for file in indexFile:
        objectIndex.append(IndexFile(file))

    # print(objectIndex[0].getCurrentData()[1][0]['fre'])
    # print(objectIndex)
    heap = []
    for i in range(3):
        print(objectIndex[i].name)
        heapq.heappush(heap, objectIndex[i])

    lastWord = ""
    merge = {}
    index_file=0
    of = "index/"+str(index_file)+"merge.json"
    indexKey={}

    while len(heap) > 0:
        temp = heapq.heappop(heap)
        currentWord = temp.getWord()

        if currentWord != lastWord:
            if (len(merge) >= FILE_EXTENSION):
                buildFinalIndex(merge,of)
                of = "index/"+str(index_file)+"merge.json"
                indexKey[list(merge.keys())[0]]=[of,len(merge)]
                buildFinalIndex(merge,of)
                index_file += 1
                merge = {}
            merge[currentWord] = temp.getCurrentData()[1]
        else:
            merge[currentWord].extend(temp.getCurrentData()[1])

        if (temp.updateCurrent()):
            heapq.heappush(heap, temp)
        lastWord = currentWord
    of = "index/"+str(index_file)+"merge.json"
    buildFinalIndex(merge,of)
    indexKey[list(merge.keys())[0]]=[of,len(merge)]
    outputData("index/index.json",indexKey)


    #tenngo que crear un minhead solo con el word

if __name__ == "__main__":
    main()







# def mergeTables(self):
# 		class TableClass:
# 			def __init__(self, tableName):
# 				self.name = tableName
# 				self.sizeOfChunk = SORTED_CHUNK
# 				self.last = False
# 				self.empty = False
# 				self.iteration = 0
# 				self.orderedList = (pd.read_csv(tableName,skiprows = self.iteration, nrows = self.sizeOfChunk)).values.tolist()
# 				self.size = len(pd.read_csv(tableName))

# 			def getFirst(self):
# 				return self.orderedList[0][0]

# 			def __lt__(self,other):
# 				return str(self.getFirst()) < str(other.getFirst())

# 			def updateList(self):
# 				self.iteration += 1
# 				if((self.iteration+1)*self.sizeOfChunk-1 >= self.size):
# 					self.last = True
# 				skip = self.iteration * self.sizeOfChunk
# 				self.orderedList = (pd.read_csv(self.name,skiprows = skip, nrows = self.sizeOfChunk)).values.tolist()

# 			def popFirst(self):
# 				value = self.orderedList.pop(0)
# 				if(len(self.orderedList) == 0 and self.last == True):
# 					self.empty = True
# 				elif(len(self.orderedList) == 0):
# 					self.updateList()
# 				return value

# 		tableClasses = []
# 		for i in os.listdir(PATH + 'chunks'):
# 			if i.endswith('tf_df.csv'):
# 				tableClasses.append(TableClass(PATH + 'chunks/'+ i))

# 		heapq.heapify(tableClasses)
# 		while(len(tableClasses) > 0):
# 			tmp = []
# 			tmp = tableClasses[0].popFirst()
# 			tmp[1] = ast.literal_eval(tmp[1])
# 			while(tableClasses[0].empty == True):
# 				tableClasses.pop(0)
# 			heapq.heapify(tableClasses)
# 			while(tableClasses[0].getFirst() == tmp[0]):
# 				tmp[1].update(ast.literal_eval(tableClasses[0].popFirst()[1]))
# 				while(tableClasses[0].empty == True):
# 					tableClasses.pop(0)
# 				heapq.heapify(tableClasses)
# 			self.writeLine(PATH + "merged.csv",tmp)
# 			heapq.heapify(tableClasses)


