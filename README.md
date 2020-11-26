# Victor Ostolaza
# Jorge Vasquez
# Jorge Rebosio

# Proyecto 2 de Base de Datos

En este proyecto , se construyó el índice invertido para tweets, en memoria secundaria. Además se construyo un montor de busqueda, para realizar consultas eficientes de terminos dentro de los tweets, y recuperar los tweets.  

## Preprocesamiento de Tweets
Se proceso cada Tweet para eliminar cada palabra de la lista de Stopwords, emoticonos y signos de puntuacion.

## Gestion de Memoria Secundaria

Como no se puede leer todos los indices de todos los archivos a la vez, creamos un objeto  que contiene a los punteros que apuntan al primer indice de cada archivo. Ademas, creamos una estructura de datos arbol Min Heap en el cual se iran insertando los punteros de cada archivo, mientras la cola no este vacia. Inicialmente al Min Heap se le inserta el puntero al primer indice de cada archivo. Despues,  cuando el min heap este completo(se haya insertado un puntero por archivo), se elimina el puntero que esta en el root del Min Heap(indice con word lexicograficamente menor) y se anade este puntero al diccionario Merge. Asimismo, se agrega al Min Heap el puntero que apunta al indice siguiente al indice que se acaba de eliminar. (falta...)

Cuando se inserte un indice del objeto que contiene a los punteros al Min Heap, el puntero que apuntaba a ese indice pasara a apuntar al siguiente elemento de su respectivo archivo. Es asi que la complejidad de formar la lista final de indices sera O( N log ( N / S ) ) donde S es la maxima cantidad de indices puede tener cada archivo final de indices y N es la cantidad inicial de indices 

![MinHeap](images/minheap.jpg)



## Gestion de Memoria Secundaria



## Query
Se explicara como nuestro motor de busqueda realiza una consulta. Primero, para cada palabra de la consulta se llama a la funcion `getIndexSearch` , la cual mediante un algoritmo de busqueda binaria encuentra y retorna el archivo donde posiblemente se encuentra el indice de la palabra. Luego ,  se llama a la funcion `getIndexWord` que tambien realiza un algoritmo de busqueda binaria dentro del archivo que devuelve `getIndexSearch` , y finalmente retorna el indice de la palabra que se busca. 

La complejidad de una Query es igual a O( m (log( K ) + log( S ))) . Donde K es la cantidad de archivos de indices que hay,  S es la cantidad maxima de indices por archivo y  'm' es la cantidad de palabras en la consulta. 


## Requisitos

* Flask

* FlaskCors

* Python

* Servidor local para cargar pagina

## Guia para ejecutar


Ejecutar :
```sh
python3 init.py
```


Para observar el proyecto dirijase a la siguiente direccion de su servidor local.

```sh
127.0.0.1:8080
```

## Videos
* [Primer Video](https://www.youtube.com/watch?v=TArJYOTmYt8&feature=youtu.be)

* [Segundo Video](https://www.youtube.com/watch?v=77B7T_GNKPI)
## Imagenes del Motor de busqueda

![imagen1](images/imagen1.png)

![iamgen2](images/imagen2.png)
