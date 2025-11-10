# task_4.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

from geometria_package import multiplicacion_matrices, area_hexagono, imprimir_matriz

print("=" * 70)
print("TASK 4: USO DEL PAQUETE geometria_package")
print("=" * 70)

print("\n" + "=" * 70)
print("1. CALCULO DEL AREA DE UN HEXAGONO")
print("=" * 70)

lado_hexagono = 5
print(f"\nCalculando el area de un hexagono con lado {lado_hexagono}...")
area = area_hexagono(lado_hexagono)
print(f"Area del hexagono: {area:.2f}")

print("\n" + "=" * 70)
print("2. MULTIPLICACION DE MATRICES 4x4")
print("=" * 70)

# Definir matrices para multiplicacion
matriz_1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matriz_2 = [
    [2, 0, 1, 3],
    [1, 2, 0, 1],
    [0, 1, 2, 0],
    [3, 0, 1, 2]
]

imprimir_matriz(matriz_1, "Matriz 1")
imprimir_matriz(matriz_2, "Matriz 2")

print("\n--- Realizando multiplicacion de matrices ---")
resultado = multiplicacion_matrices(matriz_1, matriz_2)
imprimir_matriz(resultado, "Resultado: Matriz 1 x Matriz 2")

print("\n" + "=" * 70)
print("OPERACIONES COMPLETADAS")
print("=" * 70)
