# task_10.py
# Sección 3. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6


# ERROR: TypeError

"""
En este archivo se documenta un error de tipo (TypeError) 
encontrado durante la práctica.
"""

print("===========================================================")
print("ERROR: TypeError - Concatenación de string con entero")
print("============================================================")

# El siguiente código genero un TypeError:



#Código incorrecto:
"""
Edad_cronopio = 25
mensaje = "El cronopio tiene " + edad_cronopio + " años de alegría"
print(mensaje)
"""

# En la ejecución el código anterior, Python mostró:
"""
Mensaje de error en la consola:
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_10.py
===========================================================
ERROR 2: TypeError - Concatenación de string con entero
============================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_10.py", line 23, in <module>
    mensaje = "El cronopio tiene " + edad_cronopio + " años de alegría"
NameError: name 'edad_cronopio' is not defined. Did you mean: 'Edad_cronopio'?
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ 
"""

# Explicación del error
print("")
print("EXPLICACIÓN:")
print("---------------------------------------------------------------------------")
print("Causa:")
print("- Se intentó concatenar un string con un entero usando el operador '+'")
print("- Python no puede mezclar tipos incompatibles en concatenación")
print("- El operador '+' tiene diferentes significados según el tipo:")
print("  - Para strings: concatenación")
print("  - Para números: suma aritmética")
print("")
print("Tipo de error:")
print("- TypeError: operación no soportada entre tipos incompatibles")
print("Dónde ocurre:")
print("- En tiempo de ejecución (runtime)")

# Solución
print("")
print("SOLUCION:")
print("---------------------------------------------------------------------------")

# Solución: Usar str() para convertir
print("")
print("Conversión con str():")
print("---------------------------------------------------------------------------")

edad_cronopio = 25
mensaje = "El cronopio tiene " + str(edad_cronopio) + " años de alegría"
print("   " + mensaje)


print("============================================================")
print("Error corregido")
print("============================================================")

# Errores TypeError
print("")
print("Errores TypeError:")
print("---------------------------------------------------------------------------")

# error: Sumar string con número
print("")
print("Intentar sumar string con número:")
try:
    resultado = "5" + 3
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: int('5') + 3 = ", int("5") + 3)

# Error: Usar operador no soportado
print("")
print("Multiplicar string por float:")
try:
    texto = "hola" * 2.5
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: 'hola' * 2 = ", "hola" * 2)

#  Error: Función con argumentos incorrectos
print("")
print("Pasar tipo incorrecto a una función:")
try:
    numeros = [1, 2, 3]
    numeros.append(4, 5)  # append() solo acepta 1 argumento
except TypeError as e:
    print(f"   Error: {e}")
    print("   Correcto: usar .extend([4, 5]) o dos .append()")
