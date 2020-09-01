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


def loadMovies (archivoPeliculas):
    lst = loadCSVFile(archivoPeliculas, compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadCasting (archivoCasting):
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
    archivo=loadMovies(archivoPeliculas)
    for i in range(1,lt.size(archivo)):
        elemento=lt.getElement(archivo,i)
        modelo.agregarPelicula_1(catalogo, elemento)
        ID=int(elemento["id"])
        modelo.agregarApuntador(catalogo, ID, elemento)

def cargarDirectores(catalogo, archivoCasting):
    """
    Carga director al catalogo
    """
    archivo=loadCasting(archivoCasting)
    print("Cargando datos a catalogos")
    for i in range(1,lt.size(archivo)):
        linea=lt.getElement(archivo,i)
        nombreDirector= linea["director_name"]    #se obtiene director de cada pelicula
        ref= int(linea["id"])
        comp=lt.newList('SINGLE_LINKED',modelo.compIDpelicula)
        for k in range(1,lt.size(catalogo["apuntadorSegunId"])):
            dicc=lt.getElement(catalogo["apuntadorSegunId"],k)
            ids=int(dicc["ID"])                           #obtiene lista de ids de catalogo
            lt.addLast(comp,ids)
        pos=lt.isPresent(comp, ref)              #compara si la referencia se encuentra en el catalogo
        apuntador=lt.getElement(catalogo["apuntadorSegunId"],pos)
        modelo.agregarDirector(catalogo, nombreDirector, apuntador)
    print("Catalogos cargados correctamente")

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

