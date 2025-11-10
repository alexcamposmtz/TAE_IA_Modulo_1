# task_6.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de valor (ValueError)
encontrado durante la practica con reshape en NumPy.
"""

import numpy as np

print("=" * 70)
print("TASK 6: ValueError - Error en Reshape")
print("=" * 70)

# CODIGO CON ERROR:
"""
import numpy as np

# Crear array de 12 elementos
arr = np.arange(12)
print(f"Array original: {arr}")
print(f"Shape: {arr.shape}")

# Intentar reshape a 4x4 (Error: 12 elementos no caben en 4x4=16)
reshaped = arr.reshape(4, 4)
print(f"Array reshaped: {reshaped}")
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_6.py
======================================================================
TASK 6: ValueError - Error en Reshape
======================================================================
Array original: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Shape: (12,)
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_6.py", line 27, in <module>
    reshaped = arr.reshape(4, 4)
ValueError: cannot reshape array of size 12 into shape (4,4)
"""

# Causa: Intentar hacer reshape a una forma incompatible

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: ValueError")
print("Causa: Dimensiones incompatibles en reshape")
print("Mensaje: ValueError: cannot reshape array of size 12 into shape (4,4)")
print()
print("En NumPy, reshape requiere que:")
print("  Numero total de elementos = producto de las nuevas dimensiones")
print()
print("En el codigo con error:")
print("  - Array original tiene 12 elementos")
print("  - reshape(4, 4) requiere 4 × 4 = 16 elementos")
print("  - 12 ≠ 16, por lo tanto genera ValueError")
print()
print("Soluciones posibles:")
print("1. Usar dimensiones compatibles (3x4, 2x6, 1x12, etc.)")
print("2. Calcular dimensiones automaticamente con -1")
print("3. Usar resize() en lugar de reshape() (rellena con ceros)")
print("4. Agregar o eliminar elementos antes de reshape")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Dimensiones compatibles
print("\nSolucion 1: Usar dimensiones compatibles")
print("-" * 70)

arr = np.arange(12)
print(f"Array original: {arr}")
print(f"Shape: {arr.shape}, Elementos: {arr.size}")

print("\nReshapes validos para 12 elementos:")

# 3x4
reshaped_3x4 = arr.reshape(3, 4)
print(f"\nreshape(3, 4) - 3 × 4 = 12 ✓")
print(reshaped_3x4)

# 4x3
reshaped_4x3 = arr.reshape(4, 3)
print(f"\nreshape(4, 3) - 4 × 3 = 12 ✓")
print(reshaped_4x3)

# 2x6
reshaped_2x6 = arr.reshape(2, 6)
print(f"\nreshape(2, 6) - 2 × 6 = 12 ✓")
print(reshaped_2x6)

# 6x2
reshaped_6x2 = arr.reshape(6, 2)
print(f"\nreshape(6, 2) - 6 × 2 = 12 ✓")
print(reshaped_6x2)

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Dimension automatica con -1
print("\nSolucion 2: Calcular dimension automaticamente con -1")
print("-" * 70)

arr = np.arange(12)
print(f"Array original: {arr}")

# Especificar una dimension y dejar que NumPy calcule la otra
reshaped_auto = arr.reshape(3, -1)
print(f"\nreshape(3, -1) - NumPy calcula: 3 × {12//3} = 12 ✓")
print(reshaped_auto)

reshaped_auto2 = arr.reshape(-1, 4)
print(f"\nreshape(-1, 4) - NumPy calcula: {12//4} × 4 = 12 ✓")
print(reshaped_auto2)

print("\nNota: Solo se puede usar -1 en una dimension")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 3: Usar resize
print("\nSolucion 3: Usar resize() para forzar dimensiones")
print("-" * 70)

arr = np.arange(12)
print(f"Array original: {arr}")
print(f"Shape: {arr.shape}")

# resize permite cambiar el tamaño, rellenando con ceros si es necesario
arr_resized = np.resize(arr, (4, 4))
print(f"\nnp.resize(arr, (4, 4)) - Rellena con repeticion")
print(arr_resized)
print("\nNota: resize() repite los elementos si es necesario")

# Alternativa: pad con ceros
arr_padded = np.pad(arr, (0, 4), mode='constant')
arr_reshaped = arr_padded.reshape(4, 4)
print(f"\nAlternativa con pad (relleno de ceros):")
print(arr_reshaped)

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 4: Ajustar elementos
print("\nSolucion 4: Ajustar numero de elementos")
print("-" * 70)

# Crear array con el numero correcto de elementos desde el inicio
arr_16 = np.arange(16)
print(f"Array con 16 elementos: {arr_16}")

reshaped_correct = arr_16.reshape(4, 4)
print(f"\nreshape(4, 4) - 4 × 4 = 16 ✓")
print(reshaped_correct)

# O recortar el array original
arr = np.arange(12)
arr_truncated = arr[:9]  # Tomar solo 9 elementos
reshaped_truncated = arr_truncated.reshape(3, 3)
print(f"\nArray recortado a 9 elementos:")
print(f"Original: {arr}")
print(f"Recortado: {arr_truncated}")
print(f"reshape(3, 3) - 3 × 3 = 9 ✓")
print(reshaped_truncated)

# Tabla de reshapes comunes
print("\n" + "=" * 70)
print("TABLA DE RESHAPES COMUNES")
print("=" * 70)
print("\nPara N elementos, reshapes validos (filas × columnas = N):")
for n in [12, 16, 20, 24]:
    arr_temp = np.arange(n)
    print(f"\n{n} elementos:")
    divisors = [(i, n//i) for i in range(1, n+1) if n % i == 0]
    for rows, cols in divisors[:5]:  # Mostrar solo primeros 5
        print(f"  {rows} × {cols} = {n}")
    if len(divisors) > 5:
        print(f"  ... y {len(divisors)-5} mas")
