# task_2.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 2: Matrices especiales y operaciones basicas
- Crear matriz 4x4 de unos (M1)
- Crear matriz 4x4 llena de 5s (M2)
- Crear matriz identidad 4x4 (I)
- Calcular S = M1 + M2 - I
- Calcular P = M2 * I (multiplicacion elemento por elemento)
"""

import numpy as np


def print_matrix(name, matrix):
    """
    Imprime una matriz de forma formateada.
    
    Parametros:
        name (str): Nombre de la matriz
        matrix (ndarray): Matriz a imprimir
    """
    print(f"\n{name}:")
    print(matrix)
    print(f"Shape: {matrix.shape}, Dtype: {matrix.dtype}")


def main():
    """Funcion principal que ejecuta todas las operaciones del Task 2."""
    print("=" * 70)
    print("TASK 2: MATRICES ESPECIALES Y OPERACIONES BASICAS")
    print("=" * 70)
    
    # 1. Crear matriz 4x4 de unos (M1)
    print("\n--- Creando Matrices Especiales ---")
    M1 = np.ones((4, 4))
    print_matrix("M1 (Matriz de unos 4x4)", M1)
    
    # 2. Crear matriz 4x4 llena de 5s (M2)
    M2 = np.full((4, 4), 5)
    # Alternativa: M2 = np.ones((4, 4)) * 5
    print_matrix("M2 (Matriz de 5s 4x4)", M2)
    
    # 3. Crear matriz identidad 4x4 (I)
    I = np.eye(4)
    print_matrix("I (Matriz identidad 4x4)", I)
    
    # Explicacion de matrices especiales
    print("\n" + "-" * 70)
    print("Explicacion de Matrices Especiales")
    print("-" * 70)
    print("M1: Matriz de unos - np.ones((4, 4))")
    print("    Todos los elementos son 1")
    print("\nM2: Matriz de 5s - np.full((4, 4), 5)")
    print("    Todos los elementos son 5")
    print("\nI:  Matriz identidad - np.eye(4)")
    print("    Diagonal principal = 1, resto = 0")
    
    # 4. Calcular S = M1 + M2 - I
    print("\n" + "=" * 70)
    print("Operacion 1: S = M1 + M2 - I")
    print("=" * 70)
    S = M1 + M2 - I
    
    print("\nPaso a paso:")
    print("M1 + M2 =")
    print(M1 + M2)
    print("\n(M1 + M2) - I =")
    print_matrix("S (Resultado final)", S)
    
    # Verificacion
    print("\nVerificacion:")
    print("  - Elementos diagonal: 1 + 5 - 1 = 5")
    print("  - Elementos fuera diagonal: 1 + 5 - 0 = 6")
    print(f"  Valor diagonal: {S[0, 0]}")
    print(f"  Valor fuera diagonal: {S[0, 1]}")
    
    # 5. Calcular P = M2 * I (multiplicacion elemento por elemento)
    print("\n" + "=" * 70)
    print("Operacion 2: P = M2 * I (multiplicacion elemento por elemento)")
    print("=" * 70)
    P = M2 * I  # Multiplicacion elemento por elemento (Hadamard)
    
    print("\nNota: '*' en NumPy es multiplicacion elemento por elemento")
    print("No es multiplicacion matricial (para eso usar '@' o np.matmul)")
    
    print_matrix("P (Resultado final)", P)
    
    print("\nVerificacion:")
    print("  - Elementos diagonal: 5 * 1 = 5")
    print("  - Elementos fuera diagonal: 5 * 0 = 0")
    print(f"  Valor diagonal: {P[0, 0]}")
    print(f"  Valor fuera diagonal: {P[0, 1]}")
    print("  P es una matriz diagonal con 5s en la diagonal principal")
    
    # Resumen de resultados
    print("\n" + "=" * 70)
    print("RESUMEN DE RESULTADOS")
    print("=" * 70)
    print("\nMatriz S = M1 + M2 - I:")
    print(S)
    print(f"  - Suma de todos los elementos: {np.sum(S)}")
    print(f"  - Valor promedio: {np.mean(S):.2f}")
    
    print("\nMatriz P = M2 * I:")
    print(P)
    print(f"  - Suma de todos los elementos: {np.sum(P)}")
    print(f"  - Traza (suma diagonal): {np.trace(P)}")
    
    # Operaciones adicionales para demostrar conocimiento
    print("\n" + "-" * 70)
    print("Operaciones Adicionales (Demostracion)")
    print("-" * 70)
    
    # Multiplicacion matricial vs elemento por elemento
    P_matmul = M2 @ I  # Multiplicacion matricial
    print("\nMultiplicacion matricial M2 @ I:")
    print(P_matmul)
    print("Resultado identico a M2 * I porque I es identidad")
    
    # Transpuesta
    print(f"\nTranspuesta de S igual a S? {np.array_equal(S, S.T)}")
    print("(S es simetrica)")


if __name__ == "__main__":
    main()
