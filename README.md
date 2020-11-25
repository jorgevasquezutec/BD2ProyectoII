# Proyecto 2 de Base de Datos

En este proyecto , se construyó el índice invertido para tweets, en memoria secundaria. Además se construyo un montor de busqueda, para realizar consultas eficientes de terminos dentro de los tweets, y recuperar los tweets.  

## Preprocesamiento de Tweets
Se proceso cada Tweet para eliminar cada palabra de la lista de Stopwords, emoticonos y signos de puntuacion.

## Gestion de Memoria Secundaria

Como no se puede leer todos los indices de todos los archivos a la vez, creamos una cola de prioridad de punteros que apuntan al primer indice de cada archivo. Ademas, creamos un arbol Min Heap en el cual se insertara el primer elemento de la cola de prioridad, mientras la cola no este vacia. 

Una vez se inserte un indice de la cola de prioridad al Min Heap, el puntero que apuntaba a ese indice pasara a apuntar al siguiente elemento de su respectivo archivo. Es asi que la complejidad de formar la lista final de indices sera O( N log ( N / S ) ) donde S es la maxima cantidad de indices puede tener cada archivo final de indices y N es la cantidad inicial de indices 

![MinHeap](images/minheap.jpg)



## Gestion de Memoria Secundaria



## Query
Se explicara como nuestro motor de busqueda realiza una consulta. Primero, para cada palabra de la consulta se llama a la funcion `getIndexSearch` , la cual mediante un algoritmo de busqueda binaria encuentra y retorna el archivo donde posiblemente se encuentra el indice de la palabra. Luego ,  se llama a la funcion `getIndexWord` que tambien realiza un algoritmo de busqueda binaria dentro del archivo que devuelve `getIndexSearch` , y finalmente retorna el indice de la palabra que se busca. 

La complejidad de una Query es igual a O( m (log( K ) + log( S ))) . Donde K es la cantidad de archivos de indices que hay,  S es la cantidad maxima de indices por archivo y  'm' es la cantidad de palabras en la consulta. 



## Futuras Mejoras

Se podria mejorar de calculo de Score e insercion de indices implementandolo con una estructura de datos Max-Heap en lugar de Min-Heap y la complejidad pasaria a ser O(N) donde N es la cantidad de inicial de indices.

## Guia para ejecutar


Ejecutar :
```sh
python3 init.py
```


Para observar el proyecto dirijase a la siguiente direccion de su servidor local.

```sh
127.0.0.1:5000
```

## Imagenes del Motor de busqueda

![imagen1](images/imagen1.png)

![iamgen2](images/imagen2.png)
