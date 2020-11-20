import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem import SnowballStemmer
import sys
import json

nltk.download('punkt')
nltk.download('stopwords')
stemmer = SnowballStemmer('spanish')

def removeSpecialCharacters(txt):
    characters = ("\"", "\'", "º", "&")
    for character in characters:
        txt = txt.replace(character, "")
    return txt

def removePunctuation(text):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)


def treatData(txt):
    list_normalize=[]
    #removemos caracteres especiales y signos de puntuacion
    texto = removeSpecialCharacters(removePunctuation(txt))
    tknzr = TweetTokenizer(preserve_case=False,strip_handles=True, reduce_len=True)
    tokenized = tknzr.tokenize(texto)
    #Filtrar los stopwords
    stoplist = stopwords.words("spanish")
    stoplist += ['?', 'aqui','.',',','»','«','â','ã','>','<','(',')','º']
    # tokens_clean = tokens.copy()
    filtered = [w for w in tokenized if not w in stoplist and len(w) >= 3]

    for p in filtered:
        list_normalize.append(stemmer.stem(p))

    return list_normalize

def outputData(outputfile, data):
	#imprimos la data en el formato key : [books]
    data_to_print = sorted(data.items())
    import json
    with open(outputfile, 'w') as fp:
        fp.reconfigure(encoding='utf-8')
        json.dump(data_to_print, fp)



    # for k, v in data_to_print:
    #     print(k, " : ", v, file=out)
