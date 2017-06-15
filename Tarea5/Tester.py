#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

@author: anaid
"""

import random
from Grafo import Grafo
from KruskalUA import kruskal
from Kruskal import Kruskal2

def genUniforme(n):
    archivo = open("instUniforme.txt", "w")
    count=0.0
    archivo.writelines("c Esto es un archivo con instancias para grafos. \np did "+ str(n) +"\n")
    
    for n1 in range(0, n):
        for n2 in range(0,n):
            if n1 >= n2:
                continue
            a="e "+ str(n1)+" "+str(n2)+" "+str(random.uniform(0, 300))+"\n" 
            count+=1.0
            archivo.writelines(a)
    archivo.writelines("c El grafo tiene un grado de coneccividad de: "+ str(count/((n*(n-1))/2)))
    archivo.close()
    
genUniforme(30)
print "Test con 30 instansias"
grafo=Grafo()
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 1: "
kruskal(grafo)
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 2: "
Kruskal2(grafo)



genUniforme(80)
print "Test con 80 instansias"
grafo=Grafo()
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 1: "
kruskal(grafo)
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 2: "
Kruskal2(grafo)


genUniforme(100)
print "Test con 100 instansias"
grafo=Grafo()
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 1: "
kruskal(grafo)
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 2: "
Kruskal2(grafo)


genUniforme(150)
print "Test con 150 instansias"
grafo=Grafo()
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 1: "
kruskal(grafo)
grafo.cargarGrafo("instUniforme.txt")
print "Kruskal 2: "
Kruskal2(grafo)

