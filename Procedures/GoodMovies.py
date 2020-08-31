import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from App import reto as rt

from time import process_time 

#Buenas Peliculas#
def good_movies(director):
    t1_start = process_time()
    lst1 = rt.loadMovies
    lst2 = rt.loadMovies2
    goodlst = []
    avg = 0
    for row in range(1, lt.size(lst1)):
        if float(lst1[row]["vote_average"])>=6.0 and lst2[row]["director_name"] == director:
            goodlst.append(lst1[row]["original_title"])
            avg += float(lst1[row]["vote_average"])
    respuesta = {"Good Movies":goodlst, "Number of Movies":len(goodlst), "Average Vote": avg/len(goodlst)}
    t1_stop = process_time()         
    print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
    return(respuesta)






    