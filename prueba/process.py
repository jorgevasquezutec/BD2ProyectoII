import os
from os.path import isfile, join
import pandas as pd
from constants import *
from tokenpy import *
from itertools import chain
from nltk import FreqDist, sent_tokenize, word_tokenize # $ pip install nlt

# W1,(idf(W1)  	Doc1: tf(W1,Doc1), Doc2: tf(W1,Doc2)
# W2,(idf(W1)  	Doc1: tf(W2,Doc1), Doc7: tf(W2,Doc7)

def getFiles():
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
        words = chain.from_iterable(map(word_tokenize, treat_data(text)))
        freq = FreqDist(map(str.casefold, words))
        for w1,w2 in freq.items():
            obj={"tweet":idi,"fre":w2}
            if w1 in diccionario:
                diccionario[w1].append(obj)
            else:
                diccionario[w1] = []
                diccionario[w1].append(obj)
    
    output_data(OUTPUTFILE+index, diccionario)

        
    
        
def main():
    files=getFiles()
    for cnt,file in enumerate(files):
        createIndex(file,str(cnt) + 'tf_df' + '.txt')


if __name__ == "__main__":
    main()


