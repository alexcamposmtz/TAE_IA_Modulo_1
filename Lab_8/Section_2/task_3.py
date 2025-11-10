# task_3.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de importacion (ImportError/ModuleNotFoundError)
encontrado durante la practica con matplotlib.
"""

print("=" * 70)
print("TASK 3: ModuleNotFoundError - Error de Modulo No Encontrado")
print("=" * 70)

# CODIGO CON ERROR:
"""
import matplotlb.pyplot as plt  # Error: nombre incorrecto del modulo
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = [np.sin(xi) for xi in x]

plt.plot(x, y)
plt.title('Onda Seno')
plt.show()
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_3.py
======================================================================
TASK 3: ModuleNotFoundError - Error de Modulo No Encontrado
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_8/Section_2/task_3.py", line 17, in <module>
    import matplotlb.pyplot as plt  # Error: nombre incorrecto del modulo
ModuleNotFoundError: No module named 'matplotlb'
"""

# Causa: Error tipografico en el nombre del modulo matplotlib

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: ModuleNotFoundError")
print("Causa: Error tipografico en el nombre del modulo")
print("Mensaje: ModuleNotFoundError: No module named 'matplotlb'")
print("Este error ocurre cuando Python no puede encontrar el modulo")
print("que se intenta importar. En este caso, el error es tipografico:")
print("  - Incorrecto: 'matplotlb' (falta 'i')")
print("  - Correcto: 'matplotlib'")
print()
print("Otros escenarios comunes de este error:")
print("1. El modulo no esta instalado en el entorno")
print("2. Error tipografico en el nombre del modulo")
print("3. El modulo esta instalado en otro entorno virtual")
print()
print("Soluciones:")
print("1. Corregir el nombre del modulo")
print("2. Instalar el modulo: pip install matplotlib")
print("3. Verificar el entorno virtual activo")

print("-" * 70)

# CODIGO CORREGIDO:
print("\nSolucion: Corregir el nombre del modulo")
print("-" * 70)

try:
    import matplotlib.pyplot as plt  # Nombre corregido
    import numpy as np
    
    print("Modulos importados exitosamente:")
    print(f"  - matplotlib version: {plt.matplotlib.__version__}")
    print(f"  - numpy version: {np.__version__}")
    
    print("\nCreando grafica de prueba...")
    x = np.linspace(0, 2 * np.pi, 100)
    y = [np.sin(xi) for xi in x]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color='#2E86AB', linewidth=2)
    ax.set_title('Onda Seno - Importacion Correcta', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('X (radianes)', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
    
    plt.tight_layout()
    plt.show()
    
    print("Grafica mostrada exitosamente.")
    
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    print("Por favor instala matplotlib: pip install matplotlib")
