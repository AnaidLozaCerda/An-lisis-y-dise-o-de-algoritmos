def reader( filename ):
    file_object = open(filename, "r")
    matriz = []
    line_counter = 0
    for line in file_object:
        if line[0] == "c":
            title = line[2:];#Subcadena desde el caracter 2 hasta el final
        elif line[0] == "p":
            arreglo = line.split(" ")
            n = arreglo[2] #Columnas
            m = int(arreglo[3]) #Filas
        else:
            linea_matriz = line.split(" ")
            matriz.append([])
            for value in range(0, int(n)-1):
                matriz[line_counter].append(int(linea_matriz[value]))
            line_counter += 1
    return {'matriz':matriz, 'titulo':title, 'variables':m  ,'clausulas':n}



#Ejemplo de uso
#result = reader("instancia.txt")
#print result["titulo"]
#print result["matriz"]
