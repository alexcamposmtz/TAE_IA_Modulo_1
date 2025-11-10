# task_5.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de nombre (NameError)
encontrado durante la practica con matplotlib y list comprehensions.
"""

print("=" * 70)
print("TASK 5: NameError - Error de Nombre No Definido")
print("=" * 70)

# CODIGO CON ERROR:
"""
import matplotlib.pyplot as plt
import numpy as np

# Intentar usar una variable antes de definirla
x = np.linspace(0, 2 * np.pi, 100)
y = [np.sin(xi) * amplitude for xi in x]  # Error: amplitude no definida

plt.plot(x, y)
plt.title('Onda Seno con Amplitud')
plt.show()
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_5.py
======================================================================
TASK 5: NameError - Error de Nombre No Definido
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_5.py", line 22, in <module>
    y = [np.sin(xi) * amplitude for xi in x]  # Error: amplitude no definida
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_5.py", line 22, in <listcomp>
    y = [np.sin(xi) * amplitude for xi in x]  # Error: amplitude no definida
NameError: name 'amplitude' is not defined
"""

# Causa: Variable 'amplitude' usada sin ser definida previamente

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: NameError")
print("Causa: Variable 'amplitude' no esta definida")
print("Mensaje: NameError: name 'amplitude' is not defined")
print("Este error ocurre cuando intentamos usar una variable")
print("que no ha sido definida previamente en el codigo.")
print()
print("Casos comunes de NameError:")
print("1. Usar una variable antes de asignarle un valor")
print("2. Error tipografico en el nombre de la variable")
print("3. Variable definida en un scope diferente")
print("4. Olvidar importar un modulo o funcion")
print()
print("Soluciones:")
print("1. Definir la variable antes de usarla")
print("2. Verificar la ortografia del nombre")
print("3. Asegurar que la variable este en el scope correcto")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Definir la variable
print("\nSolucion 1: Definir la variable antes de usarla")
print("-" * 70)

import matplotlib.pyplot as plt
import numpy as np

# Definir amplitude antes de usarla
amplitude = 2.0  # Definida antes del list comprehension
x = np.linspace(0, 2 * np.pi, 100)
y = [np.sin(xi) * amplitude for xi in x]

print(f"Amplitud definida: {amplitude}")
print(f"Numero de puntos: {len(x)}")
print("Variable definida correctamente. Graficando...")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color='#A23B72', linewidth=2.5, label=f'Amplitud = {amplitude}')
ax.set_title('Onda Seno con Amplitud Definida', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X (radianes)', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.5)
ax.legend(fontsize=10)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
ax.set_yticks([-2, -1, 0, 1, 2])

plt.tight_layout()
plt.show()

print("Grafica 1 mostrada exitosamente.")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Usar parametros de funcion
print("\nSolucion 2: Usar parametros de funcion para evitar NameError")
print("-" * 70)

def generate_sine_wave(amplitude, frequency, num_points=100):
    """
    Genera una onda seno con amplitud y frecuencia especificadas.
    
    Parametros:
        amplitude (float): Amplitud de la onda
        frequency (float): Frecuencia de la onda
        num_points (int): Numero de puntos a generar
        
    Retorna:
        tuple: Arrays de x e y
    """
    x = np.linspace(0, 2 * np.pi, num_points)
    y = [amplitude * np.sin(frequency * xi) for xi in x]
    return x, y

# Generar multiples ondas con diferentes amplitudes
amplitudes = [0.5, 1.0, 1.5, 2.0]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

fig, ax = plt.subplots(figsize=(10, 6))

for amp, color in zip(amplitudes, colors):
    x, y = generate_sine_wave(amplitude=amp, frequency=1)
    ax.plot(x, y, color=color, linewidth=2, label=f'A = {amp}', alpha=0.8)

ax.set_title('Ondas Seno con Diferentes Amplitudes', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('X (radianes)', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')
ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.5)
ax.legend(fontsize=10)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
ax.set_yticks([-2, -1, 0, 1, 2])

plt.tight_layout()
plt.show()

print("Grafica 2 mostrada exitosamente.")
print("\nUsando funciones con parametros, evitamos NameError")
print("y hacemos el codigo mas reutilizable.")
