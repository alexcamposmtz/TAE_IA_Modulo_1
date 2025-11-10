# task_8.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

"""
Se documenta un error de importación (ImportError / ModuleNotFoundError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 8: ImportError - Error de Importacion")
print("=" * 70)

# CODIGO CON ERROR:
"""
import geometria_pakage
resultado = geometria_package.area_circulo(5)
"""

# Error:

"""
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_8.py
======================================================================
TASK 8: ImportError - Error de Importacion
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_8.py", line 18, in <module>
    import geometria_pakage
ModuleNotFoundError: No module named 'geometria_pakage'
"""
# Causa: El nombre del paquete esta mal escrito

# CODIGO CON ERROR:
# from geometria_package import area_cuadrada  # Nombre incorrecto
# resultado = area_cuadrada(5)

# Error: ImportError: cannot import name 'area_cuadrada' from 'geometria_package'
# Causa: La funcion se llama 'area_cuadrado', no 'area_cuadrada'

# CODIGO CON ERROR:
# Si falta el archivo __init__.py en geometria_package:
# from geometria_package import area_circulo

# Error: ModuleNotFoundError: No module named 'geometria_package'
# Causa: Sin __init__.py, Python no reconoce la carpeta como paquete

print("Explicacion de los errores:")
print("-" * 70)
print("ERROR 1: Nombre de paquete incorrecto")
print("  Causa: Ortografia incorrecta del paquete")
print("  Mensaje: ModuleNotFoundError: No module named 'geometria_package_mal_escrito'")
print()
print("ERROR 2: Nombre de funcion incorrecto")
print("  Causa: La funcion 'area_cuadrado' fue escrita como 'area_cuadrada'")
print("  Mensaje: ImportError: cannot import name 'area_cuadrada'")
print()
print("ERROR 3: Falta __init__.py")
print("  Causa: El archivo __init__.py no existe en geometria_package/")
print("  Mensaje: ModuleNotFoundError o (unknown location)")
print("  ESTO ES LO QUE TE PASO ANTES!")
print()
print("ERROR 4: Importar desde modulo equivocado")
print("  Causa: Intentar importar multiplicacion_matrices desde areas.py")
print("  Mensaje: ImportError: cannot import name 'multiplicacion_matrices' from 'areas'")
print("-" * 70)

# CODIGO CORREGIDO - Importaciones correctas
print("=" * 70)
print("SOLUCIONES")
print("=" * 70)

print("Solucion - Importar modulos individuales (como en task_3):")
import sys
import os
# Agregar directorio para encontrar los modulos
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'section_1'))

try:
    import areas
    import matrices
    print("Importacion de modulos areas y matrices")
    print(f"Funciones en areas: area_circulo, area_cuadrado, area_triangulo, area_hexagono")
    print(f"Funciones en matrices: suma, resta, multiplicacion")
except ImportError as e:
    print(f"Error al importar modulos: {e}")