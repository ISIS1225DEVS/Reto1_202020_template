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



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Encontrar buenas peliculas")
    print("3- Ranking de peliculas")
    print("4- Conocer un director")
    print("5- Conocer un actor")
    print("6- Entender un genero")
    print("7- Crear ranking")
    print("0- Salir")
    

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile_1 (file, cmpfunction):
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


def loadMovies_1 ():
    lst = loadCSVFile_1("themoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    print(lst) 


def loadCSVFile2 (file, sep=";"):
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def comparacion_promedio_mayor(elemento1,elemento2):
    return elemento1[1]["Promedio"]>elemento2[1]["Promedio"]

def comparacion_promedio_menor(elemento1,elemento2):
    return elemento1[1]["Promedio"]<elemento2[1]["Promedio"]

def comparacion_contar_mayor(elemento1,elemento2):
    return elemento1[1]["Votos"]>elemento2[1]["Votos"]

def comparacion_contar_menor(elemento1,elemento2):
    return elemento1[1]["Votos"]<elemento2[1]["Votos"]


def reqerimiento_1(nombre_director, lista_casting, lista_estadisticas):
    peliculas_buenas = 0
    promedio = 0
    lista_id = lt.newList()
    for posicion in range(1, lt.size(lista_casting)):
        linea_casting = lt.getElement(lista, posicion)
        if linea_casting['director_name'] == nombre_director:
            id = linea['id']
            linea_estadisticas = lt.getElement(lista_estadisticas, posicion)
            if linea_estadisticas['id'] == id:
                promedio += float(linea_estadisticas['vote_average'])
                peliculas_buenas += 1
    return (peliculas_buenas, round((promedio/peliculas_buenas), 2))

 
def Requerimiento2(numero, parametro, orden,lista):
    lista_retorno=lt.newList(datastructure="SINGLE_LINKED")
    contador1=0
    peliculas=[]
    while contador1<numero:
        mayor=0
        menor=99999999999
        titulo=""
        if parametro=="promedio" and orden=="mayor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_average"])>mayor and actual["title"] not in peliculas:
                        mayor=float(actual["vote_average"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Promedio":mayor}])
            peliculas.append(titulo)
            contador1+=1
        if parametro=="contar" and orden=="mayor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_count"])>mayor and actual["title"] not in peliculas:
                        mayor=float(actual["vote_count"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Votos":mayor}])
            peliculas.append(titulo)
            contador1+=1
        if parametro=="promedio" and orden=="menor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_average"])<menor and actual["title"] not in peliculas:
                        menor=float(actual["vote_average"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Promedio":menor}])
            peliculas.append(titulo)
            contador1+=1
        if parametro=="contar" and orden=="menor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_count"])<menor and actual["title"] not in peliculas:
                        menor=float(actual["vote_count"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Votos":menor}])
            peliculas.append(titulo)
            contador1+=1

    if parametro=="promedio" and orden=="mayor":
        lt.shell(lista_retorno,comparacion_promedio_mayor)
    if parametro=="promedio" and orden=="menor":
        lt.shell(lista_retorno,comparacion_promedio_menor)
    if parametro=="contar" and orden=="mayor":
        lt.shell(lista_retorno,comparacion_contar_mayor)
    if parametro=="contar" and orden=="menor":
        lt.shell(lista_retorno,comparacion_contar_menor)

    return print(lista_retorno)

def req3 (criteria,column,lst,lst1):
    if lst["type"]=="SINGLE_LINKED":
        t1_start = process_time()
        dic="no hay peliculas que cumplan con este criterio"
        indi=0
        pos=0
        prev = None
        idlst=[]
        lstfinal=[]
        prom=0
        pose=[]
        current=lst1['first']
        while pos < lst1["size"]:
            prev = current
            if current["info"][column].lower()==criteria.lower():
                idlst.append(int(current["info"]["id"]))
                pose.append(pos)
            current=current["next"]
            pos+=1
        pos=0
        current=lst["first"]
        while pos < lst["size"] and indi < len(idlst):
            prev=current
            if int(current["info"]["id"])==idlst[indi]:
                indi+=1
                lstfinal.append(current["info"]["original_title"])
                prom+=float(current["info"]["vote_average"])
            current=current["next"]
            pos+=1
        prom=prom/len(idlst)
        prom=(prom//0.1)/10
        dic={"lista":lstfinal,"size":len(idlst),"promedio":prom}
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    else:
        t1_start = process_time()
        lstfinal=[]
        pos=[]
        prom=0
        for i in range(1,lt.size(lst1)+1):
            if lt.getElement(lst1,i)[column].lower()==criteria.lower():
                pos.append(i)
        for a in pos:
            lstfinal.append(lt.getElement(lst,a)["original_title"])
            prom+=float(lt.getElement(lst,a)["vote_average"])
        prom=(prom//0.1)/(10*len(pos))
        dic={"lista":lstfinal,"size":len(pos),"promedio":prom}
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return(dic)


def Requerimiento_4(nombre_actor,lista_casting,lista_estadisticas):
        lista_peliculas = lt.newList()
        numero_peliculas = 0
        promedio_calificacion = 0
        director_mas_colaboraciones = [] #Contador
        cuenta_colaboraciones = [] #Contador
        for posicion in range(lt.size(lista)):
            linea_casting = lt.getElement(lista_casting, posicion)
            linea_estadisticas = lt.getElement(lista_estadisticas, posicion)
            if (linea_casting['actor1_name'] == nombre_actor) or (linea_casting['actor2_name'] == nombre_actor) or (linea_casting['actor3_name'] == nombre_actor) or (linea_casting['actor4_name'] == nombre_actor) or (linea_casting['actor5_name'] == nombre_actor):
                lt.addLast(lista_peliculas, lista_estadisticas['original_title'])
                numero_peliculas += 1
                promedio_calificacion += float(linea['vote_average'])
                if linea_casting['director_name'] not in director_mas_colaboraciones:
                    director_mas_colaboraciones.append(linea['director_name'])
                    cuenta_colaboraciones.append(1)
                else:
                    ubicacion_director = director_mas_colaboraciones.index(linea['director_name'])
                    cuenta_colaboraciones[ubicacion_director] += 1
        mas_colaboraciones = director_mas_colaboraciones[cuenta_colaboraciones.index(max(cuenta_colaboraciones))]
        return (lista_peliculas,numero_peliculas, round((promedio_calificacion / numero_peliculas),2), mas_colaboraciones)


def req5(criteria,lst):
    if lst["type"]=="SINGLE_LINKED":
        t1_start = process_time()
        dic={}
        pos=0
        lstfinal=[]
        prom=0
        current=lst['first']
        while pos < lst["size"]:
            prev = current
            if current["info"]["genres"].lower()==criteria.lower():
                lstfinal.append(current["info"]["original_title"])
                prom+=float(current["info"]["vote_average"])
            current=current["next"]
            pos+=1
        prom=(prom//0.1)/(10*len(lstfinal))
        dic={"lista de peliculas":lstfinal,"size":len(lstfinal),"promedio":prom}
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    else:
        t1_start = process_time()
        dic={}
        lstfinal=[]
        pos=[]
        prom=0
        for i in range(1,lt.size(lst)+1):
            if lt.getElement(lst,i)["genres"].lower()==criteria.lower():
                lstfinal.append(lt.getElement(lst,i)["original_title"])
                prom+=float(lt.getElement(lst,i)["vote_average"])
        prom=(prom//0.1)/(10*len(lstfinal))
        dic={"lista de peliculas":lstfinal,"size":len(lstfinal),"promedio":prom}
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return(dic)
                

def Requerimiento6(numero, parametro, genero, orden,lista):
    lista_retorno=lt.newList(datastructure="SINGLE_LINKED")
    contador1=0
    peliculas=[]
    while contador1<numero:
        mayor=0
        menor=99999999999
        titulo=""
        if parametro=="promedio" and orden=="mayor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_average"])>mayor and actual["title"] not in peliculas and genero in actual["genres"]:
                        mayor=float(actual["vote_average"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Promedio":mayor}])
            peliculas.append(titulo)
            contador1+=1
        if parametro=="contar" and orden=="mayor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_count"])>mayor and actual["title"] not in peliculas and genero in actual["genres"]:
                        mayor=float(actual["vote_count"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Votos":mayor}])
            peliculas.append(titulo)
            contador1+=1
        if parametro=="promedio" and orden=="menor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_average"])<menor and actual["title"] not in peliculas and genero in actual["genres"]:
                        menor=float(actual["vote_average"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Promedio":menor}])
            peliculas.append(titulo)
            contador1+=1
        if parametro=="contar" and orden=="menor":
            for i in range(1,lt.size(lista)):
                actual=lt.getElement(lista,i)
                if float(actual["vote_count"])<menor and actual["title"] not in peliculas and genero in actual["genres"]:
                        menor=float(actual["vote_count"])
                        titulo=actual["title"]
            lt.addFirst(lista_retorno,[{"Película":titulo},{"Votos":menor}])
            peliculas.append(titulo)
            contador1+=1

    if parametro=="promedio" and orden=="mayor":
        lt.shell(lista_retorno,comparacion_promedio_mayor)
    if parametro=="promedio" and orden=="menor":
        lt.shell(lista_retorno,comparacion_promedio_menor)
    if parametro=="contar" and orden=="mayor":
        lt.shell(lista_retorno,comparacion_contar_mayor)
    if parametro=="contar" and orden=="menor":
        lt.shell(lista_retorno,comparacion_contar_menor)
     
    return print(lista_retorno)

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """

    lstmovies={"size":0}
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n')
         #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1

                lstmovies = loadMovies_1()
                lista2 = loadCSVFile2("Data/themoviesdb/MoviesCastingRaw-small.csv")
                print("Datos cargados", lista2['size'], "elementos cargados")

            elif int(inputs[0])==2: #requerimiento 1
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    nombre_director = input('Ingrese el nombre del director: \n')
                    print(reqerimiento_1(nombre_director,lista2,lstmovies))

            elif int(inputs[0])==3: #requerimineto 2
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    n1=int(input("Número de peliculas: \n"))
                    p1=input("contar o promedio")
                    o1=input("mayor o menor")
                    Requerimiento2(n1,p1,o1,lstmovies)


            elif int(inputs[0])==4: #requerimineto 3
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    print("buscar info de director")
                    criteria =input('Ingrese el nombre del director\n')
                    lst1=loadCSVFile("themoviesdb/AllMoviesCastingRaw.csv",compareRecordIds)
                    respuesta=req3(criteria,"director_name",lstmovies,lst1) #filtrar una columna por criterio  
                    print(respuesta)
                 
            
            elif int(inputs[0])==5: #requerimineto 4
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    nombre_actor = input('Ingrese el nombre del actor: \n')
                    print(Requerimiento_4(nombre_actor,lista2,lstmovies))
                    

            elif int(inputs[0])==6: #requerimineto 5
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    print("entender un genero")
                    criteria=input("ingrese el genero: \n")
                    respuesta=req5(criteria,lstmovies)
                    print(respuesta)


            elif int(inputs[0])==7: #requerimineto 6
                if lstmovies==None or lstmovies['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    n2=int(input("Número de peliculas: \n"))
                    p2=input("contar o promedio \n")
                    o2=input("mayor o menor \n")
                    gen=input("¿Genero? (primera letra en mayúscula) \n")
                    Requerimiento6(n2,p2,gen,o2,lstmovies)                


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
    