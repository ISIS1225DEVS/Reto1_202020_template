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
import controlador

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 

#======================
#   Ruta archivos
#======================

archivoPeliculas="theMoviesdb/SmallMoviesDetailsCleaned.csv"
archivoCasting="theMoviesdb/MoviesCastingRaw-small.csv"

#==========================
#     funciones print
#==========================

def printDatosDirector(director, puntaje):
    """
    Imprime datos directo particular
    """
    if director:
        print("Director encontrado: " + director["nombre"])
        print("Promedio: " + str(puntaje))
        print("Total peliculas: "+ str(lt.size(director["ref_peliculas"])))
        Lista = (director["ref_peliculas"])
        iterator = it.newIterator(Lista)
        while it.hasNext(iterator):
            diccionarioID=it.next(iterator)
            llave=diccionarioID["pelicula"]
            for i in range(1):
                datos=lt.getElement(llave,i)
                titulo=datos["original_title"]
                print("Titulo: "+ titulo)
    else:
        print("No encontro director")



#==========================
#     menu principal
#==========================


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
                print("Iniciando catalogo")
                cont=controlador.iniciarCatalogo()
                print("Cargando datos")
                controlador.cargarDatos(cont, archivoPeliculas, archivoCasting)

            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                nombreDirector = input("Ingrese nombre director: ")
                infoDirector=controlador.obtenerPeliculasPorDirector(cont, nombreDirector)
                puntaje= controlador.promedioDirector(cont, nombreDirector)
                printDatosDirector(infoDirector, puntaje)

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