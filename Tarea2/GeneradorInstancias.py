#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:40:24 2017

Generador de instancias para grafos de 10 nodos. 
Genera instancias para el problema del agente viajero. Considerando que el agente puede viajar desde cualquier ciudad a cualquier ciudad.
Se considera que el costo de ir de la ciudad A a la ciudad B es el mismo que ir de la ciudad B a la ciudad A

@author: anaid
"""
import random 


matriz=[]

def validate(n1, n2):
    if n1==n2:
        return True
    elif matriz.get(n1)==n2:    
        return True
    elif matriz.get(n2)==n1:
        return True
    else:
        return False4


'''
def grafo():
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
'''



def main():
    archivo = open("instancias.txt", "w+")
    n=int(input("Cuantas ciudades desea agregar?: "))
    #n = random.randint(2,10)
    #m = random.randint(n-1, n*(n-1))
    
    archivo.writelines("c Esto es un archivo con instancias para grafos. \np did "+ str(n) +"\n")
    
    for n1 in range(0, n):
        #m = random.randint(1, n-1)
        for n2 in range(0,n):
            #n2=random.randint(1,n)
            #while n1 == n2 :
            #    n2=random.randint(1,n)
            
            if n1 >= n2:
                continue
            
            a="e "+ str(n1)+" "+str(n2)+" "+str(random.randint(0, 100))+" "+str(random.randint(0,100))+"\n" 
            archivo.writelines(a)


    archivo.close()
    
if __name__ == "__main__":
    main()
    