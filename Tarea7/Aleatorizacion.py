#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

Programa de aleatorizacion

@author: anaid
"""
import random

def dentro(dardos):
    dardosDentro=0
    for i in range(dardos):
        x=random.random()
        y=random.random()
        z=(x*x)+(y*y)
        if z<=1:
            dardosDentro+=1
    return dardosDentro

def calculoPI(dardosDentro, dardos):
    pi=4*dardosDentro/dardos
    
    
    
        
        