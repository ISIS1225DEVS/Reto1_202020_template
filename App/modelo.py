import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it

from time import process_time 

#================================
#      estructura catalogo
#================================


def newCatalog():
    """
    Inicia catalogo peliculas
    """
    catalogo={"peliculas_1":None, "apuntadorSegunId":None, "directores":None, "generos":None, "actores":None}
    catalogo["peliculas_1"]=lt.newList('ARRAY_LIST',compIDpelicula)
    catalogo["apuntadorSegunId"]=lt.newList('ARRAY_LIST',compIDpelicula)
    catalogo["directores"]=lt.newList("ARRAY_LIST",compDirectores)
    catalogo["generos"]=lt.newList('SINGLE_LINKED',compGenero)
    catalogo["actores"]=lt.newList("ARRAY_LIST",compActores)
    return catalogo

def nuevaEntradaPelicula(ID):
    """
    Diccionario que incluye el ID de la pelicula (desde archivo casting)y apunta a filas de esta pelicula en catalogo
    """
    pelicula={"ID":0, "pelicula":None}
    pelicula["ID"]=ID
    pelicula["pelicula"]=lt.newList("SINGLE_LINKED",compIDpelicula)
    return pelicula

def nuevoDirector(nombre):
    """
    Diccionario con nombre de director, lista con nombres de sus de peliculas y promedio de rating
    """
    director={"nombre": "","ref_peliculas":None, "puntaje_total":0.0}
    director["nombre"]=nombre
    director["ref_peliculas"]=lt.newList('ARRAY_LIST',compIDpelicula)
    return director

def nuevoGenero(nombre_genero):
    """
    diccionario con nombre del genero, lista con nombres de peliculas de este genero, y promedio de rating
    """
    genero={"nombre":"", "peliculas":None, "promedio":0}
    genero["nombre"]=nombre_genero
    genero["peliculas"]=lt.newList("SINGLE_LINKED",compGenero)


#==================================================
#   funciones para agregar datos a catalogo
#==================================================

def agregarPelicula_1(catalogo, pelicula):
    """
    Agrega una pelicula al catalogo peliculas_1
    """
    lt.addLast(catalogo["peliculas_1"], pelicula)

def agregarApuntador (catalogo, ID, pelicula_1):
    """
    Agrega apuntador a catalogo
    """
    peliculas= catalogo["apuntadorSegunId"]
    
    Identidad=nuevaEntradaPelicula(ID)
    lt.addLast(peliculas, Identidad)
    lt.addLast(Identidad["pelicula"], pelicula_1)

def agregarDirector(catalogo, nombreDirector, ID_pelicula):
    """
    Agrega director a catalogo, y lista de peliculas a su diccionario
    """
    directores= catalogo["directores"]
    nombres=lt.newList('SINGLE_LINKED',compDirectores)
    for i in range(1,lt.size(directores)):
        directo=lt.getElement(directores,i)
        nombre=directo["nombre"]
        lt.addLast(nombres,nombre)
    posibleDirector= lt.isPresent(nombres, nombreDirector)
    if posibleDirector > 0:
        director=lt.getElement(directores, posibleDirector)
    else:
        director=nuevoDirector(nombreDirector)
        lt.addLast(directores, director)
    lt.addLast(director["ref_peliculas"],ID_pelicula)           #el ID_pelicula es un diccionario
    
    pelicula=ID_pelicula["pelicula"]
    for i in range(1):
        datos=lt.getElement(pelicula,i)
        calificacion=datos["vote_average"]

    director["puntaje_total"]+=float(calificacion)

    


#==================================================
#   funciones de consulta
#==================================================

def directorAverage(catalogo, nombreDirector):
    nombres=lt.newList('SINGLE_LINKED',compDirectores)
    for i in range(1,lt.size(catalogo["directores"])):
        director=lt.getElement(catalogo["directores"],i)
        nombre=director["nombre"]
        lt.addLast(nombres,nombre)
    posibleDirector= lt.isPresent(nombres, nombreDirector)
    if posibleDirector > 0:
        directorf=lt.getElement(catalogo["directores"], posibleDirector)
    else:
        print("error, no encontro director")
    
    promedio=directorf["puntaje_total"]/lt.size(directorf["ref_peliculas"])

    return promedio

def obtenerPeliculasDirector(catalogo, nombreDirector):
    nombres=lt.newList('SINGLE_LINKED',compDirectores)
    for i in range(1,lt.size(catalogo["directores"])):
        director=lt.getElement(catalogo["directores"],i)
        nombre=director["nombre"]
        lt.addLast(nombres,nombre)

    posiciondirector=lt.isPresent(nombres, nombreDirector)

    if posiciondirector >0:
        infodirector= lt.getElement(catalogo["directores"],posiciondirector)
        return infodirector
    return None





#==================================================
#   funciones de comparacion
#==================================================

def compIDpelicula(id1,id2):
    """
    compara dos IDs de peliculas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compDirectores(nombre1, nombre2):
    """
    compara dos directores de peliculas
    """
    if (nombre1 == nombre2):
        return 0
    elif nombre1 > nombre2:
        return 1
    else:
        return -1

def compGenero(genero1, genero2):
    """
    compara dos generos distintos
    """
    if (genero1 == genero2):
        return 0
    elif genero1 > genero2:
        return 1
    else:
        return -1

def compActores(actor1, actor2):
    """
    compara dos generos distintos
    """
    if (actor1 == actor2):
        return 0
    elif actor1 > actor2:
        return 1
    else:
        return -1