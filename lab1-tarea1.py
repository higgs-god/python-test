import random

def matriz_random(filas,columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(0,5) 
            fila.append(elem)
        m.append(fila)
    return m 

def suma_matrices(m1,m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final

filas = int(input("ingrese la cantidad de filas de la matriz:"))
columnas = int(input("ingrese la cantidad de columnas de la matriz:"))
print(("creando la primera matriz aleatoria:"))
m1 = matriz_random(filas,columnas)
print(m1,"\n")
print(("creando la segunda matriz aleatoria:"))
m2 = matriz_random(filas,columnas)
print(m2,"\n")

matriz_final = suma_matrices(m1,m2)
print("la suma de las matrices es:")
for fila in matriz_final:
    print(fila)
