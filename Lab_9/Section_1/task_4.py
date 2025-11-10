# task_4.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 4:
- Generar matriz 3x3 con enteros aleatorios de 1 a 9
- Guardar la matriz en "matrix_original.npy"
- Cargar el archivo en variable B
- Elevar al cuadrado todos los elementos de B
- Guardar como "matrix_squared.npy"
- Cargar ambas matrices y verificar que ningun elemento coincida
"""

import numpy as np
import os


def main():
    """Funcion principal que ejecuta todas las operaciones del Task 4."""
    print("=" * 70)
    print("TASK 4: GUARDAR Y CARGAR MATRICES CON NUMPY")
    print("=" * 70)
    
    # 1. Generar matriz 3x3 con enteros aleatorios de 1 a 9
    print("\n--- Generando Matriz Original ---")
    print("-" * 70)
    np.random.seed(42)  # Para reproducibilidad
    matrix_original = np.random.randint(1, 10, size=(3, 3))
    print("Matriz original generada (3x3 con enteros de 1 a 9):")
    print(matrix_original)
    print(f"Shape: {matrix_original.shape}, Dtype: {matrix_original.dtype}")
    
    # 2. Guardar la matriz en "matrix_original.npy"
    print("\n--- Guardando Matriz Original ---")
    print("-" * 70)
    filename_original = "matrix_original.npy"
    np.save(filename_original, matrix_original)
    print(f"Matriz guardada en: {filename_original}")
    
    # Verificar que el archivo existe
    if os.path.exists(filename_original):
        file_size = os.path.getsize(filename_original)
        print(f"Archivo creado exitosamente")
        print(f"Tamaño del archivo: {file_size} bytes")
    
    # 3. Cargar el archivo en variable B
    print("\n--- Cargando Matriz desde Archivo ---")
    print("-" * 70)
    B = np.load(filename_original)
    print(f"Matriz cargada desde {filename_original}:")
    print(B)
    print(f"Shape: {B.shape}, Dtype: {B.dtype}")
    
    # Verificar que se cargó correctamente
    print(f"\nVerificacion: Matrices identicas? {np.array_equal(matrix_original, B)}")
    
    # 4. Elevar al cuadrado todos los elementos de B
    print("\n--- Elevando al Cuadrado ---")
    print("-" * 70)
    B_squared = B ** 2
    print("Matriz B (original):")
    print(B)
    print("\nMatriz B^2 (al cuadrado):")
    print(B_squared)
    
    # Mostrar la transformacion elemento por elemento
    print("\nTransformacion elemento por elemento:")
    for i in range(3):
        for j in range(3):
            print(f"  B[{i},{j}] = {B[i,j]} → B_squared[{i},{j}] = "
                  f"{B[i,j]}^2 = {B_squared[i,j]}")
    
    # 5. Guardar como "matrix_squared.npy"
    print("\n--- Guardando Matriz al Cuadrado ---")
    print("-" * 70)
    filename_squared = "matrix_squared.npy"
    np.save(filename_squared, B_squared)
    print(f"Matriz al cuadrado guardada en: {filename_squared}")
    
    if os.path.exists(filename_squared):
        file_size = os.path.getsize(filename_squared)
        print(f"Archivo creado exitosamente")
        print(f"Tamaño del archivo: {file_size} bytes")
    
    # 6. Cargar ambas matrices y verificar que ningun elemento coincida
    print("\n" + "=" * 70)
    print("VERIFICACION: NINGUN ELEMENTO DEBE COINCIDIR")
    print("=" * 70)
    
    # Cargar ambas matrices
    matrix_1 = np.load(filename_original)
    matrix_2 = np.load(filename_squared)
    
    print("\nMatriz Original:")
    print(matrix_1)
    print("\nMatriz al Cuadrado:")
    print(matrix_2)
    
    # Comparacion booleana elemento por elemento
    print("\n--- Comparacion Booleana (elemento por elemento) ---")
    print("-" * 70)
    comparison = matrix_1 == matrix_2
    print("Mascara booleana (True = elementos iguales):")
    print(comparison)
    
    # Contar coincidencias
    num_matches = np.sum(comparison)
    total_elements = matrix_1.size
    print(f"\nNumero de elementos que coinciden: {num_matches}")
    print(f"Total de elementos: {total_elements}")
    print(f"Porcentaje de coincidencias: {num_matches/total_elements*100:.1f}%")
    
    # Verificacion especial para el valor 1
    print("\n--- Caso Especial: El numero 1 ---")
    print("-" * 70)
    ones_in_original = np.sum(matrix_1 == 1)
    if ones_in_original > 0:
        print(f"La matriz original contiene {ones_in_original} elemento(s) con valor 1")
        print(f"1^2 = 1, por lo que estos elementos coincidiran")
        print(f"Posiciones de 1s en matriz original:")
        ones_positions = np.where(matrix_1 == 1)
        for i, j in zip(ones_positions[0], ones_positions[1]):
            print(f"  matrix_1[{i},{j}] = 1 → matrix_2[{i},{j}] = 1")
    else:
        print("La matriz original no contiene 1s")
        print("Por lo tanto, NINGUN elemento coincide")
    
    # Resultado final
    print("\n" + "=" * 70)
    print("RESULTADO FINAL")
    print("=" * 70)
    if num_matches == 0:
        print("EXITO: Ningun elemento coincide entre las matrices")
    elif num_matches == ones_in_original:
        print(f"NOTA: Solo coinciden {num_matches} elemento(s) con valor 1")
        print("Esto es esperado porque 1^2 = 1")
    else:
        print(f"ATENCION: {num_matches} elementos coinciden")
    
    # Informacion de archivos guardados
    print("\n--- Archivos Guardados ---")
    print("-" * 70)
    print(f"1. {filename_original}")
    print(f"   Contiene: Matriz original 3x3")
    print(f"2. {filename_squared}")
    print(f"   Contiene: Matriz al cuadrado 3x3")
    print("\nEstos archivos pueden ser cargados con np.load()")
    
    # Limpiar archivos (opcional)
    print("\n--- Limpieza (Opcional) ---")
    print("-" * 70)
    print("Para eliminar los archivos .npy, ejecutar:")
    print(f"  os.remove('{filename_original}')")
    print(f"  os.remove('{filename_squared}')")


if __name__ == "__main__":
    main()
