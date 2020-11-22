import linecache
import pandas as pd
import json

def getIndexSearch(word,file):
    l=0
    index=pd.read_json(file,lines=True)
    u=len(index)-1
    prev=[]
    line=[]
    while l<=u :
        m=(l+u)//2
        line=json.loads(linecache.getline(file, m))
        if(line[0]>word):
            u=m-1
        elif (line[0]<word):
            l=m+1
        else:
            return line[1]
        prev=line
    return prev

def getIndexWord(word,file):
    # l=0
    # index=pd.read_json(file,lines=True)
    # u=len(index)-1
    # while l<=u :
    #     m=(l+u)//2
    #     line=json.loads(linecache.getline(file, m))
    #     if(line[0]>word):
    #         u=m-1
    #     elif (line[0]<word):
    #         l=m+1
    #     else:
    #         return line[1]
    #     prev=line
    # return prev



print(getNearSearch("ovari","index/index.json"))
