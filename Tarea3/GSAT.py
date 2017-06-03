#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:25:00 2017

@author: anaid
"""
import random
from copy import copy

class GSAT():
    collector = []
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
                if rule < 0:
                    counter += self.negar(choises[abs(rule) - 1])
                else:
                    counter += choises[abs(rule) - 1]
            if(counter == 0):
                return False
        return True
    
    
    def solve(self,clausules, choises):
        if(self.validate(clausules, choises)):
            return choises
        else:
            solution = None
            for n in range(0, len(choises)):
                c2 = copy(choises)
                c2[n] = self.negar(c2[n])
                if(self.valid(c2)):
                    solution = self.solve(clausules, c2)
                    if(solution != None):
                        break
            return solution
    
    #Metodo main
    def __init__(self, clausules):
        nx = len(clausules[0])
        x = []
        for i in range(0, nx):
            x.append(random.choice([0, 1]))
        print self.solve(clausules, x)





clausules = [[-1, 2, 3], [-1, 3, -2], [-3, -2, 1]]
gsat=GSAT(clausules)
