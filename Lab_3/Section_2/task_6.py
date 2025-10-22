# task_6.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# ERROR: TypeError
"""
Se documenta un error de tipo (TypeError)
encontrado durante la práctica.
"""

print("=" * 70)
print("ERROR: TypeError - Concatenación de string con entero")
print("=" * 70)

# El siguiente código generó un TypeError:
# Código incorrecto:
"""
edad = 25
mensaje = "Tengo " + edad + " años"
print(mensaje)
"""

# En la ejecución del código anterior, Python mostró:
"""
Mensaje de error en la consola:

(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_6.py
======================================================================
ERROR: TypeError - Concatenación de string con entero
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_6.py", line 18, in <module>
    mensaje = "Tengo " + edad + " años"
TypeError: can only concatenate str (not "int") to str
"""

# Explicación del error
print("")
print("EXPLICACIÓN:")
print("-" * 70)
print("Causa:")
print("- Se intentó concatenar un string con un entero usando el operador '+'")
print("- Python no puede mezclar tipos incompatibles en concatenación")
print("- El operador '+' tiene diferentes significados según el tipo:")
print("  • Para strings: concatenación")
print("  • Para números: suma aritmética")
print("")
print("Tipo de error:")
print("- TypeError: operación no soportada entre tipos incompatibles")
print("")
print("Dónde ocurre:")
print("- En tiempo de ejecución (runtime)")

# Solución
print("")
print("SOLUCIÓN:")
print("-" * 70)
print("")
print("Opción 1 - Conversión con str():")
print("-" * 70)
edad = 25
mensaje = "Tengo " + str(edad) + " años"
print("   " + mensaje)

print("")
print("Opción 2 - Usar f-strings (recomendado):")
print("-" * 70)
mensaje = f"Tengo {edad} años"
print("   " + mensaje)

print("")
print("Opción 3 - Usar format():")
print("-" * 70)
mensaje = "Tengo {} años".format(edad)
print("   " + mensaje)

print("")
print("=" * 70)
print("Error corregido")
print("=" * 70)

# Errores de TypeError que se nos presentarón
print("")
print("Errores de TypeError:")
print("-" * 70)

# Error 1: Sumar string con número
print("")
print("1. Intentar sumar string con número:")
try:
    resultado = "5" + 3
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: int('5') + 3 =", int("5") + 3)

# Error 2: Multiplicar string por float
print("")
print("2. Multiplicar string por float:")
try:
    texto = "hola" * 2.5
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: 'hola' * 2 =", "hola" * 2)

# Error 3: Función con tipo incorrecto de argumento
print("")
print("3. Pasar tipo incorrecto a una función:")
try:
    numeros = [1, 2, 3]
    numeros.append(4, 5)  # append() solo acepta 1 argumento
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: usar .extend([4, 5]) o dos .append()")

# Error 4: Indexar con tipo incorrecto
print("")
print("4. Usar índice no entero:")
try:
    lista = [10, 20, 30]
    elemento = lista["1"]
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: lista[1] =", lista[1])
