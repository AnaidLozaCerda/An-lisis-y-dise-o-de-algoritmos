#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:25:00 2017

@author: anaid
"""
import random
from copy import copy
from reader import reader

class GSAT():
    collector = []
    maxIter=100
    i=0
    
    def negar(self, value):
        if value == 0:
            return 1
        else:
            return 0
    
    def valid(self,choises):
        if(choises in self.collector):
            return False
        else:
            self.collector.append(choises)
            return True
    
    
    def validate(self,clausules, choises):
        for clausule in clausules:
            counter = 0
            for rule in clausule:
                if (int(rule) < 0):
                    counter += self.negar(choises[(abs(rule) - 2)])
                else:
                    counter += choises[abs(rule) - 2]
            if(counter == 0):
                return False
        return True
    
    
    def solve(self,clausules, choises):
        self.i+=1
        if(self.validate(clausules, choises) or self.i>self.maxIter):
            return choises
        else:
            solution = None
            for x in range(0, len(choises)):
                c2 = copy(choises)
                c2[x] = self.negar(c2[x])
                if(self.valid(c2)):
                    solution = self.solve(clausules, c2)
                    if(solution != None):
                        break
                else:
                    continue
            return solution
    
    #Metodo main
    def __init__(self, clausules, v):
        x = []
        for i in range(0, v):
            x.append(random.choice([0, 1]))
        print self.solve(clausules, x)




clausules = reader("instancia.txt")
#clausules = [[-1, 2, 3], [-1, 3, -2], [-3, -2, 1]]
gsat=GSAT(clausules["matriz"],clausules["variables"])
