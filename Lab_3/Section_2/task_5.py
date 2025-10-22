# task_5.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# ERROR: SyntaxError
"""
Se documenta un error de sintaxis (SyntaxError)
encontrado durante la práctica.
"""

print("=" * 70)
print("ERROR: SyntaxError - Falta de dos puntos en estructura de control")
print("=" * 70)

# El siguiente código generó un SyntaxError:
# Código incorrecto:
"""
contador = 0
while contador < 5
    print(f"Iteración {contador}")
    contador += 1
"""

# En la ejecución del código anterior, Python mostró:
"""
Mensaje de error en la consola:

(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_5.py
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_5.py", line 18
    while contador < 5
                      ^
SyntaxError: expected ':'
"""

# Explicación del error
print("")
print("EXPLICACIÓN:")
print("-" * 70)
print("Causa:")
print("- Falta el símbolo de dos puntos ':' al final de la declaración while")
print("- Python requiere ':' en todas las estructuras de control")
print("- El ':' indica el inicio de un bloque de código indentado")
print("")
print("Tipo de error:")
print("- SyntaxError: sintaxis inválida")
print("")
print("Dónde ocurre:")
print("- En tiempo de parsing (antes de ejecutar)")
print("- Python no puede ni siquiera interpretar el código")

# Solución
print("")
print("SOLUCIÓN:")
print("-" * 70)
print("")
print("Código corregido con ':' al final:")
print("-" * 70)
contador = 0
while contador < 3:
    print(f"   Iteración {contador}")
    contador += 1

print("")
print("=" * 70)
print("Error corregido")
print("=" * 70)

# Errores que se nos presentaron de SyntaxError
print("")
print("Errores comunes de SyntaxError:")
print("-" * 70)

# if sin dos puntos
print("")
print("1. Estructura if sin dos puntos:")
print("   Incorrecto: if x > 5")
print("   Correcto:   if x > 5:")

# for sin dos puntos
print("")
print("2. Estructura for sin dos puntos:")
print("   Incorrecto: for i in range(10)")
print("   Correcto:   for i in range(10):")

# def sin dos puntos
print("")
print("3. Definición de función sin dos puntos:")
print("   Incorrecto: def mi_funcion()")
print("   Correcto:   def mi_funcion():")

# Falta de paréntesis 
print("")
print("4. Falta de Paréntesis:")
print("   Incorrecto: resultado = (5 + 3")
print("   Correcto:   resultado = (5 + 3)")

# Comillas sin cerrar
print("")
print("5. Comillas sin cerrar:")
print("   Incorrecto: texto = 'Hola mundo")
print("   Correcto:   texto = 'Hola mundo'")
