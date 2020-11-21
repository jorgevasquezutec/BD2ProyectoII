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

# line = linecache.getline(filename, 2)
# print(line)

# W1,(idf(W1)  	Doc1: tf(W1,Doc1), Doc2: tf(W1,Doc2)
#temp= 000  [[twe1][tw1]]
#calcular lso tf y df
#blokc=20000
# W2,(idf(W1)  	Doc1: tf(W2,Doc1), Doc7: tf(W2,Doc7)

def buildFinalIndex(d):
    of = "test.json"
    for word, data in d.items():
        w = {word : {}}
        w[word]["idf"] = TWEETCOUNT/len(data)
        w[word]["tweets"] = {}
        for tweet in data:
            w[word]["tweets"][tweet["tweet"]] = 1 + math.log10(tweet['fre'])
        finalOutput(of, w)


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

def createIndex(file,index):
    diccionario={}
    df = pd.read_json(file)
    for i, r in df.iterrows():
        idi = r.values[0]
        text = r.values[2]
        words = chain.from_iterable(map(word_tokenize, treatData(text)))
        freq = FreqDist(map(str.casefold, words))
        for w1,w2 in freq.items():
            obj={"tweet":idi,"fre":w2}
            if w1 in diccionario:
                diccionario[w1].append(obj)
            else:
                diccionario[w1] = [obj]

    outputData(OUTPUTFILE+index, diccionario)

def mergeFiles():
    temp=[]



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

    # def getWord(self):
    #     text=linecache.getline(self.name, 1)
    #     return text.split(':')[0].strip()

    # def parseObject(self):
    #     obj={}
    #     text=linecache.getline(self.name, 1)
    #     tempSplit = text.split('{')
    #     for i in range(1, len(tempSplit)):
    #         finalSplit = tempSplit[i].split('}')[0].split(',')
    #         obj[finalSplit[0].split(':')[1].strip()] = int(finalSplit[1].split(':')[1].strip())
    #     return obj

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
    #     createIndex(file,str(cnt) + 'tf_df' + '.json')

    indexFile=getFiles(OUTPUTFILE,EXTENSIONOUT,"tf_df")
    # print(len(indexFile))
    objectIndex=[]
    for file in indexFile:
        objectIndex.append(IndexFile(file))

    # print(objectIndex[0].getCurrentData()[1][0]['fre'])
    # print(objectIndex)
    heap = []
    for i in range(3):
        heapq.heappush(heap, objectIndex[i])

    lastWord = ""
    merge = {}

    while len(heap) > 0:
        temp = heapq.heappop(heap)
        currentWord = temp.getWord()

        if currentWord != lastWord:
            if (len(merge) >= 2000):
                buildFinalIndex(merge)
                merge = {}
            merge[currentWord] = temp.getCurrentData()[1]
        else:
            merge[currentWord].extend(temp.getCurrentData()[1])

        if (temp.updateCurrent()):
            heapq.heappush(heap, temp)
        lastWord = currentWord
    buildFinalIndex(merge)

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


