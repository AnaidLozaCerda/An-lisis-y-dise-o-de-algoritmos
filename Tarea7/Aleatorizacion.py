#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

Programa de aleatorización, donde siempre se obtendran respuestas aleatorias aun que no siempre seran 

@author: anaid
"""

from copy import deepcopy
import random

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
        lista = cassillasValidas(n, fila, current) #Lista restringida
        while len(lista) > 0:
            i = random.choice(lista) #Seleccion aleatoria
            lista.remove(i)
            nueva_lista = deepcopy(current)
            nueva_lista.append([i, fila])
            result = DFS(n, fila+1, nueva_lista)
            if(result != None):
                break
    else:
        result = current
    return result

print DFS(8, 0, [])