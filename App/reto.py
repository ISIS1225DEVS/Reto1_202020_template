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
from Sorting import shellsort as sh 

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
    lst = loadCSVFile("App\SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def less_count( self, element1, element2):
    if int(element1['vote_count']) <  int(element2['vote_count']):
        return True
    return False


def less_average( self, element1, element2):
    if int(element1['vote_average']) <  int(element2['vote_average']):
        return True
    return False

def greater_count(self, element1, element2):
    if int(element1['vote_count']) > int(element2['vote_count']):
        return True 
    return False

def greater_average(self,element1,element2):
    if int(element1['vote_average']) > int(element1['vote_average']):
        return True 
    return False


def crear_ranking_peliculas(tipo_de_ordenamiento,cantidad_elementos:int,orden):
    lista_peliculas = loadMovies()
    lista_resultado = lt.newList('SINGLE_LINKED',None)

    if tipo_de_ordenamiento == "vote_average":
        if orden == 'ascendente':
            sorting = sh.shellSort(lista_peliculas,greater_average)
        elif orden == 'descendente':
            sorting = sh.shellSort(lista_peliculas,less_average)
    elif tipo_de_ordenamiento == 'vote_count':
        if orden == 'ascendente':
            sorting = sh.shellSort(lista_peliculas,greater_count)
        elif orden == 'descendente':
            sorting = sh.shellSort(lista_peliculas,less_count)
    contador = 1
    while contador <= cantidad_elementos:
        lt.addFirst(lista_resultado,lt.getElement(lista_peliculas,contador))
        contador += 1 
    return lista_resultado


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

                ordenamiento = str(input("Ingrese el criterio de ordenamiento: " ))
                elementos = int(input("Ingrese la cantidad de elementos que desea ver: " ))
                tipo_orden = str(input("Ingrese el tipo de orden: 'ascendente o descendente': "))
                crear_ranking_peliculas(ordenamiento,elementos,tipo_orden)
                pass

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()