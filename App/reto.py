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
from time import process_time 

ar = "ARRAY_LIST"

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
        with open(  cf.data_dir + file, encoding="utf-8-sig") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    lst = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds)
    #lst = loadCSVFile("theMoviesdb/AllMoviesDetailsCleaned.csv",compareRecordIds)

    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting ():
    lst = loadCSVFile("theMoviesdb/MoviesCastingRaw-small.csv",compareRecordIds)
    #lst = loadCSVFile("theMoviesdb/AllMoviesCastingRaw.csv",compareRecordIds)

    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def lessAverageMovie(elemento1,elemento2):
    """Método que devuelve True si el elemento 1 es menor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_AVERAGE)"""

    return elemento1["vote_average"]<elemento2["vote_average"]

def greaterAverageMovie(elemento1,elemento2):

    """Método que devuelve True si el elemento 1 es mayor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_AVERAGE)"""

    return elemento1["vote_average"]>elemento2["vote_average"]

def lessCountMovie(elemento1,elemento2):
    """Método que devuelve True si el elemento 1 es menor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_COUNT)"""

    return elemento1["vote_count"]<elemento2["vote_count"]

def greaterCountMovie(elemento1,elemento2):
    """Método que devuelve True si el elemento 1 es mayor que el elemento 2. Devuelve falso de lo contrario
        (Trabaja con la llave VOTE_COUNT)"""

    return elemento1["vote_count"]>elemento2["vote_count"]


def requerimiento_b(lst,count, sortingPreference, sortingOrder):
    if sortingPreference == "votos" and sortingOrder == "menor":
        lt.ordenamiento_shell(lst,lessCountMovie)
    elif sortingPreference == "votos" and sortingOrder == "mayor":
        lt.ordenamiento_shell(lst,greaterCountMovie)
    elif sortingPreference == "calificación" or sortingPreference == "calificacion" and sortingOrder == "menor":
        lt.ordenamiento_shell(lst,lessAverageMovie)
    elif sortingPreference == "calificación" or sortingPreference == "calificacion" and sortingOrder == "mayor":
        lt.ordenamiento_shell(lst,greaterAverageMovie)

    resultado = lt.newList("ARRAY_LIST") 
    for i in range(1,count+1):

        pelicula = lt.getElement(lst,i)
        lt.addLast(resultado,pelicula['title'])
    
    print('Su ranking es:',resultado['elements'])

def findRelation(name,lst):
    lstSearching = lt.newList(ar)
    for i in range(1,lt.size(lst)):
        casting = lt.getElement(lst,i)
        if casting['director_name'] == name:
            lt.addLast(lstSearching,casting['id'])
    return lstSearching


def meetDirector(name,lst1,lst2):
    lstIds=findRelation(name,lst1)
    lstMovies = lt.newList(ar)
    plus = 0
    for i in range(1,lt.size(lstIds)+1):
        ids = lt.getElement(lstIds,i)
        for j in range(1,lt.size(lst2)):
            data = lt.getElement(lst2,j)
            if data['id']==ids:
                lt.addLast(lstMovies,data['title'])
                vote_average = data['vote_average']
                plus += float(vote_average)
    average= plus/lt.size(lstIds)
    print('La lista de películas es:', lstMovies['elements'])
    print('El promedio de calificación total de las películas es:',round(average,2))
    print('La cantidad de películas dirigidas por el director es:',lt.size(lstIds))

