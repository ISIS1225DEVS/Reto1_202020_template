import config as cf
import sys
import csv
import modelo

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 

#==============================
#     Iniciar catalogo
#==============================

def iniciarCatalogo():
    """
    Inicia catalogo vacio desde el modelo
    """
    catalogo=modelo.newCatalog()
    return catalogo

#==============================
#     Funciones para cargar datos y almacenarlos en el modelo
#==============================

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
    lst = loadCSVFile(archivoPeliculas, compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting ():
    lst = loadCSVFile("theMoviesdb/MovieCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def cargarDatos(catalogo, archivoPeliculas, archivoCasting):
    """
    Carga datos desde archivos csv al modelo
    """
    cargarPeliculas_1(catalogo, archivoPeliculas)
    cargarPeliculas_2(catalogo, archivoCasting)
    cargarDirectores(catalogo, archivoCasting)
    cargarGeneros(catalogo, archivoPeliculas)

def cargarPeliculas_1(catalogo, archivoPeliculas):
    """
    Carga datos de peliculas al catalogo bajo la lista de peliculas_1
    """
    archivo=loadMovies()
    for pelicula in archivo:
        modelo.agregarPelicula_1(catalogo, pelicula)

def cargarPeliculas_2(catalogo, archivoCasting):
    """
    Carga datos de peliculas al catalogo bajo la lista de peliculas_2
    """
    archivo=loadCasting()
    for pelicula in archivo:
        modelo.agregarPelicula_2(catalogo, pelicula)
        director= pelicula["director_name"]    #se obtiene director de cada pelicula
        ID= pelicula["id"]
        modelo.agregarDirector(catalogo, nombreDirector, ID)



