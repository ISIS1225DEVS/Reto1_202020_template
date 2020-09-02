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
from Sorting import shellsort as shell

from time import process_time 




def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Encontrar Buenas Peliculas")
    print("2- Rankin de Peliculas")
    print("3- Conocer a un Director")
    print("4- Conocer a un Actor")
    print("5- Entender un genero cinematografico")
    print("6- Crear Rankin del Genero")
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



def cargar_listaDirectores(file, sep=";"):
    lst = lt.newList('SINGLE_LINKED', comparar_director) 
   
    dialect = csv.excel()
    dialect.delimiter=sep
    
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                director ={}
                director["nombre"] = row["director_name"]
                posicion1 = lt.isPresent(lst, director["nombre"])

                if posicion1 ==0:
                    director["ids_peliculas"] = lt.newList()
                    lt.addLast(director["ids_peliculas"],row['id'])
                    lt.addFirst(lst,director)
                else:
                    director = lt.getElement(lst,posicion1)
                    lt.addLast(director["ids_peliculas"],row['id'])
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



def peliculas_por_director(lstDirectores,lstPelicuas,criterio):
    pos = lt.isPresent(lstDirectores,criterio)
    if pos ==0:
        print("No existe diretor")
        return None
    else:
        director = lt.getElement(lstDirectores,pos)

        listaBuenasPeliculas ={'peliculas': None, 'promedio': None }
        listaBuenasPeliculas['peliculas'] = lt.newList() 

        lista_ids = director['ids_peliculas']
        itera = it.newIterator(lista_ids)

        average = 0      
        
        while  it.hasNext(itera):
            id = it.next(itera)
            pos1 = lt.isPresent(lstPelicuas,id)
            peli = lt.getElement(lstPelicuas,pos1)                 
            if float(peli['vote_average'])>= 6:

                lt.addLast(listaBuenasPeliculas['peliculas'],peli['original_title'])
                average = average + float(peli['vote_average'])
               
        listaBuenasPeliculas['promedio'] = average

        return listaBuenasPeliculas

def encontrarRankingVoto(criterio,cantidad, columna,lst):
    #from  Sorting.insertionsort import  insertionSort
   # from  Sorting.shellsort import shellSort
    salida = lt.newList()


    if int(criterio) == 1:
        shell.shellSort1(lst,greater,columna)
    else:
        shell.shellSort1(lst,less, columna)


    itera = it.newIterator(lst)
    i =1

    while it.hasNext(itera):
        ele_salida ={}
        elemento = it.next(itera)
        ele_salida["id"] = elemento["id"]
        ele_salida["original_title"] = elemento["original_title"]
        ele_salida[columna] = elemento[columna]        
        lt.addLast(salida,ele_salida)
        i = i+1
        if i > int(cantidad):
            break     
    return salida

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

def peliculas_por_actor(listaActores,listaPeliculas,nombreActor):
    

    pos_actor = lt.isPresent(listaActores,nombreActor)
    actor = lt.getElement(listaActores,pos_actor)

    itera = it.newIterator(actor["peliculas"])
    print("Contidad de peliculas actor ",nombreActor , ": " ,actor["peliculas"]["size"],"\n")

    average = 0 
    
    while it.hasNext(itera):
        id_pelicula = it.next(itera)
        posicion = lt.isPresent(listaPeliculas, id_pelicula)
        peliculas  = lt.getElement(listaPeliculas, posicion)
        average += float(peliculas["vote_average"])
        print(peliculas["original_title"])

    promedio = average/actor["peliculas"]["size"] 
    print("El promedio de todas sus peliculas es:\n", promedio)

    #con que directores ha trabajado mas
    itera = it.newIterator(actor["director"])
    
    while it.hasNext(itera):
        diretor = it.next(itera)
        print("director ", diretor)
    
    shell.shellSort1(actor["director"],greater,"count")

    print("Director con mas colaboraciones:\n")
    print(lt.getElement(actor["director"],1))

def cargar_peliculas_genero(file, sep = ";"):
    lst = lt.newList('SINGLE_LINKED', comparar_genero) #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                generos = row['genres'].split("|")
                #print(generos)
                
                for genero in generos:
                    elemento = {}
                    elemento["genero"] = genero

                    # lst es la lista con todos los elementos
                    posicion1 = lt.isPresent(lst, elemento["genero"])
                    if posicion1 == 0: # no esta
                        elemento["peliculas"] = lt.newList('SINGLE_LINKED', comparar_pelicula) #lista con las peliculas por genero
                        elemento["sum_Votos"] = int(row["vote_count"])
                        lt.addLast(elemento["peliculas"], row["original_title"])
                        lt.addLast(lst, elemento)  # se adiciona a la lista de todos los elemnetos lst 
                    else:
                        elemento_row  = lt.getElement(lst, posicion1)
                        #revisar si la peicula ya esta 
                        posi_peli = lt.isPresent(elemento_row['peliculas'],row["original_title"])
                        if posi_peli == 0:
                            lt.addLast(elemento_row["peliculas"], row["original_title"])
                            elemento_row["sum_Votos"] +=  int(row["vote_count"])

                    
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

def peliculas_por_genero(listagenero,criterio):
   pos = lt.isPresent(listagenero,criterio)
   if pos ==0:
       print(" No se necontro este genero")
       return
   else:
        generos = lt.getElement(listagenero,pos)
        lista_peliculas = generos["peliculas"]
        itera = it.newIterator(lista_peliculas)
        print("Las Peliculas del genero ", criterio, " son:")
        while it.hasNext(itera):
            pelicula = it.next(itera)
            print(pelicula)
        print ("Numero de peliculas por genero: ", criterio, " es:",lista_peliculas['size'] )
        print ("El promedio en votos  por genero: ", criterio, " es:",generos['sum_Votos']/lista_peliculas['size']  )

