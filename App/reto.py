"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
import collections
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as shell
from Sorting import selectionsort as selection
from Sorting import insertionsort as insertion
from time import process_time


def print_menu():
    """
    Imprime el menu de opciones
    """
    print('\nBienvenido')
    print('1- Cargar Datos')
    print('2- Contar las películas de la Lista')
    print('3- Contar películas de un director')
    print('4- Consultar buenas películas de un director')
    print('5- Ordenar películas por votos')
    print('6- Conocer a un director y todas sus películas')
    print('7- Conocer a un actor y todas sus películas')
    print('0- Salir')


def load_csv_file(file_d, file_c, sep=';'):
    """
    Carga un archivo csv a una lista
    Args:
        file_d
            Archivo de texto del cual se cargaran los detalles de las películas.
        file_c
            Archivo de texto del cual se cargaran los castings de las películas.
        sep :: str
            Separadores código para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None
    """
    # lst_d, lst_c = lt.newList('ARRAY_LIST'), lt.newList('ARRAY_LIST')  # Usando implementacion arraylist
    lst_d, lst_c = lt.newList('SINGLE_LINKED'), lt.newList('SINGLE_LINKED')  # Usando implementacion linkedlist
    print('Cargando archivos...')
    t1_start = process_time()  # Start time
    dialect, dialect.delimiter = csv.excel(), sep
    try:
        with open(file_d, encoding='utf-8-sig') as csvfile_d, open(file_c, encoding='utf-8-sig') as csvfile_c:
            spamreader_d, spamreader_c = (csv.DictReader(csvfile_d, dialect=dialect),
                                          csv.DictReader(csvfile_c, dialect=dialect))
            for row_d, row_c in zip(spamreader_d, spamreader_c):
                lt.addLast(lst_d, row_d)
                lt.addLast(lst_c, row_c)
    except:
        lst_d, lst_c = lt.newList('ARRAY_LIST'), lt.newList('ARRAY_LIST')
        print('Se presentó un error en la carga de los archivos')
    t1_stop = process_time()  # Final time
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return lst_d, lst_c


