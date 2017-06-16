#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

Programa de aleatorización, donde siempre se obtendran respuestas factibles aun que no se asegura que sean optimos 

@author: anaid
"""


datos = {(1, 2) : 4, (1, 3) : 5, (1, 4) : 5, (1, 5) : 6,
         (2, 3) : 5, (2, 4) : 9, (2, 5) : 5,
         (3, 4) : 1, (3, 5) : 7,
         (4, 5) : 3}
ciudades = 5

import random
#
ciudad1 = random.randint(1, ciudades)
ciudad2 = random.randint(1, ciudades)
while ciudad1 == ciudad2:
    ciudad2 = random.randint(1, ciudades)
#
def get_recorrido(ciudad_inicial, recorrido, datos, total):
    recorrido.append(ciudad_inicial)
    if(len(recorrido) == total):
        #Si ya se completo la cadena regresar
        return recorrido
    else:
        #Si no se a completado el recorrido Encontrar ciudad cercana a la inicial
        menor = None
        next_ciudad = None
        for conexion in datos:
            if ciudad_inicial in conexion:
                next_option = None
                if(conexion[0] == ciudad_inicial):
                    next_option = conexion[1]
                else:
                    next_option = conexion[0]
                if next_option not in recorrido:
                    if menor == None or menor > datos[conexion]:
                        menor = datos[conexion]
                        next_ciudad = next_option
        return get_recorrido(next_ciudad, recorrido, datos, total)

#
recorrido1 = get_recorrido(ciudad1, [], datos, ciudades)
recorrido2 = get_recorrido(ciudad2, [], datos, ciudades)

print "padres"
print recorrido1
print recorrido2

#Cruza genetica, seleccionamos un punto medio para partir
particion = ciudades / 2

hijo1 = recorrido1[:particion] + recorrido2[particion:]
hijo2 = recorrido2[:particion] + recorrido1[particion:]

print "hijos"
print hijo1
print hijo2

#Reemplazar repetidos
def no_repetir(hijo):
    not_include = []
    for i in range(1, ciudades + 1):
        if i not in hijo:
            not_include.append(i)
    if(len(not_include) > 0):
        counter = []
        for i in range(0, ciudades):
            if hijo[i] in counter:
                hijo[i] = not_include[0]
                not_include.pop(0)
            counter.append(hijo[i])
    return hijo

hijo1 = no_repetir(hijo1)
hijo2 = no_repetir(hijo2)

print "hijos (sin repetidos)"
print hijo1
print hijo2


#seleccionar los cromosomas a mutar en el hijo 1
cromosoma1 = random.randint(0, ciudades -1)
cromosoma2 = random.randint(0, ciudades -1)
while cromosoma1 == cromosoma2:
    cromosoma2 = random.randint(0, ciudades -1)

aux = hijo1[cromosoma1]
hijo1[cromosoma1] = hijo1[cromosoma2]
hijo1[cromosoma2] = aux

#seleccionar los cromosomas a mutar en el hijo 2
cromosoma1 = random.randint(0, ciudades -1)
cromosoma2 = random.randint(0, ciudades -1)
while cromosoma1 == cromosoma2:
    cromosoma2 = random.randint(0, ciudades -1)

aux = hijo2[cromosoma1]
hijo2[cromosoma1] = hijo2[cromosoma2]
hijo2[cromosoma2] = aux

print "hijos mutados"
print hijo1
print hijo2


#Buscar el de la ruta mas corta
ruta1 = 0
for i in range(0, ciudades - 1):
    if(hijo1[i] < hijo1[i+1]):
        ruta1 = ruta1 + datos[(hijo1[i], hijo1[i+1])]
    else:
        ruta1 = ruta1 + datos[(hijo1[i+1], hijo1[i])]


ruta2 = 0
for i in range(0, ciudades - 1):
    if(hijo2[i] < hijo2[i+1]):
        ruta2 = ruta2 + datos[(hijo2[i], hijo2[i+1])]
    else:
        ruta2 = ruta2 + datos[(hijo2[i+1], hijo2[i])]

#Mostrar solucion
print "Solucion:"
if ruta1 < ruta2:
    print hijo1
    print "Costo:"
    print ruta1
else:
    print hijo2
    print "Costo:"
    print ruta2




















