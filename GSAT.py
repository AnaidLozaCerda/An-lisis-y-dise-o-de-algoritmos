#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:25:00 2017

@author: anaid
"""
import random


class GSAT():
    x=[]

    ecuaciones=[(-1, -2, -3),(-2, 3,-4,),(-3, 2, 4)]
    verdadero=0
    sx=0
    for i in range(4):
        x.append(random.choice([0,1]))
    
    
    def switch(self, variables):
        s=abs(random.choice(variables))
        print s, self.x[s]
        if s>0: self.x[s]=0 
        else: self.x[s]=1
    '''    
    def cargarInst():
        instancias=open(instancias.txt)
        instancias.read
    '''
    
    def nuevo(self):
        self.x=[]
        self.verdadero=0
        self.sx=0
        for i in range(4):
            self.x.append(random.randint(0,1))
            print self.x
    
    
    def __init__(self):
        while self.verdadero != len(self.ecuaciones):    
            for j in range(len(self.ecuaciones)):
                for k in self.ecuaciones[j]:
                    if k < 0 :
                        self.sx+= (self.x[abs(k)-1] * -1)
                    else:
                        self.sx+= self.x[abs(k)-1]
                    
                        
                if self.sx>0: 
                    self.verdadero+=1
                    print self.ecuaciones[j]
                    self.switch(self.ecuaciones[j])
                    break
        #if s != len(ecuaciones): 
    
''' 
    def switch(self):
        s=abs(random.choice(1))
        print s, self.x[s]
        if s>0: self.x[s]=0 
        else: self.x[s]=1
'''

a = GSAT()