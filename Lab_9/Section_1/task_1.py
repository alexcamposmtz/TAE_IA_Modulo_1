# task_1.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 1: Crear un array A con numeros del 1 al 20.
- Obtener elementos en indices pares (no valores pares)
- Calcular la suma de todos los valores impares
- Reemplazar todos los multiplos de 3 con -1
- Imprimir el array resultante
"""

import numpy as np


def main():
    """Funcion principal que ejecuta todas las operaciones del Task 1."""
    print("=" * 70)
    print("TASK 1: OPERACIONES BASICAS CON ARRAYS DE NUMPY")
    print("=" * 70)
    
    # Crear array A con numeros del 1 al 20
    A = np.arange(1, 21)
    print("\n--- Array Original ---")
    print(f"A = {A}")
    print(f"Tipo: {type(A)}")
    print(f"Shape: {A.shape}")
    print(f"Dtype: {A.dtype}")
    
    # 1. Obtener elementos en indices pares (posiciones 0, 2, 4, ...)
    print("\n" + "-" * 70)
    print("1. Elementos en indices pares (no valores pares)")
    print("-" * 70)
    even_indices = A[::2]  # Slicing: desde inicio, hasta final, paso 2
    print(f"Indices pares: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18")
    print(f"Elementos en indices pares: {even_indices}")
    print(f"Numero de elementos: {len(even_indices)}")
    
    # 2. Calcular la suma de todos los valores impares
    print("\n" + "-" * 70)
    print("2. Suma de todos los valores impares")
    print("-" * 70)
    # Indexacion condicional: seleccionar elementos donde A % 2 != 0
    odd_values = A[A % 2 != 0]
    sum_odd = np.sum(odd_values)
    print(f"Valores impares: {odd_values}")
    print(f"Suma de valores impares: {sum_odd}")
    
    # Verificacion matematica: suma de n numeros impares = n^2
    n_odd = len(odd_values)
    print(f"Verificacion: suma de {n_odd} primeros impares = {n_odd}^2 = {n_odd**2}")
    
    # 3. Reemplazar todos los multiplos de 3 con -1
    print("\n" + "-" * 70)
    print("3. Reemplazar multiplos de 3 con -1")
    print("-" * 70)
    # Crear una copia para no modificar el original
    A_modified = A.copy()
    
    # Encontrar multiplos de 3
    multiples_of_3_mask = A_modified % 3 == 0
    multiples_of_3 = A_modified[multiples_of_3_mask]
    print(f"Multiplos de 3 originales: {multiples_of_3}")
    print(f"Posiciones: {np.where(multiples_of_3_mask)[0]}")
    
    # Reemplazar con -1
    A_modified[multiples_of_3_mask] = -1
    
    print("\n--- Array Resultante ---")
    print(f"A_modified = {A_modified}")
    
    # Mostrar comparacion
    print("\n" + "-" * 70)
    print("Comparacion Original vs Modificado")
    print("-" * 70)
    print(f"Original:    {A}")
    print(f"Modificado:  {A_modified}")
    
    # Estadisticas finales
    print("\n" + "-" * 70)
    print("Estadisticas del Array Modificado")
    print("-" * 70)
    print(f"Minimo: {np.min(A_modified)}")
    print(f"Maximo: {np.max(A_modified)}")
    print(f"Media: {np.mean(A_modified):.2f}")
    print(f"Suma total: {np.sum(A_modified)}")
    print(f"Cantidad de -1: {np.sum(A_modified == -1)}")
    print(f"Cantidad de positivos: {np.sum(A_modified > 0)}")


if __name__ == "__main__":
    main()
