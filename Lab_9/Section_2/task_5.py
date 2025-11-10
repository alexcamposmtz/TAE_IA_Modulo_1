# task_5.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de indice (IndexError)
encontrado durante la practica con arrays de NumPy.
"""

import numpy as np

print("=" * 70)
print("TASK 5: IndexError - Error de Indice Fuera de Rango")
print("=" * 70)

# CODIGO CON ERROR:
"""
import numpy as np

# Crear array de 10 elementos
arr = np.arange(10)
print(f"Array: {arr}")
print(f"Longitud: {len(arr)}")

# Intentar acceder al indice 10 (Error: solo hay indices 0-9)
value = arr[10]
print(f"Valor en indice 10: {value}")
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_5.py
======================================================================
TASK 5: IndexError - Error de Indice Fuera de Rango
======================================================================
Array: [0 1 2 3 4 5 6 7 8 9]
Longitud: 10
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_5.py", line 27, in <module>
    value = arr[10]
IndexError: index 10 is out of bounds for axis 0 with size 10
"""

# Causa: Intentar acceder a un indice que no existe en el array

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: IndexError")
print("Causa: Intento de acceder al indice 10 en un array de tamaño 10")
print("Mensaje: IndexError: index 10 is out of bounds for axis 0 with size 10")
print()
print("En NumPy, los indices comienzan en 0:")
print("  - Array de tamaño 10 tiene indices validos: 0, 1, 2, ..., 9")
print("  - Indice 10 esta fuera de rango")
print()
print("Soluciones posibles:")
print("1. Verificar el tamaño del array antes de acceder")
print("2. Usar indices validos (0 hasta len(arr)-1)")
print("3. Usar indices negativos (-1, -2, etc.) para acceder desde el final")
print("4. Usar try-except para manejar el error")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Usar indice valido
print("\nSolucion 1: Usar indice valido")
print("-" * 70)

# Crear array de 10 elementos
arr = np.arange(10)
print(f"Array: {arr}")
print(f"Longitud: {len(arr)}")
print(f"Indices validos: 0 hasta {len(arr)-1}")

# Acceder al ultimo elemento (indice 9)
value = arr[9]
print(f"\nValor en indice 9 (ultimo): {value}")

# Tambien se puede usar -1 para el ultimo elemento
value_last = arr[-1]
print(f"Valor en indice -1 (ultimo): {value_last}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Verificar antes de acceder
print("\nSolucion 2: Verificar tamaño antes de acceder")
print("-" * 70)

arr = np.arange(10)
index_to_access = 10

print(f"Array: {arr}")
print(f"Longitud: {len(arr)}")
print(f"Indice que queremos acceder: {index_to_access}")

if 0 <= index_to_access < len(arr):
    value = arr[index_to_access]
    print(f"Valor en indice {index_to_access}: {value}")
else:
    print(f"Error: Indice {index_to_access} fuera de rango")
    print(f"Rango valido: 0 a {len(arr)-1}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 3: Slicing seguro
print("\nSolucion 3: Usar slicing (mas robusto)")
print("-" * 70)

arr = np.arange(10)
print(f"Array: {arr}")

# Slicing no genera IndexError, simplemente retorna un array vacio
result = arr[10:15]
print(f"\narr[10:15] = {result}")
print(f"Tipo: {type(result)}, Tamaño: {len(result)}")
print("Slicing fuera de rango retorna array vacio, no error")

# Obtener ultimos 3 elementos de forma segura
last_three = arr[-3:]
print(f"\nUltimos 3 elementos arr[-3:] = {last_three}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 4: Manejo con try-except
print("\nSolucion 4: Manejo de errores con try-except")
print("-" * 70)

arr = np.arange(10)
indices_to_try = [5, 9, 10, 15, -1]

print(f"Array: {arr}")
print(f"\nIntentando acceder a varios indices:")

for idx in indices_to_try:
    try:
        value = arr[idx]
        print(f"  arr[{idx:>3}] = {value:>2} ✓")
    except IndexError:
        print(f"  arr[{idx:>3}] = ERROR - Indice fuera de rango ✗")

# Demostracion adicional
print("\n" + "=" * 70)
print("DEMOSTRACION ADICIONAL: ARRAYS MULTIDIMENSIONALES")
print("=" * 70)

# Error comun con matrices
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\nMatriz 2x3:")
print(matrix)
print(f"Shape: {matrix.shape}")

print("\nAcceso correcto:")
print(f"  matrix[0, 0] = {matrix[0, 0]}")
print(f"  matrix[1, 2] = {matrix[1, 2]}")

print("\nAcceso incorrecto (comentado para evitar error):")
print("  # matrix[2, 0]  <- IndexError: index 2 fuera de rango para eje 0")
print("  # matrix[0, 3]  <- IndexError: index 3 fuera de rango para eje 1")

print("\nIndices validos para esta matriz:")
print(f"  Eje 0 (filas): 0 hasta {matrix.shape[0]-1}")
print(f"  Eje 1 (columnas): 0 hasta {matrix.shape[1]-1}")
