import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from App import reto as rt

from time import process_time 

def conocer_actor(actor,lst1,lst2):
    t1_start = process_time()
    lstid= []
    mlist = []
    avg = 0
    ddict={}
    iterator = it.newIterator(lst2)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if actor == element["actor1_name"] or actor == element["actor2_name"] or actor == element["actor3_name"] or actor == element["actor4_name"] or actor == element["actor5_name"]:
            lstid.append(element['id'])
            if element["director_name"] in ddict.keys():
                ddict[element["director_name"]] += 1

            else:
                ddict[element["director_name"]] = 1
            

    iterator2 = it.newIterator(lst1)
    while it.hasNext(iterator2):
        element2 = it.next(iterator2)
        if element2['id'] in lstid:
            mlist.append(element2["original_title"])
            avg += float(element2["vote_average"])
    mayor = 0
    dmayor = ""
    for key in ddict:
        if ddict[key]>mayor:
            mayor = ddict[key]
            dmayor = key 
        
    respuesta = {"Actor Movies":mlist, "Number of Movies":len(mlist), "Average Rating": round(avg/len(mlist),2), "Favourite Director":dmayor}
    t1_stop = process_time()         
    print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
    return(respuesta)

