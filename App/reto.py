
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
from Sorting import mergesort as sort
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


def loadCSVFile (lst,file, sep=";"):
    dialect = csv.excel()
    dialect.delimiter=sep
    try: 
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")

def get_two_csv(file1,file2,list_type):
    list1=   lt.newList(list_type)
    list2=  lt.newList(list_type)
    lst_movies = lt.newList(list_type)
    loadCSVFile(list1,file1)
    loadCSVFile(list2,file2)
    for i in range(0,lt.size(list1)):
        tuples= (lt.getElement(list1,i),lt.getElement(list2,i))
        lt.addLast(lst_movies,tuples)


    return lst_movies

#ESTA ES LA FUNCIÓN PARA LA BÚSQUEDAD DEL DIRECTOR Y DE SUS PELÍCULAS BUENAS
#REQUERIMIENTO 1

def good_movies(lista,busqueda):
#La x mas votadas
    count=0
    sum=0
    recorrido=0
    di=0
    vot=1
    try:
        while recorrido <= lt.size(lista) :
            if lt.getElement(lista,recorrido)[di]["director_name"] == busqueda:
                vote= float(lt.getElement(lista,recorrido)[vot]['vote_average'])
                if vote >= 6:
                    count+=1
                    sum+= vote
            recorrido+=1
        return((count,sum/count))
    except:
        print("El director no fue encontrado")
    

#REQUERIMIENTO 3
def peliculas_de_un_director(list,director_name):
    size= lt.size(list)
    dirigidas= []
    numero= 0
    calificacion= 0
    for i in range(0,size):
        elem= lt.getElement(list,i)
        if elem[0]['director_name'] == director_name :
            dirigidas.append(elem[1]['original_title'])
            calificacion+= float(elem[1]['vote_average'])
            numero+=1
    if len(dirigidas) >= 1 :
        print('El director '+ director_name + ' ha dirigido ' + str(numero) + ' peliculas, y la calificacion promedio de las mismas es '+ str(round((calificacion/numero),2))+ '.' )
        print('A continuacion se listan los nombres de las peliculas')
        print(dirigidas)
    else: 
        print('El director no esta en la lista, Intente nuevamente')



#Funciones para requerimiento 2

def comparar_vote_count (movie1, movie2):
    return ( float(movie1[1]["vote_count"]) > float(movie2[1]["vote_count"]))

def comparar_vote_averange (movie1, movie2):
    return ( float(movie1[1]["vote_average"]) > float(movie2[1]["vote_average"]))


def lista_ordenada_vote_count(list):
    list_type='SINGLE_LINKED'
    lista_OrdenadaPorVotacion= lt.newList(list_type,comparar_vote_count)
    cont=0
    while cont <= lt.size(list):
        elemento=lt.getElement(list,cont)
        lt.addLast(lista_OrdenadaPorVotacion,elemento)
        cont+=1
    sort.mergesort (lista_OrdenadaPorVotacion,comparar_vote_count)
    return lista_OrdenadaPorVotacion


def obtener_peliculas_mas_votadas (list, number):
    movies = lista_ordenada_vote_count(list)
    peliculas_mas_votadas_ascendente= lt.newList()
    peliculas_mas_votadas_descendente= lt.newList()
    for cont in range (1, number+1):
        tuple1=("Id: ",lt.getElement (movies, cont)[0]["id"],"Title: ",lt.getElement (movies, cont)[1]["original_title"],"Vote_Count: ",lt.getElement (movies, cont)[1]["vote_count"]  )
        lt.addFirst (peliculas_mas_votadas_ascendente, tuple1)
        lt.addLast (peliculas_mas_votadas_descendente, tuple1)
    return (peliculas_mas_votadas_descendente,peliculas_mas_votadas_ascendente)

def obtener_peliculas_menos_votadas (list, number):
    movies = lista_ordenada_vote_count(list)
    peliculas_menos_votadas_ascendente= lt.newList()
    peliculas_menos_votadas_descendente= lt.newList()
    for cont in range (1, number+1):
        tuple1 = ("Id: ",lt.lastElement(movies)[0]["id"],"Title: ",lt.lastElement(movies)[1]["original_title"],"Vote_Count: ", lt.lastElement(movies)[1]["vote_count"])
        lt.addFirst (peliculas_menos_votadas_ascendente, tuple1)
        lt.addLast (peliculas_menos_votadas_descendente, tuple1)
        lt.removeLast(movies)
    return (peliculas_menos_votadas_descendente,peliculas_menos_votadas_ascendente)

def lista_ordenada_vote_averange(list):
    list_type='SINGLE_LINKED'
    lista_OrdenadaPorPuntajeVotacion= lt.newList(list_type)
    cont=0
    while cont <= lt.size(list):
        elemento=lt.getElement(list,cont)
        lt.addLast(lista_OrdenadaPorPuntajeVotacion,elemento)
        cont+=1
    sort.mergesort(lista_OrdenadaPorPuntajeVotacion,comparar_vote_averange)
    return lista_OrdenadaPorPuntajeVotacion


