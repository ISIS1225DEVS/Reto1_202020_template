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
    lst = loadCSVFile(archivoCasting ,compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def cargarDatos(catalogo, archivoPeliculas, archivoCasting):
    """
    Carga datos desde archivos csv al modelo
    """
    cargarPeliculas_1(catalogo, archivoPeliculas)
    cargarDirectores(catalogo, archivoCasting)

def cargarPeliculas_1(catalogo, archivoPeliculas):
    """
    Carga datos de peliculas al catalogo bajo la lista de peliculas_1
    Crea apuntador que relaciona ID con datos de pelicula
    """
    archivo=loadMovies()
    for pelicula in archivo:
        modelo.agregarPelicula_1(catalogo, pelicula)
        ID=pelicula["id"]
        modelo.agregarApuntador(catalogo, ID, pelicula)

def cargarDirectores(catalogo, archivoCasting):
    """
    Carga director al catalogo
    """
    archivo=loadCasting()
    for pelicula in archivo:
        nombreDirector= pelicula["director_name"]    #se obtiene director de cada pelicula
        ref= pelicula["id"]                     #se obtiene id de cada peilcula en casting
        ids=catalogo["apuntadorSegunId"]        #obtiene lista de ids de catalogo
        pos=lt.isPresent(ids, ref)              #compara si la referencia se encuentra en el catalogo
        if pos >0:
            apuntador=lt.getElement(ids, pos)       #linea datos pelicula
        else:
            print("error")

        modelo.agregarDirector(catalogo, nombreDirector, apuntador)


#==============================
#     Funciones para consultas
#==============================

def obtenerPeliculasPorDirector(catalogo, nombreDirector):
    """
    retorna peliculas de un director
    """
    infoDirector=modelo.obtenerPeliculasDirector(catalogo, nombreDirector)
    return infoDirector

def promedioDirector(catalogo, nombreDirector):
    """
    retorno puntaje promedio de un director
    """

    puntaje=modelo.directorAverage(catalogo, nombreDirector)
    return puntaje

