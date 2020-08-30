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
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting():
    lstCasting= loadCSVFile("theMoviesdb/MoviesCastingRaw-small.csv", compareRecordIds)
    print("Datos cargados, " + str(lt.size(lstCasting))+ "elementos cargados")
    return lstCasting


def unir_listas(lista_a:list, lista_b:list)->list:
    union_listas = lt.newList('SINGLE_LINKED', None)

    iter1 = it.newIterator(lista_a)
    while it.hasNext(iter1):
        d = it.next(iter1)

        iter2 = it.newIterator(lista_b)
        while it.hasNext(iter2):
            c = it.next(iter2)

            if not "id" in d:
                print(d)

            if d["id"] == c["id"]:
                union_d_con_c = {**d, **c}
                lt.addFirst(union_listas, union_d_con_c)
                break
    return(union_listas)

def conocer_director (director:str)->list:
    
    casting = lt.newList('SINGLE_LINKED', None)
    # casting_file = "Data/MoviesCastingRaw-small.csv" 
    casting_file = "Data/theMoviesdb/MoviesCastingRaw-small.csv"
    with open(casting_file, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lt.addFirst(casting, row)

    details = lt.newList('SINGLE_LINKED', None)
    # details_file = "Data/SmallMoviesDetailsCleaned.csv" 
    details_file = "Data/theMoviesdb/SmallMoviesDetailsCleaned.csv"
    with open(details_file, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lt.addFirst(details, row)

    
    details_pelis= lt.newList('SINGLE_LINKED', None)
    pelis_por_director = lt.newList('SINGLE_LINKED', None)

    iter = it.newIterator(casting)
    while it.hasNext(iter):
        c = it.next(iter)
        if c['director_name'] == director:
            lt.addFirst(pelis_por_director, c)
            iter = it.newIterator(details)
            while it.hasNext(iter):
                d = it.next(iter)
                if d["id"]==c["id"]:
                    lt.addFirst(details_pelis, d)  
        
    
    lista_final= unir_listas(details_pelis, pelis_por_director)
           
    numero_de_peliculas_director = lt.size(lista_final)
    suma_vote_average = 0.0
    
    iter = it.newIterator(lista_final)
    while it.hasNext(iter):
        u = it.next(iter)
        suma_vote_average = suma_vote_average + float(u["vote_average"])
        vote_average_pelicula=u['vote_average']
        vote_count=u['vote_count']
        id_peli=u['id']
    
    promedio_peliculas = 0
    if(numero_de_peliculas_director > 0):
        promedio_peliculas = suma_vote_average/numero_de_peliculas_director

    resp=("Pelicula," +"\t"+"Director,"+"\t"+ "Vote_average,"+"\t"+"vote_count"+"\n"+\
        "------------------------------------------------------------"+"\n"+\
            "P"+str(id_peli)+"\t"+"\t"+str(director)+"\t"+"\t"+str(vote_average_pelicula)+"\t"+"\t"+str(vote_count)+"\n"+"\n"\
            +"Numero de peliculas: "+ str(numero_de_peliculas_director)+"\n"+ \
            "Promedio peliculas (vote_average): "+ str(promedio_peliculas))
    
    return(resp)

def conocer_actor (actor:str)->list:
    
    casting = lt.newList('SINGLE_LINKED', None)
    # casting_file = "Data/MoviesCastingRaw-small.csv" 
    casting_file = "Data/theMoviesdb/MoviesCastingRaw-small.csv"
    with open(casting_file, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lt.addFirst(casting, row)

    details = lt.newList('SINGLE_LINKED', None)
    # details_file = "Data/SmallMoviesDetailsCleaned.csv" 
    details_file = "Data/theMoviesdb/SmallMoviesDetailsCleaned.csv"
    with open(details_file, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lt.addFirst(details, row)

    
    details_pelis= lt.newList('SINGLE_LINKED', None)
    pelis_por_actor = lt.newList('SINGLE_LINKED', None)

    iter = it.newIterator(casting)
    while it.hasNext(iter):
        c = it.next(iter)
        if c["actor1_name"] == actor or c["actor2_name"] == actor or \
            c["actor3_name"] == actor or c["actor4_name"] == actor \
            or c["actor5_name"] == actor:
            lt.addFirst(pelis_por_actor, c)
            iter = it.newIterator(details)
            while it.hasNext(iter):
                d = it.next(iter)
                if d["id"]==c["id"]:
                    lt.addFirst(details_pelis, d)  
        
    
    lista_final= unir_listas(details_pelis, pelis_por_actor)
           
    numero_de_peliculas_actor = lt.size(lista_final)
    suma_vote_average = 0.0
    
    iter = it.newIterator(lista_final)
    while it.hasNext(iter):
        u = it.next(iter)
        suma_vote_average = suma_vote_average + float(u["vote_average"])
        vote_average_pelicula=u['vote_average']
        vote_count=u['vote_count']
        id_peli=u['id']
    
    promedio_peliculas = 0
    if(numero_de_peliculas_actor > 0):
        promedio_peliculas = suma_vote_average/numero_de_peliculas_actor

    resp=("Pelicula," +"\t"+"Actor,"+"\t"+ "\t"+"\t"+ "Vote_average"+"\t"+"\t"+"vote_count"+"\n"+\
        "-------------------------------------------------------------------------"+"\n"+\
            "P"+str(id_peli)+"\t"+"\t"+str(actor)+"\t"+"\t"+str(vote_average_pelicula)+"\t"+"\t"+"\t"+str(vote_count)+"\n"+"\n"\
            +"Numero de peliculas: "+ str(numero_de_peliculas_actor)+"\n"+ \
            "Promedio peliculas (vote_average): "+ str(promedio_peliculas))
    
    return(resp)
          


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
                lstMovies = loadMovies()
                lstCasting= loadCasting()

            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                if lstMovies==None or lt.size(lstMovies)==0 or lstCasting==None or lt.size(lstCasting)==0:
                    print ("Hubo un error imprimiendo los resultados")
                else:
                    director= input("Ingrese el director:\n")
                    resp= conocer_director(director)
                    print(resp)
                pass

            elif int(inputs[0])==4: #opcion 4
                if lstMovies==None or lt.size(lstMovies)==0 or lstCasting==None or lt.size(lstCasting)==0:
                    print ("Hubo un error imprimiendo los resultados")
                else:
                    actor= input("Ingrese el actor:\n")
                    resp= conocer_actor(actor)
                    print(resp)
                
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()

