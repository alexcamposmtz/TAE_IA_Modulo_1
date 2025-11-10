# task_5.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

"""
Se documenta un error de sintaxis (SyntaxError)
encontrado durante la práctica.
"""

import math

print("=" * 70)
print("TASK 5: SyntaxError - Error de Sintaxis")
print("=" * 70)

# CODIGO CON ERROR:
"""
def area_circulo(radio=None):
    if radio is None:
        radio = 1.0
        print("AVISO: Usando valor por defecto para el radio: 1.0"
    area = math.pi * radio ** 2
    return area
"""
# Error presentado:
"""
base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_5.py
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_5.py", line 22
    print("AVISO: Usando valor por defecto para el radio: 1.0"
         ^
SyntaxError: '(' was never closed
"""

# Causa: Falta el parentesis de cierre en la linea del print


print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: SyntaxError")
print("Causa: Falta cerrar el parentesis en la funcion print()")
print("Mensaje: SyntaxError: '(' was never closed")
print("Este es un error comun al escribir funciones como las de")
print("nuestro modulo areas.py")
print("Solucion:")
print("Agregar el parentesis de cierre:")
print('print("AVISO: Usando valor por defecto para el radio: 1.0")')

print("-" * 70)

# CODIGO CORREGIDO:
def area_circulo(radio=None):
    """Calcula el area de un circulo"""
    if radio is None:
        radio = 1.0
        print("AVISO: Usando valor por defecto para el radio: 1.0")
    area = math.pi * radio ** 2
    return area

print("Prueba con codigo corregido:")
print("Calculando area de circulo con radio por defecto...")
resultado = area_circulo()
print(f"Area: {resultado:.2f}")

print("\nCalculando area de circulo con radio 5...")
resultado = area_circulo(5)
print(f"Area: {resultado:.2f}")


# Ejemplo adicional con matriz
print("\nEjemplo adicional - Error en definicion de matriz:")
print("Incorrecto: matriz = [[1, 2, 3, [4, 5, 6]  # Falta cerrar corchetes")
print("Correcto:   matriz = [[1, 2, 3], [4, 5, 6]]")
matriz = [[1, 2, 3], [4, 5, 6]]
print(f"Matriz correcta: {matriz}")
print("=" * 70)
