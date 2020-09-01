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
<<<<<<< HEAD
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

=======
    details= loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(details)) + " elementos cargados")
    return details

def loadCasting():
    casting= loadCSVFile("theMoviesdb/MoviesCastingRaw-small.csv", compareRecordIds)
    print("Datos cargados, " + str(lt.size(casting))+ "elementos cargados")
    return casting


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

def conocer_director (director:str, casting:list, details:list)->list:
       
    details_pelis= lt.newList('SINGLE_LINKED', None)
    pelis_por_director = lt.newList('SINGLE_LINKED', None)

    
    t1_start = process_time()

    iter_casting = it.newIterator(casting)
    while it.hasNext(iter_casting):
        c = it.next(iter_casting)
        if c['director_name'] == director:
            lt.addFirst(pelis_por_director, c)
            iter_details= it.newIterator(details)
            while it.hasNext(iter_details):
                d = it.next(iter_details)
                if d["id"]==c["id"]:
                    lt.addFirst(details_pelis, d)  
        
    
    lista_final= unir_listas(details_pelis, pelis_por_director)
           
    numero_de_peliculas_director = lt.size(lista_final)
    suma_vote_average = 0.0
    
    iter_final = it.newIterator(lista_final)
    print (("Pelicula," +"\t"+"Director,"+"\t"+ "Vote_average,"+"\t"+"vote_count"+"\n"+\
        "------------------------------------------------------------"))
        
    while it.hasNext(iter_final):
        u = it.next(iter_final)
        suma_vote_average = suma_vote_average + float(u["vote_average"])
        vote_average_pelicula=u['vote_average']
        vote_count=u['vote_count']
        id_peli=u['id']
        
        print("P"+str(id_peli)+"\t"+"\t"+str(director)+"\t"+str(vote_average_pelicula)+"\t"+"\t"+str(vote_count))
    print("\n")    

    promedio_peliculas = 0
    if(numero_de_peliculas_director > 0):
        promedio_peliculas = suma_vote_average/numero_de_peliculas_director
        print("Numero de peliculas: "+ str(numero_de_peliculas_director)+"\n"+ \
            "Promedio peliculas (vote_average): "+ str(promedio_peliculas)+"\n")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos") 

    
    return ()

def conocer_actor (actor:str, casting:list, details:list)->list:
    
    details_pelis= lt.newList('SINGLE_LINKED', None)
    pelis_por_actor = lt.newList('SINGLE_LINKED', None)

    t1_start = process_time()

    iter_casting = it.newIterator(casting)
    while it.hasNext(iter_casting):
        c = it.next(iter_casting)
        if c["actor1_name"] == actor or c["actor2_name"] == actor or \
            c["actor3_name"] == actor or c["actor4_name"] == actor \
            or c["actor5_name"] == actor:
            lt.addFirst(pelis_por_actor, c)
            iter_details= it.newIterator(details)
            while it.hasNext(iter_details):
                d = it.next(iter_details)
                if d["id"]==c["id"]:
                    lt.addFirst(details_pelis, d)  

    
    lista_final= unir_listas(details_pelis, pelis_por_actor)
           
    numero_de_peliculas_actor = lt.size(lista_final)
    suma_vote_average = 0.0
    
    mayor=0
    i=0
    dict_dir={}
    iter_final= it.newIterator(lista_final)
    print (("Pelicula," +"\t"+"Director,"+"\t"+ "Vote_average,"+"\n"+\
        "------------------------------------------------------------"))
    while it.hasNext(iter_final):
        u = it.next(iter_final)
        suma_vote_average = suma_vote_average + float(u["vote_average"])
        vote_average_pelicula=u['vote_average']
        vote_count=u['vote_count']
        director=u["director_name"]
        id_peli=u['id']
        print("P"+str(id_peli)+"\t"+"\t"+str(director)+"\t"+str(vote_average_pelicula))

        dire= u['director_name'] 
        if dire not in dict_dir:
            dict_dir[dire]=1
        elif dire in dict_dir:
            dict_dir[dire]+=1

    print("\n")
    director_mas_colaboraciones = max(dict_dir, key=dict_dir.get) 
        
   
    promedio_peliculas = 0
    if(numero_de_peliculas_actor > 0):
        promedio_peliculas = suma_vote_average/numero_de_peliculas_actor
        print("Numero de peliculas: "+ str(numero_de_peliculas_actor)+"\n"+ \
            "Promedio peliculas (vote_average): "+ str(promedio_peliculas)+"\n"+\
                "Director con más colaboraciones: "+ str(director_mas_colaboraciones)+"\n")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos") 

    return ()
>>>>>>> 0b1008cd698ca785189c3202df83af36000e5511

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

                ordenamiento = str(input("Ingrese el criterio de ordenamiento: " ))
                elementos = int(input("Ingrese la cantidad de elementos que desea ver: " ))
                tipo_orden = str(input("Ingrese el tipo de orden: 'ascendente o descendente': "))
                crear_ranking_peliculas(ordenamiento,elementos,tipo_orden)
                pass

            elif int(inputs[0])==3: #opcion 3
                if lstMovies==None or lt.size(lstMovies)==0 or lstCasting==None or lt.size(lstCasting)==0:
                    print ("Hubo un error imprimiendo los resultados")
                else:
                    director= input("Ingrese el director:\n")
                    resp= conocer_director(director, lstCasting, lstMovies)
                    print(resp)
                pass

            elif int(inputs[0])==4: #opcion 4
                if lstMovies==None or lt.size(lstMovies)==0 or lstCasting==None or lt.size(lstCasting)==0:
                    print ("Hubo un error imprimiendo los resultados")
                else:
                    actor= input("Ingrese el actor:\n")
                    resp= conocer_actor(actor, lstCasting, lstMovies)
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