def count_director_movies(director, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada
    Args:
        director:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        lst
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size'] == 0:
        print('La lista esta vacía')
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            element = it.next(iterator)
            if director.lower() in element[column].lower():  # filtrar por palabra clave
                counter += 1
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return counter


def get_director_movie_ids(search, result, director):
    iterator = it.newIterator(search)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if director.lower() in element['director_name'].lower():  # filtrar por nombre
            lt.addLast(result, element['id'])

def get_actor_name_id(search, result, actor):
    iterator = it.newIterator(search)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if actor.lower() in element['actor1_name'].lower():
            lt.addLast(result,element['id'])
        elif actor.lower() in element['actor2_name'].lower():
            lt.addLast(result,element['id'])
        elif actor.lower() in element['actor3_name'].lower():
            lt.addLast(result,element['id'])
        elif actor.lower() in element['actor4_name'].lower():
            lt.addLast(result,element['id'])
        elif actor.lower() in element['actor5_name'].lower():
            lt.addLast(result,element['id'])

def get_actor_director(search, result, actor):
    iterator = it.newIterator(search)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if actor.lower() in element['actor1_name'].lower():
            lt.addLast(result,element['director_name'])
        elif actor.lower() in element['actor2_name'].lower():
            lt.addLast(result,element['director_name'])
        elif actor.lower() in element['actor3_name'].lower():
            lt.addLast(result,element['director_name'])
        elif actor.lower() in element['actor4_name'].lower():
            lt.addLast(result,element['director_name'])
        elif actor.lower() in element['actor5_name'].lower():
            lt.addLast(result,element['director_name'])
       
def movies_total_average(movies):
    iterator = it.newIterator(movies)
    votes_sum = 0
    while it.hasNext(iterator):
        element = it.next(iterator)
        votes_sum += float(element['vote_average'])
    total_vote_average = votes_sum / movies['size']
    return round(total_vote_average, 1)


def find_good_movies(director, vote_average, lst_d, lst_c):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
        return 0, 0
    else:
        t1_start = process_time()  # tiempo inicial
        all_director_movies, good_movies = (lt.newList('ARRAY_LIST') for _ in range(2))
        # Search all director movie ids and add them to a list.
        get_director_movie_ids(lst_c, all_director_movies, director)
        # Search good movies and add vote points to list.
        iterator_ids = it.newIterator(all_director_movies)
        while it.hasNext(iterator_ids):
            movie_id = it.next(iterator_ids)
            iterator_movies = it.newIterator(lst_d)
            while it.hasNext(iterator_movies):
                movie = it.next(iterator_movies)
                if movie_id == movie['id']:
                    actual_vote = float(movie['vote_average'])
                    if actual_vote >= vote_average:
                        lt.addLast(good_movies, movie)
        show_movies(good_movies, director)
        # Calculate number of good movies and total vote average of director.
        total_vote_average = movies_total_average(good_movies)
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return good_movies['size'], total_vote_average


def know_director(director, lst_d, lst_c):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
        return 0, 0
    else:
        t1_start = process_time()  # tiempo inicial
        all_director_movies, movies_data = (lt.newList('ARRAY_LIST') for _ in range(2))
        # Search all director movie ids and add them to a list.
        get_director_movie_ids(lst_c, all_director_movies, director)
       
        # Search movies and add vote points to list.
        iterator_ids = it.newIterator(all_director_movies)
        while it.hasNext(iterator_ids):
            movie_id = it.next(iterator_ids)
            iterator_movies = it.newIterator(lst_d)
            while it.hasNext(iterator_movies):
                movie = it.next(iterator_movies)
                if movie_id == movie['id']:
                    lt.addLast(movies_data, movie)
        show_movies(movies_data, director)
        # Calculate number of movies and total vote average of director.
        total_vote_average = movies_total_average(movies_data)
        t1_stop = process_time()  # tiempo final
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return movies_data['size'], total_vote_average


def show_movies(movies, director):
    if director is not None:
        print('Las películas dirigidas por', director, 'son:')
        iterator = it.newIterator(movies)
        while it.hasNext(iterator):
            element = it.next(iterator)
            print('-', element['title'])
    else:
        iterator = it.newIterator(movies)
        while it.hasNext(iterator):
            element = it.next(iterator)
            print('-', element['title'] + ':',
                  '\n   con un puntaje promedio de', element['vote_average'],
                  'y un total de', element['vote_count'], 'votaciones')

def actor_movies(movies,actor):
    if actor is not None:
        print('Las películas protagonizadas por', actor, 'son:')
        iterator = it.newIterator(movies)
        while it.hasNext(iterator):
            element = it.next(iterator)
            print('-',element['title'])
    else:
        iterator = it.newIterator(movies)
        element = it.next(iterator)
        print('-',element['title'] + ':',
                    '\n con un puntaje promedio de', element['vote_average'],
                    'y un total de', element['vote_count'], 'votaciones')

"""
def filtro_directores(lista_dct):
    lista_directores = []
    for i in range(0,lista_dct['size']):
        if lista_dct['elements'][i] not in lista_directores:
            lista_directores.append(lista_dct['elements'][i])
    print(lista_directores)
    return lista_directores
     """   

def know_actor(actor, lst_movies, lst_casting):
    if len(lst_movies) == 0:
        print('Las listas están vacías')
        return 0, 0
    else:
        t1_start = process_time()
        peliculas_actor = lt.newList('ARRAY_LIST')
        movies_data = lt.newList('ARRAY_LIST')
        director = lt.newList('ARRAY_LIST')
        get_actor_name_id(lst_casting,peliculas_actor,actor)
        get_actor_director(lst_casting,director,actor)
        iterator_id = it.newIterator(peliculas_actor)
        while it.hasNext(iterator_id):
            movie_id = it.next(iterator_id)
            iterator_movies = it.newIterator(lst_movies)
            while it.hasNext(iterator_movies):
                movie =it.next(iterator_movies)
                if movie_id == movie['id']:
                    lt.addLast(movies_data,movie)
        
        
        lista_directores = collections.Counter(director['elements']).most_common(1)
        director_colaboraciones = lista_directores[0][0]
        actor_movies(movies_data, actor)
        total_vote_average = movies_total_average(movies_data)
        t1_stop = process_time()
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
        return movies_data['size'], total_vote_average, director_colaboraciones


def less_average(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True
    return False


def greater_average(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False


def less_count(element1, element2):
    if float(element1['vote_count']) < float(element2['vote_count']):
        return True
    return False


def greater_count(element1, element2):
    if float(element1['vote_count']) > float(element2['vote_count']):
        return True
    return False


def order_movies(function, lst_d, req_elements, algorithm, column):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if len(lst_d) == 0:
        print('Las listas están vacías')
    else:
        t1_start = process_time()  # tiempo inicial
        # Sort movies.
        if algorithm == 'selection':
            if function == 'less':
                selection.selectionSort(lst_d, less_count) if column == 'vote_count' \
                    else selection.selectionSort(lst_d, less_average)
            elif function == 'greater':
                selection.selectionSort(lst_d, greater_count) if column == 'vote_count' \
                    else selection.selectionSort(lst_d, greater_average)
        elif algorithm == 'shell':
            if function == 'less':
                shell.shellSort(lst_d, less_count) if column == 'vote_count' \
                    else shell.shellSort(lst_d, less_average)
            elif function == 'greater':
                shell.shellSort(lst_d, greater_count) if column == 'vote_count' \
                    else shell.shellSort(lst_d, greater_average)
        elif algorithm == 'insertion':
            if function == 'less':
                insertion.insertionSort(lst_d, less_count) if column == 'vote_count' \
                    else insertion.insertionSort(lst_d, less_average)
            elif function == 'greater':
                insertion.insertionSort(lst_d, greater_count) if column == 'vote_count' \
                    else insertion.insertionSort(lst_d, greater_average)
        t1_stop = process_time()  # tiempo final
        print(req_elements, 'best' if function == 'greater' else 'worst',
              'count:' if column == 'vote_count' else 'average:')
        show_movies(lt.subList(lst_d, 0, int(req_elements)), None)
        print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None
    """
    details_list = lt.newList('ARRAY_LIST')
    while True:
        print_menu()  # imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar:\n')  # leer opción ingresada
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                details_list, casting_list = load_csv_file('Data/Peliculas/SmallMoviesDetailsCleaned.csv',
                                                           'Data/Peliculas/MoviesCastingRaw-small.csv')  # Cargar datos
                if len(details_list) == len(casting_list):
                    print('Datos cargados, ' + str(details_list['size']) + ' elementos cargados en listas')
                else:
                    print('Datos cargados, aunque inconsistentes')
            elif int(inputs[0]) == 2:  # opcion 2
                if details_list['size'] == 0:  # obtener la longitud de la lista
                    print('La lista esta vacía')
                else:
                    print('La lista tiene ' + str(details_list['size']) + ' elementos')
            elif int(inputs[0]) == 3:  # opcion 3
                director = input('Ingrese un director para consultar su cantidad de películas:\n')  # filtrar columna
                counter_movies = count_director_movies(director, 'director_name', casting_list)
                print('Coinciden', counter_movies, 'elementos con el director', director)
            elif int(inputs[0]) == 4:  # opcion 4
                director = input('Ingrese el nombre del director para conocer sus buenas películas:\n')
                counter, average = find_good_movies(director, 6, details_list, casting_list)
                print('Existen', counter, 'buenas películas del director', director, 'en el catálogo')
                print('Las buenas películas de este director tienen un promedio de votación de', average, 'puntos.')
            elif int(inputs[0]) == 5:  # opcion 5
                print('Ranking de películas')
                req = input('Ingrese el número de películas requeridas: ')
                while int(req) < 10:
                    req = input('Ingrese por lo menos 10 películas requeridas: ')
                # Sorting direction.
                function = input('\nIngrese 1 para orden descendente\no 2 para ascendente: ')
                if function == '1':
                    function = 'greater'
                elif function == '2':
                    function = 'less'
                # Column criteria for sorting.
                column = input('\nIngrese 1 para ordenar por cantidad de votos\n'
                               'o 2 para ordenar por calificación promedio: ')
                if column == '1':
                    column = 'vote_count'
                elif column == '2':
                    column = 'vote_average'
                # Type of sorting.
                algorithm = input('\nIngrese 1 para ordenar con selection sorting\n'
                                  'o 2 para ordenar con shell sorting\n'
                                  'o 3 para ordenar con insertion sorting: ')
                if algorithm == '1':
                    algorithm = 'selection'
                elif algorithm == '2':
                    algorithm = 'shell'
                elif algorithm == '3':
                    algorithm = 'insertion'
                # Show results.
                order_movies(function, details_list, req, algorithm, column)
            elif int(inputs[0]) == 6:  # opcion 6
                director = input('Ingrese el nombre del director para conocer su trabajo:\n')
                counter, average = know_director(director, details_list, casting_list)
                print('Existen', counter, 'películas del director', director, 'en el catálogo')
                print('Las películas de este director tienen un promedio de votación de', average, 'puntos.')
            elif int(inputs[0]) == 7: # Opción 7 
                actor = input('Ingrese el nombre del actor:\n')
                counter, average, colaboracion = know_actor(actor, details_list, casting_list)
                print('Existen', counter, 'películas del actor', actor, 'en el catálogo')
                print('Las películas de este actor tienen un promedio de votación de', average, 'puntos.')
                print('Con el director que más ha colaborado ha sido:',colaboracion)
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == '__main__':
    main()
