# task_6.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de clave (KeyError)
encontrado durante la practica con configuracion de graficas.
"""

print("=" * 70)
print("TASK 6: KeyError - Error de Clave No Encontrada")
print("=" * 70)

# CODIGO CON ERROR:
"""
import matplotlib.pyplot as plt
import numpy as np

# Diccionario con configuracion de graficas
plot_config = {
    'color': '#FF6B6B',
    'linewidth': 2,
    'linestyle': '-'
}

x = np.linspace(0, 2 * np.pi, 100)
y = [np.sin(xi) for xi in x]

# Error: intentar acceder a una clave que no existe
plt.plot(x, y, 
         color=plot_config['color'],
         linewidth=plot_config['linewidth'],
         linestyle=plot_config['linestyle'],
         marker=plot_config['marker'])  # Error: 'marker' no existe

plt.title('Onda Seno')
plt.show()
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_6.py
======================================================================
TASK 6: KeyError - Error de Clave No Encontrada
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_6.py", line 35, in <module>
    marker=plot_config['marker'])  # Error: 'marker' no existe
KeyError: 'marker'
"""

# Causa: Intentar acceder a una clave que no existe en el diccionario

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: KeyError")
print("Causa: La clave 'marker' no existe en el diccionario")
print("Mensaje: KeyError: 'marker'")
print("Este error ocurre cuando intentamos acceder a una clave")
print("que no existe en un diccionario.")
print()
print("En el codigo con error:")
print("  - El diccionario tiene: 'color', 'linewidth', 'linestyle'")
print("  - Intentamos acceder a: 'marker' (no existe)")
print()
print("Soluciones posibles:")
print("1. Agregar la clave al diccionario")
print("2. Usar dict.get() con valor por defecto")
print("3. Verificar existencia con 'in' antes de acceder")
print("4. Usar try-except para manejar el error")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Agregar la clave
print("\nSolucion 1: Agregar la clave faltante al diccionario")
print("-" * 70)

import matplotlib.pyplot as plt
import numpy as np

# Diccionario completo con todas las claves necesarias
plot_config = {
    'color': '#FF6B6B',
    'linewidth': 2,
    'linestyle': '-',
    'marker': 'o'  # Clave agregada
}

x = np.linspace(0, 2 * np.pi, 20)
y = [np.sin(xi) for xi in x]

print("Configuracion de la grafica:")
for key, value in plot_config.items():
    print(f"  {key}: {value}")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y,
        color=plot_config['color'],
        linewidth=plot_config['linewidth'],
        linestyle=plot_config['linestyle'],
        marker=plot_config['marker'],  # Ahora funciona
        markersize=8)

ax.set_title('Onda Seno - Solucion 1: Clave Agregada', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X (radianes)', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

plt.tight_layout()
plt.show()

print("Grafica 1 mostrada exitosamente.")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Usar get() con valor por defecto
print("\nSolucion 2: Usar dict.get() con valor por defecto")
print("-" * 70)

# Diccionario sin la clave 'marker'
plot_config_2 = {
    'color': '#4ECDC4',
    'linewidth': 2,
    'linestyle': '--'
}

x = np.linspace(0, 2 * np.pi, 20)
y = [np.cos(xi) for xi in x]

print("Configuracion de la grafica:")
print(f"  color: {plot_config_2.get('color', 'blue')}")
print(f"  linewidth: {plot_config_2.get('linewidth', 1)}")
print(f"  linestyle: {plot_config_2.get('linestyle', '-')}")
print(f"  marker: {plot_config_2.get('marker', 'None')} (valor por defecto)")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y,
        color=plot_config_2.get('color', 'blue'),
        linewidth=plot_config_2.get('linewidth', 1),
        linestyle=plot_config_2.get('linestyle', '-'),
        marker=plot_config_2.get('marker', 's'),  # Usa 's' si no existe
        markersize=8)

ax.set_title('Onda Coseno - Solucion 2: get() con Default', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X (radianes)', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

plt.tight_layout()
plt.show()

print("Grafica 2 mostrada exitosamente.")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 3: Verificar existencia
print("\nSolucion 3: Verificar existencia con 'in'")
print("-" * 70)

# Diccionario parcial
plot_config_3 = {
    'color': '#FFA07A',
    'linewidth': 3,
}

x = np.linspace(0, 2 * np.pi, 20)
y = [np.sin(xi) * np.cos(xi) for xi in x]

# Construir argumentos verificando existencia
plot_args = {}
plot_args['color'] = plot_config_3['color'] if 'color' in plot_config_3 else 'black'
plot_args['linewidth'] = plot_config_3['linewidth'] if 'linewidth' in plot_config_3 else 1
plot_args['linestyle'] = plot_config_3['linestyle'] if 'linestyle' in plot_config_3 else '-'
plot_args['marker'] = plot_config_3['marker'] if 'marker' in plot_config_3 else '^'

print("Argumentos de la grafica:")
for key, value in plot_args.items():
    print(f"  {key}: {value}")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, **plot_args, markersize=8)

ax.set_title('Funcion Mixta - Solucion 3: Verificacion con in', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X (radianes)', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

plt.tight_layout()
plt.show()

print("Grafica 3 mostrada exitosamente.")
print("\nLa verificacion con 'in' evita KeyError y proporciona")
print("valores por defecto cuando una clave no existe.")
