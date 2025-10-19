# task_9.py
# Sección 3. Detección de Errores
# Alejandro Campos Martínez
# SyntaxError

"""
En este archivo se documenta errores de sintaxis (SyntaxError) 
encontrado durante la práctica.
"""

print("===============================================")
print("Error: SyntaxError - Paréntesis sin cerrar")
print("===============================================")

# El siguiente código genera un SyntaxError:

"""
#Código incorrecto:
print("Los cronopios son seres desordenados y felices"
"""

# Si descomentamos la línea anterior, Python muestra:
"""
MENSAJE DE ERROR:
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_9.py
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_9.py", line 19
    print("Los cronopios son seres desordenados y felices"
         ^
SyntaxError: '(' was never closed
"""

# Explicación del error
print("")
print("Explicación:")
print("------------------------------------------------------------------")
print("Causa:")
print("  - La función print() requiere que se cierre el paréntesis")
print("  - Python esperaba encontrar ')' antes del final de la línea")
print("  - Este error se detecta ANTES de ejecutar el programa")
print("Tipo de error:")
print("  - SyntaxError: error de sintaxis detectado por el parser")
print("Dónde ocurre:")
print("  - En tiempo de parseo (antes de la ejecución)")

# Solución
print("")
print("Solución:")
print("===================================================================")
print("Agregar el paréntesis de cierre al final de la línea")
print("Código corregido:")
print("===================================================================")

# Código corregido:
print("Los cronopios son seres desordenados y felices")

print("===============================================")
print("Error corregido")
print("===============================================")

# errores de SyntaxError
print("")
print("Errores que se presentaron de SyntaxError:")
print("---------------------------------------------------------------------------")

# Error: Comillas sin cerrar
print("")
print("Comillas sin cerrar:")
print("   Incorrecto: mensaje = 'Hola mundo")
print("   Correcto:   mensaje = 'Hola mundo'")

# Error: Dos puntos faltantes
print("")
print("Dos puntos faltantes en if:")
print("   Incorrecto: if x > 5")
print("   Correcto:   if x > 5:")

# Error: Indentación incorrecta
print("")
print("Indentación incorrecta:")
print("   Incorrecto:")
print("   def funcion():")
print("   return 5  # Sin indentación")
print("   Correcto:")
print("   def funcion():")
print("       return 5")