import numpy as np

def suma(m1,m2):
    m_final_suma = np.add(m1,m2)
    return m_final_suma

def resta(m1,m2):
    m_final_resta = np.subtrac(m1,m2)
    return m_final_resta

fila = int(input("ingrese la cantidad de filas de la matriz:"))
columna = int(input("ingrese la cantidad de columnas de la matriz:"))

#ingresar los elementos de la matriz 1
print("ingrese los elementos de la matriz 1:")
m1 = np.zeros((fila,columna))
for i in range(fila):
    for j in range(columna):
        elem = int(input(f"ingrese el elemento [{i}][{j}]:"))
        m1[i][j] = elem 

print("ingrese los elementos de la matriz 2:")
m2 = np.zeros((fila,columna))
for i in range(fila):
    for j in range(columna):
        elem = int(input(f"ingrese el elemento [{i}][{j}]:"))
        m2[i][j] = elem

m_final_suma = suma(m1,m2)
print("\nla matriz resultado de la suma es:")
print(m_final_suma)

m_final_resta = resta(m1,m2)
print("\nla matriz resultado de la resta es:")
print(m_final_resta)


