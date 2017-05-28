#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:40:24 2017

@author: anaid
"""
import random 


matriz={}

def validate(n1, n2):
    if n1==n2:
        return True
    elif matriz.get(n1)==n2:
        return True
    elif matriz.get(n2)==n1:
        return True
    else:
        return False


def main():
    archivo = open("instancias.txt", "w+")     
    n = 100 # random.randint(2,10)
    m = random.randint(n-1, n*(n-1))
    
    archivo.writelines("c Esto es un archivo con instancias para grafos. \np did "+ str(n) +" "+ str(m)+"\n")
    
    for i in range(m):
        n1=random.randint(1,n)
        n2=random.randint(1,n)
        while validate(n1,n2) :
            n1=random.randint(1,n)
            n2=random.randint(1,n)
        
        matriz[n1]=n2        
        a="e "+ str(n1)+" "+str(n2)+" "+str(random.randint(0, 100))+" "+str(random.randint(0,100))+"\n" 
        
        archivo.writelines(a)


    archivo.close()
    
if __name__ == "__main__":
    main()
    