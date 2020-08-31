import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from App import reto as rt

from time import process_time 

def conocer_director(director,lst1,lst2):
    t1_start = process_time()
    lstid= []
    mlist = []
    avg = 0
    iterator = it.newIterator(lst2)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if director == element["director_name"]:
            lstid.append(element['id'])

    iterator2 = it.newIterator(lst1)
    while it.hasNext(iterator2):
        element2 = it.next(iterator2)
        if element2['id'] in lstid:
            mlist.append(element2["original_title"])
            avg += float(element2["vote_average"])
    respuesta = {"Director Movies":mlist, "Number of Movies":len(mlist), "Average Rating": round(avg/len(mlist),2)}
    t1_stop = process_time()         
    print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
    return(respuesta)