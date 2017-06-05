#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

@author: anaid
"""
from heapq import merge

grafo = {   (1, 2): 7,
            (1, 4): 5,
            (2, 4): 9,
            (2, 3): 8,
            (2, 5): 7,
            (3, 5): 5,
            (4, 5):15,
            (4, 6): 6,
            (5, 6): 8,
            (5, 7): 9,
            (6, 7):11
        }

#Este debe estar en tu objeto Grafo, es del del peso
def menor(grafo):
    w = None
    nodo = None
    for i in grafo:
        if w==None or grafo.get(i) < w:
            w = grafo.get(i)
            nodo = i
    return nodo

#Auxiliar de Kruskal para buscar en los arboles
def buscar_arbol(nodo, forest):
    for tree in forest:
        for arista in tree:
            if nodo in arista:
                return tree


def kruskal(grafo, forest = []):
    peso = 0
    while len(grafo) > 0: #Aqui obtener el tamaño del grafo actual
        nodo_menor = menor(grafo) #Aqui obtener la arista de menor peso
        del grafo[nodo_menor] #Eliminar la arista del arbol
        tree1 = buscar_arbol(nodo_menor[0], forest)
        tree2 = buscar_arbol(nodo_menor[1], forest)
        if(tree1 == None or tree2 == None or tree1 != tree2):
            if tree1 in forest:
                forest.remove(tree1)
            else:
                tree1 = []
            if tree2 in forest:
                forest.remove(tree2)
            else:
                tree2 = []
            forest.append(list(merge(tree1, tree2, [nodo_menor])))
            peso = peso + grafo.get(nodo_menor) #Aqui Obtener peso
    for arbol in forest:
        for nodo in arbol:
            if(nodo[0] == nodo[1]):
                arbol.remove(nodo)
    return forest

print kruskal(grafo)
#print buscar_arbol(1, forest)