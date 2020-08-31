import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from App import reto as rt

from time import process_time 

def conocer_genero(genero,lst1):
    t1_start = process_time()
    mlst =[]
    avg = 0
    iterator = it.newIterator(lst1)
    while it.hasNext(iterator):
        elemento = it.next(iterator)
        if genero in elemento["genres"]:
            mlst.append(elemento['original_title'])
            avg += float(elemento['vote_count'])
    respuesta = {"Genre Movies":mlst, "Number of Movies":len(mlst), "Average Rating": round(avg/len(mlst),2)}
    t1_stop = process_time()         
    print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
    return(respuesta)



