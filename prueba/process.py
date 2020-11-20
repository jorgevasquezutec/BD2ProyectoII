import os
from os.path import isfile, join
import pandas as pd
from constants import *
from tokenpy import *
from itertools import chain
from nltk import FreqDist, sent_tokenize, word_tokenize # $ pip install nlt
import linecache

# line = linecache.getline(filename, 2)
# print(line)

# W1,(idf(W1)  	Doc1: tf(W1,Doc1), Doc2: tf(W1,Doc2)
# W2,(idf(W1)  	Doc1: tf(W2,Doc1), Doc7: tf(W2,Doc7)

def getFiles(FILES,EXTENSION,BEGIN):
    archivos_txt = []
    for base, dirs, files in os.walk(FILES):
        for file in files:
            fich = join(base, file)
            if fich.endswith(EXTENSION) and BEGIN in fich:
                archivos_txt.append(fich)
    return archivos_txt

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
                diccionario[w1] = []
                diccionario[w1].append(obj)

    outputData(OUTPUTFILE+index, diccionario)


def mergeFiles():
    temp=[]



class IndexFile:

    def __init__(self, nameFile):
        self.name = nameFile
        self.word = self.getWord()
        self.iteration = 1
        self.pointer= self.parseObject()
        self.size=sum(1 for line in open( self.name))

    def getWord(self):
        text=linecache.getline(self.name,  self.iteration)
        return text.split(':')[0].strip()

    def parseObject(self):
        obj={}
        text=linecache.getline(self.name,  self.iteration)
        tempSplit = text.split('{')
        for i in range(1, len(tempSplit)):
            finalSplit = tempSplit[i].split('}')[0].split(',')
            obj[finalSplit[0].split(':')[1].strip()] = int(finalSplit[1].split(':')[1].strip())
        return obj



def main():
    files = getFiles(FILES,EXTENSION,BEGIN)
    for cnt,file in enumerate(files):
        createIndex(file,str(cnt) + 'tf_df' + '.json')



    # indexFile=getFiles(OUTPUTFILE,EXTENSIONOUT,"tf_df")
    # objectIndex=[]
    # for file in indexFile:
    #     objectIndex.append(IndexFile(file))


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


