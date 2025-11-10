# task_4.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de valor (ValueError)
encontrado durante la practica con matplotlib.
"""

print("=" * 70)
print("TASK 4: ValueError - Error de Valor")
print("=" * 70)

# CODIGO CON ERROR:
"""
import matplotlib.pyplot as plt
import numpy as np

# Crear datos con diferentes longitudes
x = [1, 2, 3, 4, 5]  # 5 elementos
y = [1, 4, 9, 16]    # 4 elementos (Error: longitudes diferentes)

plt.plot(x, y)
plt.title('Grafica con error')
plt.show()
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_4.py
======================================================================
TASK 4: ValueError - Error de Valor
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_4.py", line 24, in <module>
    plt.plot(x, y)
  File "/home/xandro/.local/lib/python3.10/site-packages/matplotlib/pyplot.py", line 3838, in plot
    return gca().plot(
  File "/home/xandro/.local/lib/python3.10/site-packages/matplotlib/axes/_axes.py", line 1777, in plot
    lines = [*self._get_lines(self, *args, data=data, **kwargs)]
  File "/home/xandro/.local/lib/python3.10/site-packages/matplotlib/axes/_base.py", line 297, in __call__
    yield from self._plot_args(
  File "/home/xandro/.local/lib/python3.10/site-packages/matplotlib/axes/_base.py", line 494, in _plot_args
    raise ValueError(f"x and y must have same first dimension, but "
ValueError: x and y must have same first dimension, but have shapes (5,) and (4,)
"""

# Causa: Las listas x e y tienen diferentes longitudes

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: ValueError")
print("Causa: Las listas x e y tienen longitudes diferentes")
print("Mensaje: ValueError: x and y must have same first dimension")
print("Este error ocurre en matplotlib cuando intentamos graficar")
print("dos arrays que no tienen la misma longitud.")
print()
print("En el codigo con error:")
print("  - x tiene 5 elementos: [1, 2, 3, 4, 5]")
print("  - y tiene 4 elementos: [1, 4, 9, 16]")
print("  - matplotlib no puede emparejar los puntos (x, y)")
print()
print("Soluciones posibles:")
print("1. Asegurar que x e y tengan la misma longitud")
print("2. Recortar la lista mas larga")
print("3. Extender la lista mas corta con valores apropiados")
print("4. Revisar la logica de generacion de datos")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Misma longitud
print("\nSolucion 1: Asegurar misma longitud desde el inicio")
print("-" * 70)

import matplotlib.pyplot as plt
import numpy as np

# Crear datos con la misma longitud
x = [1, 2, 3, 4, 5]      # 5 elementos
y = [1, 4, 9, 16, 25]    # 5 elementos (corregido)

print(f"Longitud de x: {len(x)}")
print(f"Longitud de y: {len(y)}")
print("Las longitudes coinciden. Graficando...")

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, marker='o', linestyle='-', linewidth=2, 
        markersize=8, color='#FF6B6B', label='y = x²')
ax.set_title('Grafica Corregida - Misma Longitud', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(fontsize=10)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([0, 5, 10, 15, 20, 25])

plt.tight_layout()
plt.show()

print("Grafica 1 mostrada exitosamente.")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Usar list comprehension
print("\nSolucion 2: Generar datos con list comprehension")
print("-" * 70)

x_values = list(range(1, 11))
y_values = [xi**2 for xi in x_values]  # Garantiza misma longitud

print(f"Longitud de x_values: {len(x_values)}")
print(f"Longitud de y_values: {len(y_values)}")
print("Datos generados con list comprehension. Graficando...")

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_values, y_values, marker='s', linestyle='-', 
        linewidth=2, markersize=6, color='#4ECDC4', label='y = x²')
ax.set_title('Grafica con List Comprehension', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(fontsize=10)
ax.set_xticks(range(1, 11))
ax.set_yticks(range(0, 101, 20))

plt.tight_layout()
plt.show()

print("Grafica 2 mostrada exitosamente.")
