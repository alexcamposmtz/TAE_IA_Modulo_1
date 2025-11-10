# task_3.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 3:
- Crear array x de 15 valores equiespaciados entre 0 y 10 (np.linspace)
- Crear array r de 15 enteros aleatorios entre 0 y 100 (np.random.randint)
- Calcular:
  * Elementos de r mayores que la media de r
  * Suma de elementos en x menores que 5
  * Valor maximo de r y su posicion (indice)
"""

import numpy as np


def main():
    """Funcion principal que ejecuta todas las operaciones del Task 3."""
    print("=" * 70)
    print("TASK 3: ARRAYS Y OPERACIONES ESTADISTICAS")
    print("=" * 70)
    
    # 1. Crear array x con np.linspace
    print("\n--- Creacion de Arrays ---")
    print("-" * 70)
    x = np.linspace(0, 10, 15)
    print("Array x (15 valores equiespaciados entre 0 y 10):")
    print(f"x = {x}")
    print(f"Shape: {x.shape}, Dtype: {x.dtype}")
    print(f"Espaciado: {x[1] - x[0]:.4f}")
    
    # 2. Crear array r con np.random.randint
    # Fijar seed para reproducibilidad (opcional)
    np.random.seed(42)
    r = np.random.randint(0, 101, size=15)  # 101 para incluir 100
    print("\nArray r (15 enteros aleatorios entre 0 y 100):")
    print(f"r = {r}")
    print(f"Shape: {r.shape}, Dtype: {r.dtype}")
    
    # Estadisticas basicas de r
    print("\n" + "-" * 70)
    print("Estadisticas de r")
    print("-" * 70)
    mean_r = np.mean(r)
    print(f"Media: {mean_r:.2f}")
    print(f"Mediana: {np.median(r):.2f}")
    print(f"Desviacion estandar: {np.std(r):.2f}")
    print(f"Minimo: {np.min(r)}")
    print(f"Maximo: {np.max(r)}")
    
    # 3. Elementos de r mayores que la media de r
    print("\n" + "=" * 70)
    print("1. Elementos de r mayores que la media de r")
    print("=" * 70)
    greater_than_mean = r[r > mean_r]
    print(f"Media de r: {mean_r:.2f}")
    print(f"Elementos mayores que la media: {greater_than_mean}")
    print(f"Cantidad de elementos: {len(greater_than_mean)}")
    print(f"Porcentaje: {len(greater_than_mean)/len(r)*100:.1f}%")
    
    # Mostrar con indices
    indices_greater = np.where(r > mean_r)[0]
    print(f"\nIndices de elementos mayores que la media: {indices_greater}")
    for idx in indices_greater:
        print(f"  r[{idx}] = {r[idx]}")
    
    # 4. Suma de elementos en x menores que 5
    print("\n" + "=" * 70)
    print("2. Suma de elementos en x menores que 5")
    print("=" * 70)
    less_than_5 = x[x < 5]
    sum_less_than_5 = np.sum(less_than_5)
    print(f"Elementos de x menores que 5: {less_than_5}")
    print(f"Cantidad de elementos: {len(less_than_5)}")
    print(f"Suma de elementos: {sum_less_than_5:.4f}")
    
    # Verificacion
    print(f"\nVerificacion manual:")
    print(f"  Suma = {' + '.join([f'{val:.4f}' for val in less_than_5[:3]])} + ...")
    print(f"  Total = {sum_less_than_5:.4f}")
    
    # 5. Valor maximo de r y su posicion
    print("\n" + "=" * 70)
    print("3. Valor maximo de r y su posicion (indice)")
    print("=" * 70)
    max_value = np.max(r)
    max_index = np.argmax(r)  # Retorna el indice del primer maximo
    print(f"Valor maximo: {max_value}")
    print(f"Posicion (indice): {max_index}")
    print(f"Verificacion: r[{max_index}] = {r[max_index]}")
    
    # Verificar si hay multiples maximos
    all_max_indices = np.where(r == max_value)[0]
    if len(all_max_indices) > 1:
        print(f"\nNota: Hay {len(all_max_indices)} elementos con el valor maximo")
        print(f"Indices: {all_max_indices}")
    else:
        print(f"\nEl valor maximo es unico en el array")
    
    # Resumen visual
    print("\n" + "=" * 70)
    print("RESUMEN VISUAL")
    print("=" * 70)
    
    print("\nArray r con anotaciones:")
    print("Indice:  ", end="")
    for i in range(len(r)):
        print(f"{i:>4}", end=" ")
    print("\nValor:   ", end="")
    for i in range(len(r)):
        print(f"{r[i]:>4}", end=" ")
    print("\nEstado:  ", end="")
    for i in range(len(r)):
        if r[i] == max_value:
            print(" MAX", end=" ")
        elif r[i] > mean_r:
            print(" >M ", end=" ")
        else:
            print(" <=M", end=" ")
    print()
    
    print(f"\nLeyenda:")
    print(f"  MAX  = Valor maximo ({max_value})")
    print(f"  >M   = Mayor que la media ({mean_r:.2f})")
    print(f"  <=M  = Menor o igual que la media")
    
    # Comparacion entre x e r
    print("\n" + "-" * 70)
    print("Comparacion entre arrays x y r")
    print("-" * 70)
    print(f"Array x (ordenado): min={np.min(x):.2f}, max={np.max(x):.2f}, "
          f"media={np.mean(x):.2f}")
    print(f"Array r (aleatorio): min={np.min(r)}, max={np.max(r)}, "
          f"media={np.mean(r):.2f}")


if __name__ == "__main__":
    main()