"""Implementación requerimiento 4"""
def info_actor(lst,lst_b,n_actor):

    lista=[]
    lista_directores = []

    #Encontar id y directores correspondientes al actor
    for i in range(1,(lt.size(lst))-1):
        if (lt.getElement(lst,i))["actor1_name"] == n_actor:
            pelicula = lt.getElement(lst,i)["id"]
            director = lt.getElement(lst,i)["director_name"]
            lista.append(pelicula)
            lista_directores.append(director)            
        elif (lt.getElement(lst,i))["actor2_name"] == n_actor:
              pelicula = lt.getElement(lst,i)["id"]
              director = lt.getElement(lst,i)["director_name"]
              lista.append(pelicula)
              lista_directores.append(director)
        elif (lt.getElement(lst,i))["actor3_name"] == n_actor:
               pelicula = lt.getElement(lst,i)["id"]
               director = lt.getElement(lst,i)["director_name"]
               lista.append(pelicula)
               lista_directores.append(director)
        elif (lt.getElement(lst,i))["actor4_name"] == n_actor:
               pelicula = lt.getElement(lst,i)["id"]
               director = lt.getElement(lst,i)["director_name"]
               lista.append(pelicula)
               lista_directores.append(director)
        elif (lt.getElement(lst,i))["actor5_name"] == n_actor:
               pelicula = lt.getElement(lst,i)["id"]
               director = lt.getElement(lst,i)["director_name"]
               lista.append(pelicula)
               lista_directores.append(director)
        else:            
             None
    #Si no halló al actor, detiene la función
    if len(lista) == 0:
        print("No se ha encontrado el actor requerido")       
        return -1

    #hallo promedio de votación
    else:
        peliculas_del_actor = lt.newList('ARRAY_LIST')
        promedio = 0.0
        contador = 0   
        contador_d = 0           
        for i in lista:        
            for g in range(1,(lt.size(lst_b))-1):
                if lt.getElement(lst_b,g)["id"] == i:
                    lt.addLast(peliculas_del_actor,(lt.getElement(lst_b,g)["title"]))
                    promedio += float(lt.getElement(lst_b,g)["vote_average"])
                    contador += 1
                else:
                    None
        promedio = round((promedio/contador),2)
        
        #Hallo el director más recurrente
        lista_mayor = []
        for i in lista_directores:
            lista_mayor.append(lista_directores.count(i))        
        director_resultado =max(lista_mayor)
        director_más_recurrente = ""
        
        #Imprimo los resultados
        print("\n")
        print(n_actor + " ha trabajado en: " + str(contador) + " peliculas. \n")
        print("Las peliculas en las que ha participado " + n_actor + " son: ")
        print(peliculas_del_actor["elements"])
        print("\n")
        print("El promedio de la calificación de las películas en las que ha participado " + n_actor + " es: " + str(promedio) + "\n")
        if director_resultado == 1:
            director_más_recurrente = "Este actor ha trabajado solo 1 vez con cada director"
        else:
            for i in lista_directores:
                if lista_directores.count(i)==director_resultado:
                    director_más_recurrente = ("El director más recurrente con este actor es: " + i)
        print(director_más_recurrente)

def searchGenre(genre,lst):
    lstFinal=lt.newList('ARRAY_LIST')
    suma=0
    
    for i in range(1,lt.size(lst)+1):
        movie = lt.getElement(lst,i)
        if genre in movie["genres"].split("|"):
          lt.addLast(lstFinal,movie['title'])
          suma+=float(movie["vote_count"])
   
    tamanio =lt.size(lstFinal) 
    promedio=round(float(suma/(tamanio)),2) if tamanio > 0 else 0 
    return (lstFinal,tamanio,promedio)















def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    lstmovies = lt.newList('ARRAY_LIST')
    lstCasting = lt.newList(ar)
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmovies = loadMovies()
                lstCasting = loadCasting()
            elif int(inputs[0])==2: #opcion 2
                if lstmovies==None or lt.size(lstmovies)==0: #Comprobar que la lista no esté vacía
                    print('La lista está vacía.')
                else:
                    asking = True
                    moviesNumber = input("Ingrese el número de películas que quiere tener en su ranking: ")
                    problem = "El número de películas debe ser mayor o igual a diez (10)"
                    while asking:
                        if int(moviesNumber) < 10:
                            print(problem)
                            moviesNumber = input("Ingrese el número de películas que quiere tener en su ranking: ")      
                        else:
                            asking = False
                            sortingPreference = input("- Digite 'votos' si desea ordenar su ranking por cantidad de votos.\n- Digite 'calificacion' si desea ordenar su rankin por calificación promedio.\n")
                            sortingOrder = input("- Digite 'menor' si desea ordenar su ranking de menor a mayor.\n- Digite 'mayor' si desea ordenar su ranking de mayor a menor.\n")
                            nuevo = requerimiento_b(lstmovies,int(moviesNumber), sortingPreference.lower(), sortingOrder.lower())

            elif int(inputs[0])==3: #opcion 3
                if lstmovies==None or lt.size(lstmovies)==0 or lstCasting==None or lt.size(lstCasting)==0: #Comprobar que la lista no esté vacía
                    print('La lista está vacía.')
                else:
                    directorToSearch = input("Ingrese el nombre del director que desea conocer: ")
                    meetDirector(directorToSearch,lstCasting,lstmovies)

            elif int(inputs[0])==4: #opcion 4
                 if lstmovies==None or lt.size(lstmovies)==0 or lstCasting==None or lt.size(lstCasting)==0: #Comprobar que la lista no esté vacía
                    print('La lista está vacía.')
                 else:
                     nombre_actor = input("Ingrese el nombre del actor del cual quiere información: ")
                     nombre_actor = nombre_actor
                     info_actor(lstCasting,lstmovies,nombre_actor)


                

            elif int(inputs[0])==5: #opcion 5
                if lstmovies==None or lt.size(lstmovies)==0 :
                    print("Lista vacia")
                else:
                    genero=input("Ingrese el genero que desea buscar: ")
                    resultados=searchGenre(genero,lstmovies)
                    if lt.size(resultados[0])==0:
                        print("No existen peliculas con ese genero ")
                    else:
                        print("La lista de peliculas es: "+str(resultados[0]))
                        print("La cantidad de peliculas es: "+str(resultados[1]))
                        print("El promedio de votacion del genero es: "+str(resultados[2]))



            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()