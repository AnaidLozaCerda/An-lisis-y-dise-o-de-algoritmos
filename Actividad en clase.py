#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 14:13:26 2017

@author: anaid
"""

import random
from copy import deepcopy
#grafo=((1,2),(1,4),(1,5),(4,5)(4.6))

grafo = [(1, 3), (2, 3), (2, 4), (3, 4), (4, 6), (5, 6)]
 
cand = deepcopy(grafo)
arbol = set()
peso = 0
comp = dict()
 
while len(cand) > 0:
    #arista = min(cand.keys(), key = (lambda k: cand[k]))
    arista = random.choice(cand)
    cand.remove(arista) # se consideran una sola vez
    for i in cand:
        (u, v) = arista  
        cand.index(u)
        
  
    c = comp.get(v, {v})
    if u not in c:
        arbol.add(arista)
        peso += grafo[arista]
        nuevo = c.union(comp.get(u, {u}))
        for w in nuevo:
            comp[w] = nuevo  