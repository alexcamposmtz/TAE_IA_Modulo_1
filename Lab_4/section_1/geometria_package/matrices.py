def multiplicacion_matrices(matriz1, matriz2):
    """
    Realizamos la multiplicacion de dos matrices 4x4.
    
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
    Realizamos la suma de dos matrices 4x4.
    
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
    Realizamos la resta de dos matrices 4x4.
    
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
