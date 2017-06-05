#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

 Flujos y árboles de expansión - kruskal, alta y uniforme
 Este codigo tiene influencias del encontrado en la pagina: 

@author: anaid
"""

from Grafo import Grafo 
#import copy

grafo=Grafo()
grafo.cargarGrafo("instUniforme.txt")

#cand = deepcopy(grafo.getGrafo())
#cand=copy.copy(grafo)
arbol = set()
peso = 0.0
comp = {}

#print grafo.getGrafo().keys()
while len(grafo.getGrafo()) > 0:
    arista = grafo.minPeso()
    p=grafo.getPeso(arista)
    del grafo.getGrafo()[arista]
    (u, v) = arista
    c = comp.get(v, {v})
    if u not in c:
        arbol.add(arista)
        peso += p
        nuevo = c.union(comp.get(u, {u}))
        for w in nuevo:
            comp[w] = nuevo  


print('MST con peso', peso, 'Arbol:', arbol)

import random
def genUniforme(n):
    archivo = open("instUniforme.txt", "w+")
    n=int(input("Cuantas ciudades desea agregar?: "))
    
    archivo.writelines("c Esto es un archivo con instancias para grafos. \np did "+ str(n) +"\n")
    
    for n1 in range(0, n):
        for n2 in range(0,n):
            if n1 >= n2:
                continue
            a="e "+ str(n1)+" "+str(n2)+" "+str(random.uniform(0, 100))+"\n" 
            archivo.writelines(a)
    archivo.close()