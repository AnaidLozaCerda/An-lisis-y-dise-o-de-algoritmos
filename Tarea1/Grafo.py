#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:38:45 2017

Representación y manipulación de grafo

@author: anaid
"""

import random
class Grafo():
    grafo={}
    def conexiones(self, nodo):
        conn = {}
        for arista in self.grafo.keys():
            if nodo in arista: #(arista.contains(nodo)):
                conn[arista] = self.grafo.get(arista)
        return conn

    def hijos(self, nodo):
        conn = {}
        for arista in self.grafo.keys():
            if nodo == arista[0]: #(arista.contains(nodo)):
                conn[arista] = self.grafo.get(arista)
        return conn

    def padres(self, nodo):
        conn = {}
        for arista in self.grafo.keys():
            if nodo == arista[1]: #(arista.contains(nodo)):
                conn[arista] = self.grafo.get(arista)
        return conn

    def minCapacidad(self):
        menor = None
        for item in self.grafo:
            if(menor == None or self.grafo.get(item)["capacidad"] < self.grafo.get(menor)["capacidad"] and self.grafo.get(item)["capacidad"] != None):
                menor = item
        return {menor: self.grafo.get(menor)}

    def minPeso(self):
        menor = None
        for item in self.grafo:
            if(menor == None or self.grafo.get(item)["peso"] < self.grafo.get(menor)["peso"] and self.grafo.get(item)["peso"] != None):
                menor = item
        #return {menor: self.grafo.get(menor)}
        return self.grafo.key()
    
    def getGrafo(self):
        return self.grafo

    def agregarArista(self, nodoA, nodoB):
        self.grafo[(nodoA, nodoB)] = {"capacidad": None, "peso": None}
        
    # Agrega tambien el peso y la capacidad
    def agregarAristaC(self, nodoA, nodoB, capacidad, peso):
         self.grafo[(nodoA, nodoB)]={"capacidad": capacidad, "peso": peso}
         

    # Cargar un grafo que se encuentra en un archivo
    ### Mejora que se pueda decidir si elgrafo puede tener nodos conectados a si mismos
    ### Mejora 2 que guarde el grafo en un txt
    def cargarGrafo(self, filename ):
        file_object = open(filename, "r")
        for line in file_object:
            if line[0] == "p":
                arreglo = line.split(" ")
                n = arreglo[2] #nodos
               # m = arreglo[3] #aristas
            elif line[0] == "e":
                n=line.split(" ")
                if(len(n) == 5):
                    self.grafo[(n[1],n[2])]={"peso":n[3], "capacidad":n[4]}
                elif(len(n) == 4):
                    self.grafo[(n[1],n[2])]={"peso":n[3], "capacidad": None}
                else:
                    self.grafo[(n[1],n[2])]={"peso":None, "capacidad": None}
    
    
    def cargarGrafoRandom(self, nNodos, nAristas, pesoMax):
        #archivo= open(nombreArchivo, "w+")
        g=Grafo()
        for i in range(nAristas):
            g.agregarArista(random.randrint(1,nNodos),random.randrange(1,nNodos),random.randrange(1,pesoMax))
        return g

       



a = Grafo()
#print a.conexiones(3)
#print a.hijos(3)
#print a.padres(3)

a.agregar_nodo(1, 4)
print a.grafo
print a.minimo_peso()
        
