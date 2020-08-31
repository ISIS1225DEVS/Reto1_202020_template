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
    catalogo={"peliculas":None, "directores":None, "generos":None, "actores":None}
    catalogo["peliculas"]=lt.newList('SINGLE_LINKED',compIDpelicula)
    catalogo["directores"]=lt.newList("ARRAY_LIST",compDirectores)
    catalogo["generos"]=lt.newList('SINGLE_LINKED',compGenero)
    catalogo["actores"]=lt.newList("ARRAY_LIST",compActores)
    return catalogo

def nuevoDirector(nombre):
    """
    Diccionario con nombre de director, lista con nombres de sus de peliculas y promedio de rating
    """
    director={"nombre": "", "peliculas":None, "puntaje_total":0, "puntaje_promedio":0 }
    director["nombre"]=nombre
    director["peliculas"]=lt.newList('ARRAY_LIST',compDirectores)
    director["puntaje promedio"]=(director["puntaje_total"]/ lt.size(director["peliculas"]))
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

def agregarPelicula(catalogo, pelicula):
    """
    Agrega una pelicula al catalogo
    """
    lt.addLast(catalogo["peliculas"], pelicula)

def agregarDirector(catalogo, nombreDirector, pelicula):
    """
    Agrega director a catalogo, y lista de peliculas a su diccionario
    """
    directores= catalogo["directores"]
    posibleDirector= lt.isPresent(dierctores, nombreDirector)
    if posibleDirector >0:
        director=lt.getElement(directores, posibleDirector)
    else:
        director=nuevoDirector( nombreDirector)
    lt.addLast(director["peliculas"], pelicula)
    director["puntaje_total"]+= pelicula["vote_average"]


#==================================================
#   funciones de consulta
#==================================================








#==================================================
#   funciones de comparacion
#==================================================