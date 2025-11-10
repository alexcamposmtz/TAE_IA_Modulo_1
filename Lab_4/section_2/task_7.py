# task_7.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

"""
Se documenta un error de indice (IndexError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 7: IndexError - Error de Indice")
print("=" * 70)

# Ejemplo de matriz 4x4 como en nuestro laboratorio
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(f"\nMatriz 4x4:")
for fila in matriz:
    print(f"  {fila}")

print(f"\nDimensiones: 4 filas x 4 columnas")
print(f"Indices validos de filas: 0 a {len(matriz)-1}")
print(f"Indices validos de columnas: 0 a {len(matriz[0])-1}")

# CODIGO CON ERROR:
"""
print("\nIntentando acceder a matriz[4][0]...")
elemento = matriz[4][0]  # Error: fila 4 no existe
print(f"Elemento: {elemento}")
"""
# Error:
"""
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_7.py
======================================================================
TASK 7: IndexError - Error de Indice
======================================================================

Matriz 4x4:
  [1, 2, 3, 4]
  [5, 6, 7, 8]
  [9, 10, 11, 12]
  [13, 14, 15, 16]

Dimensiones: 4 filas x 4 columnas
Indices validos de filas: 0 a 3
Indices validos de columnas: 0 a 3

Intentando acceder a matriz[4][0]...
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_7.py", line 35, in <module>
    elemento = matriz[4][0]  # Error: fila 4 no existe
IndexError: list index out of range
"""

# Causa: La matriz tiene filas 0-3, pero intentamos acceder a fila 4

print("\nExplicacion del error:")
print("-" * 70)
print("Tipo de error: IndexError")
print("Causa: Intentar acceder a matriz[4][0] cuando solo hay indices 0-3")
print("Mensaje: IndexError: list index out of range")
print("\nEste error ocurre en nuestro laboratorio cuando:")
print("- Confundimos el tamaño de la matriz con el indice maximo")
print("- Usamos un loop incorrecto en multiplicacion de matrices")
print("- Olvidamos que los indices empiezan en 0")
print("Soluciones:")
print("1. Verificar dimensiones antes de acceder")
print("2. Usar range(len(matriz)) en loops")
print("3. Usar try-except para manejar el error")
print("-" * 70)

# CODIGO CORREGIDO - Opcion 1: Verificacion previa
print("Solucion 1 - Verificacion de dimensiones:")

def obtener_elemento_seguro(matriz, fila, columna):
    """Obtiene elemento de matriz verificando dimensiones"""
    if fila < 0 or fila >= len(matriz):
        print(f"Error: Fila {fila} fuera de rango (0-{len(matriz)-1})")
        return None
    if columna < 0 or columna >= len(matriz[0]):
        print(f"Error: Columna {columna} fuera de rango (0-{len(matriz[0])-1})")
        return None
    return matriz[fila][columna]

# Intentar acceso incorrecto
elemento = obtener_elemento_seguro(matriz, 4, 0)
print(f"Resultado: {elemento}")

# Acceso correcto
elemento = obtener_elemento_seguro(matriz, 3, 3)
print(f"Elemento en [3][3] (ultima posicion): {elemento}")