def cargar_peliculas_por_genero(file, sep = ";"):
    lst = lt.newList('SINGLE_LINKED', comparar_genero) #Usando implementacion linkedlist
    print("Cargando archivo ....")
    dialect = csv.excel()
    dialect.delimiter=sep
    
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            #print(row)

            generos = row['genres'].split("|")
            #print(generos)
            
            for genero in generos:
                elemento = {}
                elemento["genero"] = genero

                # lst es la lista con todos los elementos
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

def ranking_peliculas_por_genero(listagenero,columna,orden, cantidad):
    
    columna = int(columna)
    orden= int(orden)
    cantidad = int(cantidad)

    if columna ==1 :
        colum= "sum_Votos"
        lacolumna ="vote_count"  
    else:
        colum ="sum_average"
        lacolumna ="vote_averange"

    if orden == 1: # de mayor a menor
        shell.shellSort1(listagenero,greater,colum)
        elgenero ="mejor"
    else:
        shell.shellSort1(listagenero,less,colum)
        elgenero ="peor"

    generos = lt.getElement(listagenero,1)
    
    lista_peliculas = generos["peliculas"]

    if len(generos['genero']) == 0:
        generos['genero'] = "Sin definir"

    print("El genero con ", elgenero, "ranking por ", lacolumna, " es :", generos ['genero'], "\n")
    print("las ", cantidad , "primeras  peliculas  son:")
    itera = it.newIterator(lista_peliculas)
    i =1
    while it.hasNext(itera):
        peli = it.next(itera)
        print(peli)
        if i >= cantidad:
            break
        i = i +1

    print ("Numero de peliculas por genero ", generos ['genero'], " es:",lista_peliculas['size'] )
    print("Cantida de votos: ", generos['sum_Votos'])
    print ("El promedio en votos  por genero: ", generos ['genero'], " es:",generos['sum_Votos']/lista_peliculas['size']  )
    print ("El promedio en ranking  por genero: ", generos ['genero'], " es:",generos['sum_average']/lista_peliculas['size']  )


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #Requerimiento  1
                listaDirectores =cargar_listaDirectores("Data/AllMoviesCastingRaw.csv")
                listaPelicuas = cargar_peliculas("Data/AllMoviesDetailsCleaned.csv")
                criterio=input("Nombre del Director : ")
                listapeli  =peliculas_por_director(listaDirectores,listaPelicuas,criterio)

                print("promedio ", listapeli['promedio'] / listapeli['peliculas']['size'])
                print("lista d ebuena speliculas con promedio superior a 6")
                itera = it.newIterator(listapeli['peliculas'])
                while it.hasNext(itera):
                    peli = it.next(itera)
                    print(peli)
            
            elif int(inputs[0])==2: #Requerimiento 2
                lista_peliculas = cargar_peliculas("Data/AllMoviesDetailsCleaned.csv")

                criteria =input('Ingrese el criterio de búsqueda 1 Mejor evaluadas , 2  Peor evaluadas\n')
                columna = int(input("Ingrese 1 para columna de votos o 2 para columna de promedio\n"))
                cantidad = int(input("Retornar las primeras ... "))
                if int(criteria) == 1:
                    salida = "Mejor Evaluada"
                else:
                    salida = "Peor Evaluadas"

                if columna == 1:
                    nombre_columna = "vote_count"
                else:
                    nombre_columna = "vote_average"                

                lista = encontrarRankingVoto(criteria,cantidad, nombre_columna,lista_peliculas)

                print("Ranking de peliculas ", salida , " Por columna ", nombre_columna,  " es :\n")
                itera = it.newIterator(lista)
                i = 1
                while it.hasNext(itera):
                    salida = it.next(itera)
                    print(" N.", i, " : " , salida)
                    i += 1

            elif int(inputs[0])==3: #Requerimieto  3
                lista_directores = cargar_directores("Data/AllMoviesCastingRaw.csv")
                lista_peliculas = cargar_peliculas("Data/AllMoviesDetailsCleaned.csv")
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

            elif int(inputs[0])==4: #Requerimiento  4
                listaActores =cargar_listaActores("Data/AllMoviesCastingRaw.csv")
                listaPelicuas = cargar_peliculas("Data/AllMoviesDetailsCleaned.csv")


                #print("logitud lista")
                #print(listaPelicuas["size"])

                criterio=input("Nombre del actor : ")
                peliculas_por_actor(listaActores,listaPelicuas,criterio)


            elif int(inputs[0])==5: #Requerimiento 5 

                lista_Genero = cargar_peliculas_genero("Data/AllMoviesDetailsCleaned.csv")
                print(lista_Genero['size'])

                criterio=input("Nombre del Genero : ")
                peliculas_por_genero(lista_Genero,criterio) 

         

            elif int(inputs[0])==6: #Requerimiento 6 
                lista_Genero = cargar_peliculas_por_genero("Data/AllMoviesDetailsCleaned.csv")
                #print(lista_Genero['size'])


                #pedir datos usuario


                columna =  input("1. Por votos, 2. Por promedio\n")
                orden = input("1. Las Mejores , 2. Las peores\n")

                cantidad = input("Numero de peliculas a retornar\n")

                ranking_peliculas_por_genero(lista_Genero,columna,orden,cantidad)



            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()