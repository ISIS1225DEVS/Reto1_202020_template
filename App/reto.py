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

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")

def less(elemento1, elemento2, columna):
    #print("entra a less")
    if float(elemento1[columna]) < float(elemento2[columna]):
        return True
    return False

def greater(elemento1, elemento2,columna):
    #print("entra a less")
    if float(elemento1[columna]) > float(elemento2[columna]):
        return True
    return False

def comparar_director(elemento1, elemento2):
    if elemento1 == elemento2["nombre"]:
        return 0
    return 1

def comparar_actores(elemento1, elemento2):
    if elemento1 == elemento2["nombre"]:
        return 0
    return 1

def comparar_genero(elemento1, elemento2):

    if elemento1 == elemento2["genero"]:
        return 0
    return 1

def comparar_pelicula(elemento1, elemento2):

    if elemento1 == elemento2:
        return 0
    return 1

def comparar_id(elemento1, elemento2):
    if elemento1 == elemento2["id"]:
        return 0
    return 1


def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    print(lst)
    return lst


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()

            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                def cargar_directores(file, sep = ";"):
                    lst = lt.newList('SINGLE_LINKED', comparar_director) #Usando implementacion linkedlist
                    print("Cargando archivo ....")
                    t1_start = process_time() #tiempo inicial
                    dialect = csv.excel()
                    dialect.delimiter=sep
                    try:
                        with open(file, encoding="utf-8") as csvfile:
                            spamreader = csv.DictReader(csvfile, dialect=dialect)
                            for row in spamreader: 
                        
                                director = {}
                                director["nombre"] = row["director_name"]
                                posicion1 = lt.isPresent(lst, director["nombre"])
                                if posicion1 == 0:
                                    director["peliculas"] = lt.newList()
                                    lt.addLast(director["peliculas"], row["id"])
                                    lt.addLast(lst, director)
                                else:
                                    directores = lt.getElement(lst, posicion1)
                                    lt.addLast(directores["peliculas"], row["id"])
                                
                    except:
                        print("Hubo un error con la carga del archivo")
                    t1_stop = process_time() #tiempo final
                    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
                    return lst
                
                
                def cargar_peliculas (file, sep=";"):
                    lst = lt.newList('SINGLE_LINKED', comparar_id)
                    print("Cargando archivo ....")
                    #t1_start = process_time() #tiempo inicial
                    dialect = csv.excel()
                    dialect.delimiter=sep
                    try:
                        with open(file, encoding="utf-8") as csvfile:
                            spamreader = csv.DictReader(csvfile, dialect=dialect)
                            for row in spamreader: 

                                lt.addLast(lst,row)
                    except:
                        print("Hubo un error con la carga del archivo")
                    #t1_stop = process_time() #tiempo final
                    #print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
                    return lst
                
                
                lista_directores = cargar_directores(cf.data_dir+"themoviesdb/AllMoviesCastingRaw.csv")
                lista_peliculas = cargar_peliculas(cf.data_dir+"themoviesdb/AllMoviesDetailsCleaned.csv")
                print("longitud de la lista\n")

                nombre_director = input("Ingrese el nombre de un director:\n")
                pos = lt.isPresent(lista_directores, nombre_director)
                directorr=lt.getElement(lista_directores, pos)
                print("El numero de peliculas dirigidas por el director son:\n", directorr["peliculas"]["size"])
                itera = it.newIterator(directorr["peliculas"])
                average = 0
                while it.hasNext(itera):
                    elemento = it.next(itera)

                    posicion = lt.isPresent(lista_peliculas, elemento)
                    peliculas  = lt.getElement(lista_peliculas, posicion)
                    print(peliculas["original_title"])
                    average += float(peliculas["vote_average"])
                promedio = average/directorr["peliculas"]["size"] 
                print("El promedio de todas sus peliculas es:\n", promedio)

            elif int(inputs[0])==4: #opcion 4
                def cargar_listaActores(file, sep=";"):
                    lst = lt.newList('SINGLE_LINKED', comparar_actores) 
                
                    dialect = csv.excel()
                    dialect.delimiter=sep
                    nombres_actores =["actor1_name","actor2_name","actor3_name","actor4_name","actor5_name"]
                    try:
                        with open(file, encoding="utf-8") as csvfile:
                            spamreader = csv.DictReader(csvfile, dialect=dialect)
                            for row in spamreader: 
                                #print(row)

                                # agregar una lista para los directores 
                                #directores ={}
                                #directores["director"] =lt.newList('SINGLE_LINKED', comparar_directores)  #lista directores                
                                for   nombreCol in nombres_actores:                    
                                    actor = {}                    
                                    actor["nombre"] = row[nombreCol]

                                    posicion1 = lt.isPresent(lst, actor["nombre"])
                                    if posicion1 == 0:
                                        actor["peliculas"] = lt.newList()   #ids Peliculas del actor
                                        actor["director"] =lt.newList('SINGLE_LINKED', comparar_director)  #lista directores
                                    
                                        lt.addLast(actor["peliculas"], row["id"])
                                        director ={}
                                        director["nombre"] =row["director_name"]
                                        director["count"] = 1

                                        lt.addLast(actor["director"],director )
                                        

                                        lt.addLast(lst, actor)
                                    else:
                                        actores = lt.getElement(lst, posicion1)
                                        lt.addLast(actores["peliculas"], row["id"])

                                        #validra si ya esta el director o no
                                        pos_director = lt.isPresent(actores["director"],row["director_name"])

                                        if pos_director ==0:  # no esta crear director
                                            director ={}
                                            director["nombre"] = row["director_name"]
                                            director["count"] = 1

                                            lt.addLast( actores["director"],director)
                                        else:    # ya esta ese director aumnetar count en uno
                                            director = lt.getElement(actores["director"],pos_director)
                                            director["count"] = director["count"] + 1
                                
                    except:
                        print("Hubo un error con la carga del archivo")
                    return lst
                
                def cargar_peliculas (file, sep=";"):
                    lst = lt.newList('SINGLE_LINKED', comparar_id)
                    print("Cargando archivo ....")
                    #t1_start = process_time() #tiempo inicial
                    dialect = csv.excel()
                    dialect.delimiter=sep
                    try:
                        with open(file, encoding="utf-8") as csvfile:
                            spamreader = csv.DictReader(csvfile, dialect=dialect)
                            for row in spamreader: 

                                lt.addLast(lst,row)
                    except:
                        print("Hubo un error con la carga del archivo")
                    #t1_stop = process_time() #tiempo final
                    #print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
                    return lst

                listaActores =cargar_listaActores(cf.data_dir+"themoviesdb/AllMoviesCastingRaw.csv")
                listaPelicuas = cargar_peliculas(cf.data_dir+"themoviesdb/AllMoviesDetailsCleaned.csv")

                criterio=input("Nombre del actor : ")
                peliculas_por_actor(listaActores,listaPelicuas,criterio)

            elif int(inputs[0])==5: #opcion 5
                pass

            elif int(inputs[0])==6: #opcion 6

                def cargar_peliculas_por_genero(file, sep = ";"):
                    lst = lt.newList('SINGLE_LINKED', comparar_genero) #Usando implementacion linkedlist
                    print("Cargando archivo ....")
                    dialect = csv.excel()
                    dialect.delimiter=sep
    
                    with open(file, encoding="utf-8") as csvfile:
                        spamreader = csv.DictReader(csvfile, dialect=dialect)
                        for row in spamreader: 

                            generos = row['genres'].split("|")
            
                            for genero in generos:
                                elemento = {}
                                elemento["genero"] = genero

                                posicion1 = lt.isPresent(lst, elemento["genero"])
                                if posicion1 == 0: #  no esta
                                    elemento["peliculas"] = lt.newList('SINGLE_LINKED', comparar_pelicula) #lista con las peliculas por genero
                                    elemento["sum_Votos"] = int(row["vote_count"])
                                    elemento["sum_average"] = float(row["vote_average"])
                                    lt.addLast(elemento["peliculas"], row["original_title"])
                                    lt.addLast(lst, elemento)  # se adiciona a la lista de todos los elemnetos lst 
                                else:
                                    elemento_row  = lt.getElement(lst, posicion1)
                                    #revisar si la peicula ya esta 
                                    posi_peli = lt.isPresent(elemento_row['peliculas'],row["original_title"])
                                    if posi_peli == 0:
                                        lt.addLast(elemento_row["peliculas"], row["original_title"])
                                        elemento_row["sum_Votos"] += int(row["vote_count"])
                                        elemento_row["sum_average"] += float(row["vote_average"])
                
                    return lst
                
                lista_Genero = cargar_peliculas_por_genero(cf.data_dir+"themoviesdb/AllMoviesDetailsCleaned.csv")
                
                columna =  input("1. Por votos, 2. Por promedio\n")
                orden = input("1. Las Mejores , 2. Las peores\n")

                cantidad = input("Numero de peliculas a retornar\n")

                ranking_peliculas_por_genero(lista_Genero,columna,orden,cantidad)


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()