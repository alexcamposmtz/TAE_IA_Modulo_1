# task_2.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

def multiplicacion_matrices(matriz1, matriz2):
    """
    Realiza la multiplicacion de dos matrices 4x4.
    
    Parametros:
        matriz1: Primera matriz 4x4
        matriz2: Segunda matriz 4x4
    
    Retorna:
        Matriz resultante 4x4
    """
    resultado = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado


def suma_matrices(matriz1, matriz2):
    """
    Realiza la suma de dos matrices 4x4.
    
    Parametros:
        matriz1: Primera matriz 4x4
        matriz2: Segunda matriz 4x4
    
    Retorna:
        Matriz resultante 4x4
    """
    resultado = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return resultado


def resta_matrices(matriz1, matriz2):
    """
    Realiza la resta de dos matrices 4x4.
    
    Parametros:
        matriz1: Primera matriz 4x4
        matriz2: Segunda matriz 4x4
    
    Retorna:
        Matriz resultante 4x4
    """
    resultado = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            resultado[i][j] = matriz1[i][j] - matriz2[i][j]
    
    return resultado


def imprimir_matriz(matriz, nombre="Matriz"):
    """
    Imprime una matriz de forma legible.
    
    Parametros:
        matriz: Matriz a imprimir
        nombre: Nombre de la matriz
    """
    print(f"\n{nombre}:")
    for fila in matriz:
        print("[", end=" ")
        for elemento in fila:
            print(f"{elemento:6.2f}", end=" ")
        print("]")


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 2: OPERACIONES CON MATRICES 4x4")
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
    
    # Imprimir matrices originales
    imprimir_matriz(matriz_A, "Matriz A")
    imprimir_matriz(matriz_B, "Matriz B")
    
    # Realizar operaciones
    print("\n" + "=" * 70)
    print("RESULTADOS DE OPERACIONES")
    print("=" * 70)
    
    resultado_suma = suma_matrices(matriz_A, matriz_B)
    imprimir_matriz(resultado_suma, "A + B")
    
    resultado_resta = resta_matrices(matriz_A, matriz_B)
    imprimir_matriz(resultado_resta, "A - B")
    
    resultado_multiplicacion = multiplicacion_matrices(matriz_A, matriz_B)
    imprimir_matriz(resultado_multiplicacion, "A x B")
