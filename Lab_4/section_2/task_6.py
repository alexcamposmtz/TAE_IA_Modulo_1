# task_6.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

"""
Se documenta un error de tipo (TypeError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 6: TypeError - Error de Tipo")
print("=" * 70)

# CODIGO CON ERROR:
"""
def area_triangulo(base=None, altura=None):
     if base is None:
         base = 1.0
     if altura is None:
         altura = 1.0
     area = (base * altura) / 2  # Error aqui si altura es string
     return area
# 
resultado = area_triangulo(10, "5")  # altura es string!
print(f"Area: {resultado}")
"""
# Error presentado:
"""
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_6.py
======================================================================
TASK 6: TypeError - Error de Tipo
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_6.py", line 19, in <module>
    resultado = area_triangulo(10, "5")  # altura es string!
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_4/section_2/task_6.py", line 16, in area_triangulo
    area = (base * altura) / 2  # Error aqui si altura es string
TypeError: unsupported operand type(s) for /: 'str' and 'int'
"""
# Causa: Intentar multiplicar un numero (float) con un string

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: TypeError")
print("Causa: Intentar multiplicar float * str en la formula del area")
print("Mensaje: TypeError: unsupported operand type(s) for *: 'float' and 'str'")
print("Esto puede ocurrir si:")
print("- Los datos vienen de input() sin convertir")
print("- Se leen datos de archivo sin procesar")
print("- Se confunde el tipo de dato en matrices")
print("Soluciones:")
print("1. Convertir explicitamente: float(altura)")
print("2. Validar tipos antes de calcular")
print("3. Usar try-except para capturar el error")
print("-" * 70)

# CODIGO CORREGIDO - Opcion 1: Conversion explicita
print("Solucion 1 - Conversion explicita con float():")

def area_triangulo_v1(base=None, altura=None):
    """Calcula el area de un triangulo con conversion de tipos"""
    if base is None:
        base = 1.0
    if altura is None:
        altura = 1.0
    
    # Convertir a float para asegurar tipo correcto
    base = float(base)
    altura = float(altura)
    
    area = (base * altura) / 2
    return area

resultado = area_triangulo_v1(10, "5")  # Ahora funciona
print(f"Base: 10, Altura: '5' (string) -> Area: {resultado:.2f}")

# Error: intentar sumar matriz con numero directamente
print("Incorrecto: Intentar hacer matriz + 5 directamente")
print("Esto causa: TypeError: can only concatenate list (not 'int') to list")

matriz = [[1, 2], [3, 4]]
print(f"Matriz original: {matriz}")

# Correcto: Sumar 5 a cada elemento
print("Correcto: Sumar 5 a cada elemento de la matriz:")
matriz_sumada = [[elemento + 5 for elemento in fila] for fila in matriz]
print(f"Matriz + 5: {matriz_sumada}")
