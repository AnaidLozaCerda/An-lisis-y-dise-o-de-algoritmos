#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:38:45 2017

@author: anaid
"""
#grafo = [(1, 3), (2, 3), (2, 4), (3, 4), (4, 6), (5, 6)]
grafo = {(1, 3): 4, (2, 3): 2, (2, 4): 1, (3, 4): 2, (4, 6): 1, (5, 6): 2}
#print ("Cuantos vertices contendra este grafo?")
#
import random
class Grafo():
    grafo=[]
    grafoW={}
    grafoA={}
    
    def __init__(self):
        self.grafo=[]
        self.grafoW={}
        self.grafoA={}
    
    # Se concidera que la direccion va desde el primer nodo (A) al segundo (B)
    def agregarAristaW(self, nodoA, nodoB, capacidad, peso):
        self.grafoW[(nodoA, nodoB)]={"capacidad": capacidad, "peso": peso}
 
    #Grafo dirigido sin pesos
    def agregarArista(self, nodoA, nodoB):
        self.grafo.append((nodoA, nodoB))
        
    #Se considera que la lista de nodos conectados es simple y se pueden repetir 
    #los nodos ya agregados
    # Tambien se considera que es un nodo no dirigido y sin pesos
    def aristaGrafoNoDirigido(self, nodo, ListaConectados):    
        self.grafo[(nodo)]=ListaConectados
        
    # Cargar un grafo que se encuentra en un archivo
    ### Mejora que se pueda decidir si elgrafo puede tener nodos conectados a si mismos
    ### Mejora 2 que guarde el grafo en un txt
    def cargarGrafo( filename ):
        file_object = open(filename, "r")
        grafo = {}
        for line in file_object:
            if line[0] == "p":
                arreglo = line.split(" ")
                n = arreglo[2] #nodos
               # m = arreglo[3] #aristas
            elif line[0] == "e":
                n=line.split(" ")
                grafo[(n[1],n[2])]={"capacidad":n[3], "peso":n[4]}
        return grafo
    
    # Se considera que es una raiz de 4 digitos
    # Esta parte se modifico para la tarea de Recorridos y caminos de grafos
    def nuevoArbolPuzleLineal(raiz):
        siguienteNivel=[raiz]
        grafo={}
        vistos=[]
        padre=None
        siguienteNivel.append(raiz)
        while len(siguienteNivel)!=0:
            nodo=siguienteNivel.pop[0]
            if nodo not in vistos:
                hijos=[nodo[1],nodo[0],nodo[3],nodo[4]]
                grafo[nodo]={"hijos":hijos, "padre":padre}
                vistos.append(nodo)
                if len(siguienteNivel)==0:
                    padre=nodo
                    siguienteNivel.append(hijos)
        
        #self.grafoA=grafo
        return grafo
        
    
    
    def cargarGrafoRandom(self, nNodos, nAristas, pesoMax):
        #archivo= open(nombreArchivo, "w+")
        g=Grafo()
        for i in range(nAristas):
            g.agregarAristaW(random.randrint(1,nNodos),random.randrange(1,nNodos),random.randrange(1,pesoMax))
        
    '''
    def soloNodos(self):
        self.grafo=self.grafoW.keys()
    
    def grafoNoDirigido(self):
        if len(self.grafo)<1 and len(self.grafoW)>0: soloNodos(self)
       return self.grafo
       '''
       