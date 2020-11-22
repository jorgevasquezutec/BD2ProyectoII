import linecache
from math import frexp
from logic.tokenpy import *
from logic.process import *
import pandas as pd
import json
import math

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
            return line
        prev=line
    return prev

def getIndexWord(word,obj):
    # pass
    l = 0
    u = obj[1][1]-1
    while l<=u :
        m=(l+u)//2
        prevline=linecache.getline(obj[1][0], m)
        if len(prevline)!=0:
            line=json.loads(prevline)
            if(list(line.keys())[0]==word):
                return line
            elif (list(line.keys())[0]<word):
                l=m+1
            else:
                u=m-1
        else:
            break
    return {word:{}}

def search(query, K):
    words = treatData(query)
    freq = countFrequency(words)
    nonDuplicate = list(dict.fromkeys(words))
    print(nonDuplicate)
    res = []
    for word in nonDuplicate:
        obj = getIndexSearch(word, "index/index.json")
        indexword=getIndexWord(word, obj)
        if list(indexword.values())[0]!={}:
            res.append(getIndexWord(word, obj))
    # print(res)
    return calculateScore(res, freq, K)

def calculateScore(words, queryFrequencies, K):
    columns = []
    data = {}
    for word in words:
        key = list(word.keys())[0]
        for tweet in list(word[key]['tweets'].keys()):
            if tweet not in columns:
                columns.append(tweet)

    idfs = {}

    for word in words:
        key = list(word.keys())[0]
        data[key] = []
        idfs[key] = word[key]['idf']
        idf = word[key]['idf']
        for tweet in columns:
            if tweet in word[key]['tweets']:
                data[key].append(word[key]['tweets'][tweet]*idf)
            else:
                data[key].append(0)
    df = pd.DataFrame.from_dict(data, orient='index', columns=columns)

    q = []
    for word in df.index:
        tf = math.log10(queryFrequencies[word] + 1)
        idf =  idfs[word]
        q.append(tf*idf)

    df['Query'] = q

    norm = {}
    for col in df.columns:
        acum = 0
        for row in df.index:
            acum += (df[col][row]**2)
        norm[col] = math.sqrt(acum)

    for col in df.columns:
        nlize = []
        for row in df.index:
            nlize.append(df[col][row]/norm[col])
        df[f"nlize {col}"] = nlize

    scores = {}
    for tweet in columns:
        scores[tweet] = 0
        for row in df.index:
            scores[tweet] += df[f"nlize {tweet}"][row] * df["nlize Query"][row]

    # Resalta como error pero si corre
    sortedTweets = sorted(scores, reverse= True, key = scores.get)

    return sortedTweets[:K]

# search("Ejercicio de educacion eficiente eficiente",10)
