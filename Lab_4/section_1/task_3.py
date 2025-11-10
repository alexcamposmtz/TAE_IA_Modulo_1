# task_3.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

import areas
import matrices

print("=" * 70)
print("TASK 3: PRUEBA DE MODULOS")
print("=" * 70)

print("\n" + "=" * 70)
print("PRUEBA DEL MODULO: areas.py")
print("=" * 70)

print("\n--- Calculando area de circulo con radio 5 ---")
area_c = areas.area_circulo(5)
print(f"Area del circulo: {area_c:.2f}")

print("\n--- Calculando area de cuadrado con lado 4 ---")
area_cuad = areas.area_cuadrado(4)
print(f"Area del cuadrado: {area_cuad:.2f}")

print("\n--- Calculando area de triangulo con base 6 y altura 8 ---")
area_t = areas.area_triangulo(6, 8)
print(f"Area del triangulo: {area_t:.2f}")

print("\n--- Calculando area de hexagono con lado 3 ---")
area_h = areas.area_hexagono(3)
print(f"Area del hexagono: {area_h:.2f}")

print("\n" + "=" * 70)
print("PRUEBA DEL MODULO: matrices.py")
print("=" * 70)

# Definir matrices de prueba
matriz_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matriz_B = [
    [2, 0, 1, 3],
    [1, 2, 0, 1],
    [0, 1, 2, 0],
    [3, 0, 1, 2]
]

matrices.imprimir_matriz(matriz_A, "Matriz A")
matrices.imprimir_matriz(matriz_B, "Matriz B")

print("\n--- Suma de matrices ---")
resultado_suma = matrices.suma_matrices(matriz_A, matriz_B)
matrices.imprimir_matriz(resultado_suma, "A + B")

print("\n--- Resta de matrices ---")
resultado_resta = matrices.resta_matrices(matriz_A, matriz_B)
matrices.imprimir_matriz(resultado_resta, "A - B")

print("\n--- Multiplicacion de matrices ---")
resultado_mult = matrices.multiplicacion_matrices(matriz_A, matriz_B)
matrices.imprimir_matriz(resultado_mult, "A x B")

print("\n" + "=" * 70)
print("PRUEBA COMPLETADA")
print("=" * 70)
