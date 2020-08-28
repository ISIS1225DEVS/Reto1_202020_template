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
        with open( file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies (file):
    lst = loadCSVFile(file,compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def less(element1, element2, criteria):
    if float(element1[criteria]) < float(element2[criteria]):
        return True
    return False

def greater (element1,element2, criteria):
    if float(element1[criteria]) > float(element2[criteria]):
        return True
    return False

def selectionSort (lst, lessfunction, criteria,size): 
    pos1 = 1
    while pos1 < size:
        minimum = pos1              # minimun tiene el menor elemento conocido hasta ese momento
        pos2 = pos1 + 1
        while (pos2 <= lt.size(lst)):
            if (lessfunction (lt.getElement(lst, pos2),lt.getElement(lst, minimum),criteria)): 
                minimum = pos2      # minimum se actualiza con la posición del nuevo elemento más pequeño
            pos2 += 1
        lt.exchange (lst, pos1, minimum)  # se intercambia el elemento más pequeño hasta ese punto con el elemento en pos1
        pos1 += 1


def countElementsByCriteria(criteria, lst1,lst2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    lst = lt.newList()
    promedio=0
    ids=[]

    iterator = it.newIterator(lst1)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if criteria.lower() in element["director_name"].lower(): 
            ids.append(element["id"])
    
    iterator = it.newIterator(lst2)
    while  it.hasNext(iterator):
        pelicula = it.next(iterator)
        if pelicula["id"] in ids: 
            lt.addLast(lst,pelicula)
            promedio+=float(pelicula["vote_average"])
    promedio/=lst["size"]
    
    return (lst,lst["size"],promedio)

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if column == "1":
        column="vote_count"
    elif column == "2":
        column="vote_average"
    else:
        print("Valor no valido para criterio de busqueda")
    lista=lt.newList("ARRAY_LIST")
    if function.lower()=="crecimiento":
        lista_ord=selectionSort(lst,greater,column, int(elements))
    elif function.lower()=="decrecimiento":
        lista_ord=selectionSort(lst,less,column, int(elements))
    for i in range(1,(int(elements)+1)):
        lt.addLast(lista, lt.getElement(lst, i))
    return lista

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """



    lista_casting = lt.newList()   # se require usar lista definida
    lista_details = lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista_casting = loadMovies("Data/MoviesCastingRaw-small.csv") #llamar funcion cargar datos
                lista_details = loadMovies("Data/SmallMoviesDetailsCleaned.csv")
                print("Datos cargados en lista casting, ",lista_casting['size']," elementos cargados")
                print("Datos cargados en lista details, ",lista_details['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")    
                else: 
                    criteria =input('Ingrese 1 si el criterio de busqueda es COUNT o ingrese 2 si es AVERAGE\n')
                    crecimiento =input("¿Quiere la lista en crecimiento o decrecimiento?\n")
                    tamaño =input("Ingrese cuantas posiciones quiere que tenga su lista\n")
                    lista=orderElementsByCriteria(crecimiento,criteria,lista_details,tamaño)
                    print ("La lista de peliculas solicitada es:")
                    iterator = it.newIterator(lista)
                    i=1
                    while  it.hasNext(iterator):
                        element = it.next(iterator)
                        print(str(i)+"- "+element["original_title"])
                        i += 1
                    
            elif int(inputs[0])==3: #opcion 3
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")  
                else:   
                    criteria =input('Ingrese el nombre del director\n')
                    lista,counter,promedio=countElementsByCriteria(criteria,lista_casting,lista_details)
                    print ("Hay "+str(counter)+" películas buenas de ese director. Y "+str(promedio)+" es su promedio de la votacion.")
                    print("Las peliculas mejor calificadas dirigidas por " + criteria +  " son:")
                    iterator = it.newIterator(lista)
                    i=1
                    while  it.hasNext(iterator):
                        element = it.next(iterator)
                        print(str(i)+"- "+element["original_title"])
                        i += 1      
            elif int(inputs[0])==4: #opcion 4
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")
                else:
                    pass
                
            elif int(inputs[0])==5: #opcion 5
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")
                else:
                    pass
            elif int(inputs[0])==6: #opcion 6
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")
                else:
                    pass
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()