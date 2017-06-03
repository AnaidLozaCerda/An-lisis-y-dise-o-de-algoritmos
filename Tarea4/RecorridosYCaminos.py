#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 02:01:07 2017Created on Sun May 21 23:25:00 2017

@author: anaid
"""


def metodo(solucion,etapa):
	n = 8
	reinas = []
	if etapa < n:
		while True:
			if (solucion[etapa] < n):
				solucion[etapa] = solucion[etapa] + 1
			if (validar(solucion,etapa)):
				if etapa == n-1:
					etiqueta = "ABCDEFGHIJKLM"
					for x in range(0,n):
						reinas.append(str(etiqueta[solucion[x] - 1]) + str(x))
				else:
					reinas = metodo(solucion, etapa+1)
					if len(reinas)==0:
						solucion[etapa+1] = 0
			if (solucion[etapa]==n or len(reinas)):
				break
	return reinas


def validar(solucion,etapa):
	for i in range(etapa):
		if(solucion[i] == solucion[etapa]) or (abs(solucion[i] - solucion[etapa])==abs(i - etapa)):
			return False
	return True



solucion = []
for i in range(0,8):
	solucion.append(0)
etapa = 0
print metodo(solucion, etapa)

'''


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
    '''