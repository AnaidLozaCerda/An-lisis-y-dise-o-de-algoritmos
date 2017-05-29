#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 02:01:07 2017Created on Sun May 21 23:25:00 2017

@author: anaid
"""
import grafo
#grafo={(3,1,2,4):[(1,3,2,4),(3,2,1,4),(3,1,4,2)],(1,3,2,4):[(3,1,2,4),(1,2,3,4),(1,3,4,2)],(3,2,1,4):[(2,3,1,4),(3,1,2,4),(3,2,4,1)],(3,1,4,2):[(1,3,4,2),(3,4,1,2),(3,1,2,4)]}

grafo=Grafo.nuevoArbolPuzleLineal((3,1,2,4))

def BFS(grafo, solucion):
    encontrado=False
    nVisitados=[]
    nSiguientes=[]
    camino=[]
    nSiguientes.append(grafo.keys()[0])
    while not encontrado and len(nSiguientes)!=0:
        #print "frontera: " + str(nSiguientes)
        nodo=nSiguientes.pop(0)
        #print "despues del pop nodo: "+ str(nodo) + "=="+ str(solucion) +" solucion " + str(nodo==solucion)
        if nodo == solucion:
        #    print "nodo: "+ str(nodo) + " solucion: " + str(solucion)
            encontrado=True
            camino.append(nodo)
            while grafo[nodo]>0:
            #    print "encontrado: " + str(encontrado)
                return nVisitados
        else:
#            print "nodo: "+ str(nodo)
#            print "Hijos: " + str(grafo.get(nodo))
#            print "Entrara al if? "+ str(nodo not in nVisitados)
            if grafo.get(nodo) > 0 and nodo not in nVisitados:
#                print "nodo "+ str(grafo.get(nodo))+" ya visitado?"+ str((grafo.get(nodo)) not in nVisitados)
#                print "Frontera "
#                print (nFrontera)
                nSiguientes+=grafo.get(nodo)
        
        
        nVisitados.append(nodo)
#        print "visitados: " + str(nVisitados)
    
    
    return "No se encontro"


# Rompe Cabezas Lineal con DFS
BFS(grafo, (1,2,3,4))




def DFS(grafo, solucion):
    encontrado=False
    nVisitados=[]
    nSiguientes=grafo.keys()[0]
    nSiguientes.append()
    while not encontrado and len(nSiguientes)!=0:
        nodo=nSiguientes.pop(0)
        if nodo == solucion:
            encontrado=True
            return nVisitados
        else:
            if nodo[] > 0 and nodo not in nVisitados:
                nSiguientes+=grafo.get(nodo)
        
        
        nVisitados.append(nodo)
#        print "visitados: " + str(nVisitados)
    
    
    return "No se encontro"