#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

 Flujos y árboles de expansión - kruskal, alta y uniforme, este es elc odigo desarrollado sin ninguna influencia

@author: anaid
"""
from heapq import merge
#from Grafo import Grafo
from time import time


#grafo=Grafo()
#grafo.cargarGrafo("instUniforme.txt")


#Auxiliar de Kruskal para buscar en los arboles
def buscar_arbol(nodo, forest):
    for tree in forest:
        for arista in tree:
            if nodo in arista:
                return tree


def kruskal(grafo, forest = []):
    tiempo_inicial = time()
    peso = 0
    while len(grafo.getGrafo()) > 0: #Aqui obtener el tamaño del grafo actual
        nodo_menor = grafo.minPeso() #Aqui obtener la arista de menor peso
        pesoMenor=grafo.getPeso(nodo_menor) #Aqui Obtener peso para despues
        del grafo.getGrafo()[nodo_menor] #Eliminar la arista del arbol
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
            peso = peso + pesoMenor 
    for arbol in forest:
        for nodo in arbol:
            if(nodo[0] == nodo[1]):
                arbol.remove(nodo)                
    tiempo_final = time()
    #print ('Peso: ',peso,' Arbol: ', forest)
    print ('Tiempo de ejecucion: ',(tiempo_final-tiempo_inicial))
    return forest

#print kruskal(grafo)
# kruskal(grafo)


#print buscar_arbol(1, forest)
