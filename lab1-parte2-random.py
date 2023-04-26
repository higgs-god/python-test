import random

#funcion para crear una matriz aleatoria
def matriz_random(filas,columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(1,5) #numero aleatorio entre 1 y 5
            fila.append(elem)
        m.append(fila)
    return m 

#resta de 2 matrices
def resta_matrices(m1,m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            resta = m1[i][j] - m2[i][j]
            fila.append(resta)
        matriz_final.append(fila)
    return matriz_final

#suma de 2 matrices
def suma_matrices(m1,m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final

                    