def obtener_peliculas_mejor_votadas (list, number):
    movies = lista_ordenada_vote_averange(list)
    peliculas_mejores_calificaciones_ascendente= lt.newList()
    peliculas_mejores_calificaciones_descendente= lt.newList()
    for cont in range (1, number+1):
        tuple1=("Id: ",lt.getElement (movies, cont)[0]["id"],"Title: ",lt.getElement (movies, cont)[1]["original_title"],"Vote_Averange: ",lt.getElement (movies, cont)[1]["vote_average"]  )
        lt.addFirst (peliculas_mejores_calificaciones_ascendente, tuple1)
        lt.addLast (peliculas_mejores_calificaciones_descendente, tuple1)
    return (peliculas_mejores_calificaciones_descendente,peliculas_mejores_calificaciones_ascendente)

def obtener_peliculas_peor_votadas (list, number):
    movies = lista_ordenada_vote_averange(list)
    peliculas_peor_calificadas_ascendente= lt.newList()
    peliculas_peor_calificadas_descendente= lt.newList()
    for cont in range (1, number+1):
        tuple1 = ("Id: ",lt.lastElement(movies)[0]["id"],"Title: ",lt.lastElement(movies)[1]["original_title"], "Vote_Averange: ",lt.lastElement(movies)[1]["vote_average"])        
        lt.addFirst (peliculas_peor_calificadas_ascendente, tuple1)
        lt.addLast (peliculas_peor_calificadas_descendente, tuple1)
        lt.removeLast(movies)
    return (peliculas_peor_calificadas_descendente,peliculas_peor_calificadas_ascendente)


#MENU
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
                list_type1 = 'ARRAY_LIST'
                list_type2 = 'SINGLE_LINKED'
                file1 = 'Data/theMoviesdb/MoviesCastingRaw-small.csv'
                file2 = 'Data/theMoviesdb/SmallMoviesDetailsCleaned.csv'
                lst_movies_array_list= get_two_csv(file1,file2,list_type1)
                lst_movies_single_linked= get_two_csv(file1,file2,list_type2)
                print("Datos cargados, " + str(lt.size(lst_movies_single_linked)) + " elementos cargados")

            elif int(inputs[0])==2: #opcion 2
                pass
                
                dir= input('Ingrese el nombre del Director: ')
                peliculas= good_movies(lst_movies_array_list,dir)
                print("De el director "+ dir + " se encontraron " + str(peliculas[0]) + " peliculas buenas. El promedio de la puntuación de estas películas es: " + str(peliculas[1]))

            elif int(inputs[0])==3: #opcion 3
                pass
                dir= input('Ingrese el nombre del Director: ')

                peliculas_de_un_director(lst_movies_array_list,dir)
                

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==5: #opcion 5
                pass

            elif int(inputs[0])==6: #opcion 6
                    print("1 -Ver películas más votadas en orden descendente")
                    print("2- Ver películas más votadas en orden ascendente")
                    print("3- Ver películas menos votadas en orden descendente")
                    print("4- Ver películas menos votadas en orden ascendente")
                    print("5- Ver películas mejor votadas en orden descendente")
                    print("6- Ver películas mejor votadas en orden ascendente")
                    print("7- Ver películas peor votadas en orden descendente")
                    print("8- Ver películas peor votadas en orden ascendente")
                    print("9- Volver a menú principal")

                    inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
                    if len(inputs)>0:
                        if int(inputs[0])==1: 
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas más votadas en orden descendente son:\n " + str(obtener_peliculas_mas_votadas(lst_movies_single_linked,number)[0] )  )
                        elif int(inputs[0])==2:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas más votadas en orden ascendente son:\n " + str(obtener_peliculas_mas_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==3:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas menos votadas en orden descendente son:\n " + str(obtener_peliculas_menos_votadas(lst_movies_single_linked,5)[0] ))
                        elif int(inputs[0])==4: 
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas menos votadas en orden ascendente son:\n " + str(obtener_peliculas_menos_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==5:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas mejor calificadas en orden descendente son:\n " + str(obtener_peliculas_mejor_votadas(lst_movies_single_linked,number)[0] ))
                        elif int(inputs[0])==6:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas mejor calificadas en orden ascendente son:\n " + str(obtener_peliculas_mejor_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==7:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas peor calificadas en orden descendente son:\n " + str(obtener_peliculas_peor_votadas(lst_movies_single_linked,number)[0] ))
                        elif int(inputs[0])==8:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas peor calificadas en orden ascendente son:\n " + str(obtener_peliculas_peor_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==9:       
                            printMenu() #imprimir el menu de opciones en consola
                            inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()