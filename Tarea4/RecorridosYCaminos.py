#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 02:01:07 2017Created on Sun May 21 23:25:00 2017

Problema de las n reinas, resuelto por DFS y BFS

@author: anaid
"""

from copy import deepcopy

#Retorna una lista con las cassillas en que se puede colocar la reina en esa fila
def cassillasValidas(n, fila, current):
    validas = []
    for i in range(0, n):
        validas.append(i)
    for reina in current:
        #Remover la fila de la reina
        if reina[0] in validas:
            validas.remove(reina[0])
        #Remover la celda que la reina toca en diagonal en la fila acutal
        derReina = reina[0] + (fila - reina[1]) #Columna de la reina + (Fila actual - Fila de la reina)
        if derReina in validas:
            validas.remove(derReina)
        izqReina = reina[0] - (fila - reina[1]) #Columna de la reina - (Fila actual - Fila de la reina)
        if izqReina in validas:
            validas.remove(izqReina)
    return validas

def DFS(n, fila, current):
    result = None
    if(fila < n):
        lista = cassillasValidas(n, fila, current)
        if(len(lista) > 0):
            for i in lista:
                nueva_lista = deepcopy(current)
                nueva_lista.append([i, fila])
                result = DFS(n, fila+1, nueva_lista)
                if(result != None):
                    break

    else:
        result = current
    return result

def BFS(n, fila, current):
    result = None
    if(fila == 0):
        lista = cassillasValidas(n, fila, current)
        for i in lista:
            current.append([[i, fila]])
    if fila < (n - 1):
        nueva_lista = []
        for respuesta in current:
            lista = cassillasValidas(n, fila+1, respuesta)
            if(len(lista) > 0):
                for i in lista:
                    nueva_respuesta = deepcopy(respuesta)
                    nueva_respuesta.append([i, fila+1])
                    nueva_lista.append(nueva_respuesta)
        if(len(nueva_lista) > 0):
            result = BFS(n, fila+1, nueva_lista)
    else:
        for respuesta in current:
            if(len(respuesta) == n):
                result = respuesta
                break
    return result

print DFS(8, 0, [])
print BFS(8, 0, [])
