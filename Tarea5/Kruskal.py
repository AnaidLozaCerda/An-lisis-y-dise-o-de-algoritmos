#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

 Flujos y árboles de expansión - kruskal, alta y uniforme
 Este codigo tiene influencias del encontrado en la pagina: http://elisa.dyndns-web.com/teaching/mat/md.html que se vio en clase, la intencion de tomar este código fue para compararlo en cuanto a funcionamiento y eficacia.

@author: anaid
"""

#from Grafo import Grafo 
from time import time

#grafo=Grafo()
#grafo.cargarGrafo("instUniforme.txt")
def Kruskal2(grafo):
    tiempo_inicial = time()
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
    tiempo_final = time()
    #print('MST con peso ', peso, ' Arbol: ', arbol)
    print('Tiempo de ejecucion: ', (tiempo_final-tiempo_inicial))
    return arbol

