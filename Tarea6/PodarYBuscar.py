#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

Podar y buscar, minimum covering circle problem

@author: anaid
"""

#Inputs
y=0
points = [
    [ 1, 4],
    [ 5, 4],
    [-4, 5],
    [ 5,-9],
    [ 3,-5],
    [ 5,-7],
    [ 1,-1],
    [ 6, 7],
    [ 0,-5]
]


#Step 2 | Paso 2
def pairs_of_points(points):
    pairs = []
    for p in xrange(0, len(points), 2):
        if((p+1) != len(points)):
            pairs.append([points[p], points[p+1]])
        else:
            #Si son impares se empareja el ultimo con el primero
            pairs.append([points[p], points[0]])
    return pairs

#Step 3.1 | Paso 3.1
def equidistant_point(y, dot1, dot2):
    if(dot1[0] == dot2[0]):
        x3 = dot1[0] #Como sacar un punto equidistante en la recta a dos puntos con la misma x?
    else:
        x3 = ((2*y*(dot1[1] - dot2[1])) + pow(dot2[1], 2) - pow(dot1[1], 2) - pow(dot1[0], 2) + pow(dot2[0], 2))/(2 * (dot2[0] - dot1[0]))
    return [x3, y]

def list_equidistant(y, pairs):
    points = []
    for pair in pairs:
        points.append(equidistant_point(y, pair[0], pair[1]))
    print "equidistantes a cada pareja"
    print points #sin ordenar, cada uno esta en el orden de la lista de puntos
    return points

#Step 4 | Paso 4 Encontrar la media
def find_median(points):
    counts = (len(points))
    if(counts % 2 == 1 or (counts / 2) == 0):
        return points[counts / 2]
    else:#No aseguro este else
        p1 = points[counts / 2]
        p2 = points[(counts / 2) - 1]
        return [(p2[0] + p1[0]) / 2, p1[1]]

def distance_points(dot1, dot2):
    return pow(pow(dot2[0] - dot1[0],2) + pow(dot2[1] - dot1[1],2), 0.5)

#Step 5 | Paso 5 Localizar el mas lejano
def far_far_away(median, points):
    current = {"distance": -1, "point": None}
    for point in points:
        distance = distance_points(median, point)
        if(distance > current["distance"]):
            current["distance"] = distance;
            current["point"] = point
    return current


#Step 6 | Paso 6
def prune_list(farthest, median, pairs, equidistants):
    new_list = []
    if(farthest["point"][0] < median[0]):
        for n in range(0, len(equidistants)):
            if(equidistants[n][0] >= median[0]):
                if(distance_points(median, pairs[n][0]) > distance_points(median, pairs[n][1])):
                    new_list.append(pairs[n][1])
                else:
                    new_list.append(pairs[n][0])
            else:
                new_list.append(pairs[n][0])
                new_list.append(pairs[n][1])
    else:
        for n in range(0, len(equidistants)):
            if(equidistants[n][0] <= median[0]):
                if(distance_points(median, pairs[n][0]) > distance_points(median, pairs[n][1])):
                    new_list.append(pairs[n][1])
                else:
                    new_list.append(pairs[n][0])
            else:
                new_list.append(pairs[n][0])
                new_list.append(pairs[n][1])
    return new_list




def prune_and_search(y, points):
    print "--------------------------------------"
    print points
    print "--------------------------------------"
    if(len(points) <= 1):
        print "Ocurri\xc3 un error inesperado"
    elif(len(points) == 2):
        #Step 1 | Paso 1
        #resolver por fuerza bruta
        equidistants = list_equidistant(y, [points])
        return {"radio": distance_points(equidistants[0], points[0]), "centro": equidistants[0]}
    else:
        #Step 2 | Paso 2
        pairs = pairs_of_points(points)
        print "parejas de puntos"
        print pairs
        equidistants = list_equidistant(y, pairs)
        equidistants.sort()
        print equidistants
        median = find_median(equidistants)
        print "mediana"
        print median
        farthest = far_far_away(median, points)
        points2 = prune_list(farthest, median, pairs, list_equidistant(y, pairs))
        print "Nueva lista"
        print points2
        if(points2 == points):
            return {"radio": farthest["distance"], "centro": median}
        else:
            return prune_and_search(y, points2)



result = prune_and_search(y, points)

print(chr(27) + "[2J") #Limpiar pantalla
print "el resultado es: "
print result

#print distance(0, [1,1], [2,2]) #Prueba