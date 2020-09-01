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

#Hacer pruebas con 20 datos!!!!
#Error total peliculas +1
#genero no puede ir vacio
#error numero de peliculas que retorna


import config as cf
import sys
import csv
import copy
import statistics 

from ADT import list as lt
from DataStructures import listiterator as it
from Sorting import mergesort as MeSo
from Sorting import shellsort as ShSo
#
# EL MEJOR INESTABLE ES SHELLSORT
# EL MEJOR ESTABLE ES MERGESORT
#
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
    print("6- Crear ranking por genero")
    print("0- Salir")


def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1

def CountFunctionMayMen (Valor1, Valor2):
    return float(Valor1['vote_count']) > float(Valor2['vote_count'])

def CountFunctionMenMay (Valor1, Valor2):
    return float(Valor1['vote_count']) < float(Valor2['vote_count'])

def AverageFunctionMayMen (Valor1, Valor2):
    return float(Valor1['vote_average']) > float(Valor2['vote_average'])

def AverageFunctionMenMay (Valor1, Valor2):
    return float(Valor1['vote_average']) < float(Valor2['vote_average'])

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

def loadMovies (indicador,MUTE=False):
    if indicador=="details":
        lst = loadCSVFile("themoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds)
    elif indicador=="casting": 
        lst = loadCSVFile("themoviesdb/MoviesCastingRaw-small.csv",compareRecordIds)
    if MUTE==False:
        print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def ConocerAUnDirector (nombredirector,lstmoviescasting,lstmoviesdetails):
    IteradorCasting = it.newIterator(lstmoviescasting)
    IDsDirector = lt.newList()
    while it.hasNext(IteradorCasting)==True:
        elemento=it.next(IteradorCasting)
        if elemento['director_name'].upper()==nombredirector.upper():
            lt.addLast(IDsDirector,elemento["id"])
    lt.addLast(IDsDirector,-1)
    IteradorDetalles = it.newIterator(lstmoviesdetails)
    IteradorID = it.newIterator(IDsDirector)
    nombresanospuntajes=lt.newList()
    numero = it.next(IteradorID)
    while it.hasNext(IteradorID):
        pelicula=it.next(IteradorDetalles)
        if pelicula["id"]==numero:
            tripla = (pelicula["title"],pelicula["release_date"][-4:],pelicula["vote_average"])
            lt.addLast(nombresanospuntajes,tripla)
            numero=it.next(IteradorID)
    lt.addLast(nombresanospuntajes,-1)
    IteradorNAP = it.newIterator(nombresanospuntajes)
    nombresanos=lt.newList()
    numeropeliculas=lt.size(nombresanospuntajes)
    ADividir=0
    while it.hasNext(IteradorNAP):
        tripla=it.next(IteradorNAP)
        if type(tripla)==tuple:
            lt.addLast(nombresanos,(tripla[0]+" ("+tripla[1]+")"))
            ADividir+=float(tripla[2])
    lt.addLast(nombresanos,-1)
    return ((nombresanos,numeropeliculas,ADividir/numeropeliculas))

def CrearRankingPeliculas(NPeliculasRanking,Criterio,TipoDeOrdenamiento,lstmoviesdetails):
    if Criterio=="COUNT" and TipoDeOrdenamiento=="ASCENDENTE": MeSo.mergesort(lstmoviesdetails,CountFunctionMenMay)
    elif Criterio=="COUNT" and TipoDeOrdenamiento=="DESCENDENTE": MeSo.mergesort(lstmoviesdetails,CountFunctionMayMen)
    elif Criterio=="AVERAGE" and TipoDeOrdenamiento=="ASCENDENTE": MeSo.mergesort(lstmoviesdetails,AverageFunctionMenMay)
    elif Criterio=="AVERAGE" and TipoDeOrdenamiento=="DESCENDENTE": MeSo.mergesort(lstmoviesdetails,AverageFunctionMayMen)
    if Criterio=="COUNT": SopaDeMacacoUmaDeliciaKKKK="vote_count"
    elif Criterio=="AVERAGE": SopaDeMacacoUmaDeliciaKKKK="vote_average"
    iterable=it.newIterator(lstmoviesdetails)
    ListaAImprimir=lt.newList()
    while int(iterable["current_node"])<(NPeliculasRanking-1):
        pelicula=it.next(iterable)
        tripla=(pelicula["title"],pelicula["release_date"][-4:],pelicula[SopaDeMacacoUmaDeliciaKKKK])
        lt.addLast(ListaAImprimir,tripla)    
    lt.addLast(ListaAImprimir,-1)
    IteradorNAP = it.newIterator(ListaAImprimir)
    nombresanos=lt.newList()
    while it.hasNext(IteradorNAP):
        tripla=it.next(IteradorNAP)
        if type(tripla)==tuple:
            lt.addLast(nombresanos,((tripla[0]+" ("+tripla[1]+")"),tripla[2]))
    lt.addLast(nombresanos,-1)
    return (nombresanos)

def CrearRankingPeliculasGenero(Genero,NPeliculasRanking,Criterio,TipoDeOrdenamiento,lstmoviesdetails):
    if Criterio=="COUNT" and TipoDeOrdenamiento=="ASCENDENTE": MeSo.mergesort(lstmoviesdetails,CountFunctionMenMay)
    elif Criterio=="COUNT" and TipoDeOrdenamiento=="DESCENDENTE": MeSo.mergesort(lstmoviesdetails,CountFunctionMayMen)
    elif Criterio=="AVERAGE" and TipoDeOrdenamiento=="ASCENDENTE": MeSo.mergesort(lstmoviesdetails,AverageFunctionMenMay)
    elif Criterio=="AVERAGE" and TipoDeOrdenamiento=="DESCENDENTE": MeSo.mergesort(lstmoviesdetails,AverageFunctionMayMen)
    if Criterio=="COUNT": SopaDeMacacoUmaDeliciaKKKK="vote_count"
    elif Criterio=="AVERAGE": SopaDeMacacoUmaDeliciaKKKK="vote_average"
    respuesta = EntenderUnGeneroCinematografico(Genero,copy.deepcopy(lstmoviesdetails))
    iteradornombres = it.newIterator(respuesta[0])
    nombre=it.next(iteradornombres)[0]
    iterable=it.newIterator(lstmoviesdetails)
    ListaAImprimir=lt.newList()
    while it.hasNext(iteradornombres)==True and it.hasNext(iterable)==True:
        pelicula=it.next(iterable)
        if pelicula["title"]==nombre:
            tripla=(pelicula["title"],pelicula["release_date"][-4:],pelicula[SopaDeMacacoUmaDeliciaKKKK])
            lt.addLast(ListaAImprimir,tripla)  
            nombre=it.next(iteradornombres)[0] 
    lt.addLast(ListaAImprimir,-1)
    IteradorNAP = it.newIterator(ListaAImprimir)
    nombresanos=lt.newList()
    while it.hasNext(IteradorNAP):
        tripla=it.next(IteradorNAP)
        if type(tripla)==tuple:
            lt.addLast(nombresanos,((tripla[0]+" ("+tripla[1]+")"),tripla[2]))
    lt.addLast(nombresanos,-1)
    return (nombresanos)

def EntenderUnGeneroCinematografico(nombregenero,lstmoviesdetails):
    Iteradordetalles = it.newIterator(lstmoviesdetails)
    PeliculasGenero = lt.newList()
    count = 0
    while it.hasNext(Iteradordetalles):
        elemento = it.next(Iteradordetalles)
        if nombregenero.title() in elemento["genres"]:
            tupla = (elemento["original_title"],elemento["release_date"][-4:])
            lt.addLast(PeliculasGenero,tupla)
            count += int(elemento["vote_count"])
    lt.addLast(PeliculasGenero,-1)
    totalpeliculas = lt.size(PeliculasGenero)
    return(PeliculasGenero,totalpeliculas,count/totalpeliculas)


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lstmoviescasting = lt.newList()
    lstmoviesdetails = lt.newList()

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lstmoviescasting = loadMovies("casting")
                lstmoviesdetails = loadMovies("details")

            elif int(inputs[0])==2: #opcion 2
                if lt.size(lstmoviesdetails)>1:
                    try:
                        NPeliculasRanking=int(input("Ingrese el numero de peliculas que quiere que muestre el ranking (min 10): "))
                        if NPeliculasRanking<10:
                            print("Error, el numero de peliculas es menor a 10")
                            raise NameError('')
                        Criterio=input("Elija un criterio entre COUNT (conteo de votos) y AVERAGE (promedio de votos): ").upper()
                        if (Criterio!="COUNT" and Criterio!="AVERAGE"):
                            print("Error, se eligio un criterio distinto a COUNT o AVERAGE")
                            raise NameError('')
                        TipoDeOrdenamiento=input("Elija un tipo de ordenamiento entre ascendente y descendente: ").upper()
                        if (TipoDeOrdenamiento!="ASCENDENTE" and TipoDeOrdenamiento!="DESCENDENTE"):
                            print("Error, se eligio un tipo de ordenamiento distinto a ascendente o descendente")
                            raise NameError('')
                        tupla = CrearRankingPeliculas(NPeliculasRanking,Criterio,TipoDeOrdenamiento,copy.deepcopy(lstmoviesdetails))
                        IteradorImprimir=it.newIterator(tupla)
                        print("\n" + "A continuacion, las mejores " + str(NPeliculasRanking) + " peliculas por " + Criterio.lower() + ", en orden " + TipoDeOrdenamiento.lower())
                        print("-------------------------------------------------------------------------------------")
                        print("", end=" "*10)
                        print("Pelicula", end=" "*62)
                        print(Criterio.capitalize())
                        print("-------------------------------------------------------------------------------------")
                        c=1
                        while it.hasNext(IteradorImprimir)==True:
                            elemento = it.next(IteradorImprimir)
                            if type(elemento)==tuple:
                                print(str(c),end=" "*(10-len(str(c))))
                                print((elemento[0]),end=" "*(70-len(elemento[0])))
                                print(elemento[1])
                                c+=1
                    except: print("ERROR")                  
                else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

            elif int(inputs[0])==3: #opcion 3 
                if lt.size(lstmoviescasting)>1 and lt.size(lstmoviesdetails)>1:
                    nombredirector=input("Por favor ingrese el nombre del director: ")
                    tripla = ConocerAUnDirector(nombredirector,copy.deepcopy(lstmoviescasting),copy.deepcopy(lstmoviesdetails))
                    nombreano = tripla[0]
                    IterableNombreAno = it.newIterator(nombreano)
                    print("\n" + "---------------------------------------------------------------")
                    print(nombredirector + " tiene las siguientes peliculas:")
                    while it.hasNext(IterableNombreAno)==True:
                        elemento = it.next(IterableNombreAno)
                        if type(elemento)==str:
                            print("          •" + elemento)
                    print("\n" + nombredirector + " tiene " + str(tripla[1]) + " peliculas en total")
                    print("El promedio en la calificacion de sus peliculas es de " + str(tripla[2]))
                else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

            elif int(inputs[0])==4: #opcion 4
                pass
                # statistics.mode( LISTAADT["elements"]))

            elif int(inputs[0])==5: #opcion 5
                if lt.size(lstmoviesdetails)>1:
                    genero = input("Por favor ingrese el nombre del Género: ")
                    respuesta = EntenderUnGeneroCinematografico(genero,copy.deepcopy(lstmoviesdetails))
                    iteradornombres = it.newIterator(respuesta[0])
                    print("\n"+"---------------------------------------------------------------")
                    print( "Las peliculas con el genero",genero,"son las siguientes :")
                    peli = it.next(iteradornombres)
                    while (it.hasNext(iteradornombres) and type(peli)==tuple):
                        print("          •"+peli[0]+" ("+peli[1]+")")
                        peli = it.next(iteradornombres)
                    print("\n"+"Del género "+genero+" hay "+str(respuesta[1])+" peliculas")
                    print("El promedio en el contador de votos del genero es de ",respuesta[2])
                else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

            elif int(inputs[0])==6: #opcion 6   
                if lt.size(lstmoviesdetails)>1:
                    try:
                        NPeliculasRanking=int(input("Ingrese el numero de peliculas que quiere que muestre el ranking (min 10): "))
                        if NPeliculasRanking<10:
                            print("Error, el numero de peliculas es menor a 10")
                            raise NameError('')
                        Criterio=input("Elija un criterio entre COUNT (conteo de votos) y AVERAGE (promedio de votos): ").upper()
                        if (Criterio!="COUNT" and Criterio!="AVERAGE"):
                            print("Error, se eligio un criterio distinto a COUNT o AVERAGE")
                            raise NameError('')
                        TipoDeOrdenamiento=input("Elija un tipo de ordenamiento entre ascendente y descendente: ").upper()
                        if (TipoDeOrdenamiento!="ASCENDENTE" and TipoDeOrdenamiento!="DESCENDENTE"):
                            print("Error, se eligio un tipo de ordenamiento distinto a ascendente o descendente")
                            raise NameError('')
                        genero = input("Por favor ingrese el nombre del genero: ")
                        tupla = CrearRankingPeliculasGenero(genero,NPeliculasRanking,Criterio,TipoDeOrdenamiento,copy.deepcopy(lstmoviesdetails))
                        IteradorImprimir=it.newIterator(tupla)
                        print("\n" + "A continuacion, las mejores " + str(NPeliculasRanking) + " peliculas por " + Criterio.lower() + ", en orden " + TipoDeOrdenamiento.lower())
                        print("-------------------------------------------------------------------------------------")
                        print("", end=" "*10)
                        print("Pelicula", end=" "*62)
                        print(Criterio.capitalize())
                        print("-------------------------------------------------------------------------------------")
                        c=1
                        while it.hasNext(IteradorImprimir)==True:
                            elemento = it.next(IteradorImprimir)
                            if type(elemento)==tuple:
                                print(str(c),end=" "*(10-len(str(c))))
                                print((elemento[0]),end=" "*(70-len(elemento[0])))
                                print(elemento[1])
                                c+=1
                    except: print("ERROR")                  
                else: print("No se pudo hacer la operación, asegurese de cargar los datos primero")

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()