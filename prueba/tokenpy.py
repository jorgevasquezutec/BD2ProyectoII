import re
import string
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import TweetTokenizer
from nltk.stem import SnowballStemmer
import sys


nltk.download('punkt')
nltk.download('stopwords')
stemmer = SnowballStemmer('spanish')

def remove_espacial_character(txt):
    characters = ("\"", "\'", "º", "&")
    for character in characters:
        txt = txt.replace(character, "")
    return txt

def remove_punctuation(text):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)


def treat_data(txt):
    list_normalize=[]
    #removemos caracteres especiales y signos de puntuacion
    texto = remove_espacial_character(remove_punctuation(txt))
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



# def buil_index(archivos_txt,data):
	
# 	diccionario={}
# 	for arch in archivos_txt:
# 		#lista de la data tratada por archivo
# 		token_data = treat_data((open(arch, encoding='utf-8').read().lower()))
		
# 		#creaacion del diccionario del indice
# 		for p in token_data:
# 			if not p in diccionario:
# 				diccionario[p] = {}
# 				diccionario[p]['books'] = []
# 			if arch not in diccionario[p]['books']:
# 				diccionario[p]['books'].append(arch)

# 		#Obtenemos los 500 keys con el mayor numero de books (500 términos más frecuentes)
# 		sd = sorted(diccionario, key=lambda v: len(
# 			diccionario[v]['books']), reverse=True)[:500]

# 		#filtramos solo esos keys
# 		for k in sd:
# 			if not k in data:
# 				data[k] = []
# 			data[k] = diccionario[k]['books']

# 	return data


def output_data(outputfile, data):
	#imprimos la data en el formato key : [books]
    out = open(outputfile, 'w')
    out.reconfigure(encoding='utf-8')

    data_to_print = sorted(data.items())
    file = open(outputfile, "w")

    for k, v in data_to_print:
        print(k, " : ", v, file=out)

