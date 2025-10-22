# task_6.py
# Ejemplo del método .replace()
# Team 6
# Alejandro Campos Martínez
# Agustín Jaime Navarro

# Explicación del método .sort() aplicado a listas
"""
El método .replace() reemplaza todas las ocurrencias de un substring
por otro substring dentro de un string.

Sintaxis: str.replace(old, new, count=-1)

Parámetros:
- old: substring que se quiere reemplazar
- new: substring de reemplazo
- count: número máximo de reemplazos (opcional, default=-1 = todos)

Retorna: un nuevo string con los reemplazos (NO modifica el original)
"""

# Ejemplo 1: Reemplazo simple
texto = "Querida Chepita, te escribo desde un domingo lento y lleno de lluvia."
print(f"Original: '{texto}'")
nuevo_texto = texto.replace("domingo", "lunes").replace("lluvia", "luz")
print(f"Después de replace: '{nuevo_texto}'")
print(f"Original sin cambios: '{texto}'\n")

# Ejemplo 2: Reemplazo con límite
frase = "Te pienso, te sueño, te invento, te pienso otra vez."
print(f"Original: '{frase}'")
resultado = frase.replace("te", "nos", 2)
print(f"Reemplazar solo 2 veces: '{resultado}'\n")

# Ejemplo 3: Eliminar un sentimiento (reemplazo vacío)
fragmento = "Hay distancia, hay silencio, hay algo que no se dice."
print(f"Original: '{fragmento}'")
sin_silencio = fragmento.replace("silencio, ", "")
print(f"Sin 'silencio': '{sin_silencio}'\n")

# Ejemplo 4: Reemplazos encadenados
texto_corto = "A veces pienso en ti, y el reloj se detiene."
print(f"Texto original: '{texto_corto}'")
texto_transformado = texto_corto.replace("pienso", "recuerdo").replace("reloj", "tiempo")
print(f"Reemplazos encadenados: '{texto_transformado}'\n")

# Ejemplo 5: Case-sensitive
texto_case = "Chepita chepita CHEPITA"
print(f"Original: '{texto_case}'")
resultado_case = texto_case.replace("chepita", "ausencia")
print(f"Replace (case-sensitive): '{resultado_case}'\n")

# Ejemplo 6: Transformación
cita = "Te escribo sin papel, porque lo que digo no cabe en palabras."
print(f"Cita original: '{cita}'")
version_poetica = cita.replace("escribo", "pienso").replace("palabras", "silencios")
print(f"Versión transformada: '{version_poetica}'\n")

print("=========================================================================================")
print("Conclusión:")
print("- El método .replace() devuelve una nueva cadena sin modificar la original.")
print("- Su comportamiento es case-sensitive, distingue entre mayúsculas y minúsculas.")
print("- Permite definir un número máximo de reemplazos mediante el parámetro count.")
print("- Es útil para limpiar, formatear o transformar datos en texto.")
print("- Se puede encadenar para aplicar varios reemplazos en una sola instrucción.")
print("- Es una herramienta básica en la manipulación de strings dentro de Python.")
print("")
# Referencias
print("Referencia:")
print("Benedetti, M. (2022). Cartas a Chepita (1946-1948). Alfaguara.")
