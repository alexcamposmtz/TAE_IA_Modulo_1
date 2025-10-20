# task_1.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Multiplicación de Matrices 4x4
"""
Este programa realiza la multiplicación de dos matrices 4x4
sin utilizar librerías externas (como NumPy).
Se implementan tres loops anidados para calcular cada elemento
de la matriz resultado.
"""

print("=" * 70)
print("Multiplicación de matriz 4x4")
print("=" * 70)

# Definir dos matrices 4x4
# Matriz A
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Matriz B
B = [
    [2, 0, 1, 3],
    [1, 2, 0, 1],
    [3, 1, 2, 0],
    [0, 3, 1, 2]
]

# Inicializar matriz resultado C con ceros
C = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(0)
    C.append(row)

# Realizar la multiplicación de matrices
# C[i][j] = suma de (A[i][k] * B[k][j]) para todo k
for i in range(4):                      # Iterar sobre las filas de A
    for j in range(4):                  # Iterar sobre las columnas de B
        for k in range(4):              # Iterar sobre las columnas de A / filas de B
            C[i][j] += A[i][k] * B[k][j]

# Mostrar resultados
print("\nMatriz A:")
for row in A:
    print(row)

print("\nMatriz B:")
for row in B:
    print(row)

print("\nMatriz Resultado C = A x B:")
for row in C:
    print(row)