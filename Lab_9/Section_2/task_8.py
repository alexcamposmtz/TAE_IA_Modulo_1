# task_8.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de atributo (AttributeError)
encontrado durante la practica con metodos de NumPy.
"""

import numpy as np

print("=" * 70)
print("TASK 8: AttributeError - Error de Atributo/Metodo")
print("=" * 70)

# CODIGO CON ERROR:
"""
import numpy as np

# Crear array de NumPy
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")

# Intentar usar metodo que no existe (Error)
result = arr.append(6)
print(f"Array despues de append: {result}")
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_8.py
======================================================================
TASK 8: AttributeError - Error de Atributo/Metodo
======================================================================
Array: [1 2 3 4 5]
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_8.py", line 26, in <module>
    result = arr.append(6)
AttributeError: 'numpy.ndarray' object has no attribute 'append'
"""

# Causa: Los arrays de NumPy no tienen metodo append()

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: AttributeError")
print("Causa: Usar metodo que no existe en arrays de NumPy")
print("Mensaje: AttributeError: 'numpy.ndarray' object has no attribute 'append'")
print()
print("Diferencias clave entre listas de Python y arrays de NumPy:")
print()
print("Listas de Python:")
print("  - Tienen metodo .append()")
print("  - Son mutables y dinamicas")
print("  - Pueden contener tipos mixtos")
print()
print("Arrays de NumPy:")
print("  - NO tienen metodo .append()")
print("  - Tienen tamaño fijo (inmutables en tamaño)")
print("  - Todos elementos del mismo tipo")
print("  - Usan np.append() como funcion, no como metodo")
print()
print("Soluciones:")
print("1. Usar np.append() (funcion, no metodo)")
print("2. Usar np.concatenate() para unir arrays")
print("3. Crear un nuevo array con el tamaño correcto")
print("4. Usar listas si necesitas append dinamico")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Usar np.append()
print("\nSolucion 1: Usar np.append() (funcion)")
print("-" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array original: {arr}")
print(f"Shape: {arr.shape}")

# Forma correcta: np.append() es una FUNCION, no un metodo
arr_new = np.append(arr, 6)
print(f"\nnp.append(arr, 6):")
print(f"Array nuevo: {arr_new}")
print(f"Shape: {arr_new.shape}")

# Importante: np.append() retorna un NUEVO array
print(f"\nArray original (sin cambios): {arr}")
print("Nota: np.append() NO modifica el array original")

# Agregar multiples elementos
arr_multiple = np.append(arr, [6, 7, 8])
print(f"\nnp.append(arr, [6,7,8]):")
print(f"Resultado: {arr_multiple}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Usar concatenate
print("\nSolucion 2: Usar np.concatenate()")
print("-" * 70)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")

# Concatenar dos arrays
result = np.concatenate([arr1, arr2])
print(f"\nnp.concatenate([arr1, arr2]):")
print(f"Resultado: {result}")

# Concatenar multiples arrays
arr3 = np.array([7, 8, 9])
result_multiple = np.concatenate([arr1, arr2, arr3])
print(f"\nnp.concatenate([arr1, arr2, arr3]):")
print(f"Resultado: {result_multiple}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 3: Crear array con tamaño correcto
print("\nSolucion 3: Crear array del tamaño correcto desde el inicio")
print("-" * 70)

# Si conoces el tamaño final, crea el array completo
size = 10
arr_preallocated = np.zeros(size, dtype=np.int32)
print(f"Array pre-asignado (tamaño {size}): {arr_preallocated}")

# Llenar con valores
for i in range(size):
    arr_preallocated[i] = i + 1

print(f"Despues de llenar: {arr_preallocated}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 4: Usar listas cuando sea apropiado
print("\nSolucion 4: Usar listas si necesitas append dinamico")
print("-" * 70)

# Usar lista mientras construyes datos
data_list = [1, 2, 3, 4, 5]
print(f"Lista inicial: {data_list}")

# Agregar elementos dinamicamente
data_list.append(6)
data_list.append(7)
print(f"Despues de append: {data_list}")

# Convertir a array
arr_final = np.array(data_list)
print(f"\nConvertido a array NumPy: {arr_final}")
print(f"Tipo: {type(arr_final)}, Dtype: {arr_final.dtype}")

# Comparacion de metodos
print("\n" + "=" * 70)
print("COMPARACION: LISTAS vs ARRAYS DE NUMPY")
print("=" * 70)

print("\nMetodos de listas de Python:")
python_list = [1, 2, 3]
list_methods = [m for m in dir(python_list) if not m.startswith('_')]
print(f"Algunos metodos: {list_methods[:10]}")

print("\nMetodos de arrays de NumPy:")
numpy_array = np.array([1, 2, 3])
array_methods = [m for m in dir(numpy_array) if not m.startswith('_')][:10]
print(f"Algunos metodos: {array_methods}")