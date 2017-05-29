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
    n = random.randint(2,10)
    #m = random.randint(n-1, n*(n-1))
    
    archivo.writelines("c Esto es un archivo con instancias para grafos. \np did "+ str(n) +"\n")
    
    for n1 in range(1, n):
        m = random.randint(1, n-1)
        for i in range(m):
            n2=random.randint(1,n)
            while n1 == n2 :
                n2=random.randint(1,n)
            
            if matriz.get(n1) == n2 :
                continue
            
            matriz[n1]=n2 
            matriz[n2]=n1 
            a="e "+ str(n1)+" "+str(n2)+" "+str(random.randint(0, 100))+" "+str(random.randint(0,100))+"\n" 
            
            archivo.writelines(a)


    archivo.close()
    
if __name__ == "__main__":
    main()
    