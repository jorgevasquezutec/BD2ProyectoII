import os
from os.path import isfile, join
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import sys


nltk.download('punkt')
nltk.download('stopwords')
stemmer = SnowballStemmer('spanish')

RAIZ = './'
EXTENSION = ".txt"
BEGIN = "lib"

data = {}


def getFiles():
    archivos_txt = []
    for base, dirs, files in os.walk(RAIZ):
        for file in files:
            fich = join(base, file)
            if fich.endswith(EXTENSION) and BEGIN in fich:
                archivos_txt.append(fich)
    return archivos_txt


def removeSpecialCharacters(txt):
    characters = ("\"", "\'", "º", "&")
    for character in characters:
        txt = txt.replace(character, "")
    return txt


def removePunctuation(text):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)


def treat_data(txt):
    list_normalize=[]
    #removemos caracteres especiales y signos de puntuacion
    texto = removeSpecialCharacters(removePunctuation(txt))
    tokens = nltk.word_tokenize(texto)
    #Filtrar los stopwords
    stoplist = stopwords.words("spanish")
    stoplist += ['?', 'aqui','.',',','»','«','â','ã','>','<','(',')','º']
    # tokens_clean = tokens.copy()
    filtered = [w for w in tokens if not w in stoplist and len(w) >= 3]
    #Reduccion de Tokens(Normalizacion)
    for p in filtered:
        list_normalize.append(stemmer.stem(p))

    return list_normalize



def buildIndex(archivos_txt):

	diccionario={}
	for arch in archivos_txt:
		#lista de la data tratada por archivo
		token_data = treat_data((open(arch, encoding='utf-8').read().lower()))

		#creaacion del diccionario del indice
		for p in token_data:
			if not p in diccionario:
				diccionario[p] = {}
				diccionario[p]['books'] = []
			if arch not in diccionario[p]['books']:
				diccionario[p]['books'].append(arch)

		#Obtenemos los 500 keys con el mayor numero de books (500 términos más frecuentes)
		sd = sorted(diccionario, key=lambda v: len(
			diccionario[v]['books']), reverse=True)[:500]

		#filtramos solo esos keys
		for k in sd:
			if not k in data:
				data[k] = []
			data[k] = diccionario[k]['books']

	return data


def outputData(outputfile, data):
	#imprimos la data en el formato key : [books]
    out = open(outputfile, 'w')
    out.reconfigure(encoding='utf-8')

    data_to_print = sorted(data.items())
    file = open(outputfile, "w")

    for k, v in data_to_print:
        print(k, " : ", v, file=out)


def recovery(list):
    print(list)


def AND(list1, list2):
    lista_res = []
    min_ = min(len(list1), len(list2))
    j = 0
    k = 0
    for i in range(min_):
        if(list1[j] == list2[k]):
            lista_res.append(list1[j])
            j += 1
            k += 1
        elif(int(list1[j][-5]) < int(list2[k][-5])):
            j += 1
        else:
            k += 1

    return lista_res


def OR(list1, list2):
    lista_rest = []
    j = 0
    k = 0
    while(j < len(list1) and k < len(list2)):
        if(list1[j] == list2[k]):
            lista_rest.append(list1[j])
            j += 1
            k += 1
        elif(int(list1[j][-5]) < int(list2[k][-5])):
            lista_rest.append(list1[j])
            j += 1
        else:
            lista_rest.append(list2[k])
            k += 1

    if(j != k):
        if(j == len(list1)):
            lista_rest += list2[k:len(list2)]
        else:
            lista_rest += list1[j:len(list1)]

    return lista_rest


def L(key):
    _token = stemmer.stem(key.lower())
    return data[_token]


def AND_NOT(list1, list2):
    lista_res = []
    j = 0
    k = 0
    while(j < len(list1) and k < len(list2)):
        if(list1[j] == list2[k]):
            j += 1
            k += 1
        elif(int(list1[j][-5]) < int(list2[k][-5])):
            lista_res.append(list1[j])
            j += 1
        elif(int(list1[j][-5]) > int(list2[k][-5])):
            k += 1
    if(j < len(list1)):
        lista_res += list1[j:len(list1)]

    return lista_res


def main():

    files = getFiles()
    data = buildIndex(files)
    outputData("stdout.txt", data)
    print("QUERY1")
    recovery(AND(AND(L('Frodo'), L('Gollum')), L('Gandalf')))
    print("QUERY2")
    recovery(AND(AND_NOT(L('Frodo'), L('Gollum')), L('Gandalf')))
    print("QUERY3")
    recovery(AND(OR(L('Frodo'), L('Gollum')), L('Gandalf')))


if __name__ == "__main__":
    main()
