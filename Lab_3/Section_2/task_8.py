# task_8.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# ERROR: KeyError

"""
Se documenta un error de clave (KeyError)
encontrado durante la práctica.
"""

print("=" * 70)
print("ERROR: KeyError - Acceso a clave inexistente en diccionario")
print("=" * 70)

# El siguiente código generó un KeyError:
# Código incorrecto:
"""
estudiantes = {
    "Ana": 95,
    "Carlos": 87,
    "María": 92
}
nota = estudiantes["Pedro"]
print(nota)
"""

# En la ejecución del código anterior, Python mostró:
"""
Mensaje de error en la consola:

(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_8.py
======================================================================
ERROR: KeyError - Acceso a clave inexistente en diccionario
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_8.py", line 22, in <module>
    nota = estudiantes["Pedro"]
KeyError: 'Pedro'
"""

# Explicación del error
print("")
print("EXPLICACIÓN:")
print("-" * 70)
print("Causa:")
print("- Se intentó acceder a la clave 'Pedro' que no existe en el diccionario")
print("- Las claves en Python son case-sensitive (distinguen mayúsculas)")
print("- Acceder a una clave inexistente genera KeyError")
print("")
print("Demostración con el diccionario:")
estudiantes = {
    "Ana": 95,
    "Carlos": 87,
    "María": 92
}
print(f"   Diccionario: {estudiantes}")
print("   Claves disponibles:", list(estudiantes.keys()))
print("   'Pedro' NO está en las claves disponibles")
print("")
print("Tipo de error:")
print("- KeyError: clave no encontrada en el diccionario")
print("")
print("Dónde ocurre:")
print("- En tiempo de ejecución (runtime)")

# Solución
print("")
print("SOLUCIÓN:")
print("-" * 70)
print("")
print("Opción 1 - Verificar existencia de clave con 'in':")
print("-" * 70)
clave = "Pedro"
if clave in estudiantes:
    print(f"   Nota de {clave}: {estudiantes[clave]}")
else:
    print(f"   '{clave}' no está en el diccionario")

print("")
print("Opción 2 - Usar método .get() con valor por defecto:")
print("-" * 70)
nota = estudiantes.get("Pedro", "No encontrado")
print(f"   Nota de Pedro: {nota}")
nota_ana = estudiantes.get("Ana", "No encontrado")
print(f"   Nota de Ana: {nota_ana}")

print("")
print("Opción 3 - Usar .get() con None:")
print("-" * 70)
nota = estudiantes.get("Pedro")
if nota is None:
    print("   Pedro no está registrado")
else:
    print(f"   Nota: {nota}")

print("")
print("Opción 4 - Usar try-except:")
print("-" * 70)
try:
    nota = estudiantes["Pedro"]
    print(f"   Nota: {nota}")
except KeyError:
    print("   Error capturado: Pedro no está en el diccionario")

print("")
print("=" * 70)
print("Error corregido")
print("=" * 70)

# Errores presentados de KeyError
print("")
print("Errores de KeyError:")
print("-" * 70)

# Error 1: Case sensitivity
print("")
print("1. Sensibilidad a mayúsculas/minúsculas:")
try:
    nota = estudiantes["ana"]  # minúscula
except KeyError as e:
    print(f"   Error: {e}")
    print("   'ana' != 'Ana' - Las claves son case-sensitive")
    print(f"   Correcto: estudiantes['Ana'] = {estudiantes['Ana']}")

# Error 2: Espacios en claves
print("")
print("2. Espacios en nombres de claves:")
diccionario = {"clave": "valor"}
try:
    valor = diccionario["clave "]  # espacio al final
except KeyError as e:
    print(f"   Error: {e}")
    print("   'clave ' != 'clave' - Los espacios importan")

# Error 3: Tipo de clave incorrecto
print("")
print("3. Usar tipo incorrecto de clave:")
numeros = {1: "uno", 2: "dos", 3: "tres"}
try:
    valor = numeros["1"]  # string en lugar de int
except KeyError as e:
    print(f"   Error: {e}")
    print("   '1' (string) != 1 (entero)")
    print(f"   Correcto: numeros[1] = '{numeros[1]}'")

# Error 4: Clave eliminada
print("")
print("4. Intentar acceder a clave eliminada:")
temp_dict = {"a": 1, "b": 2}
del temp_dict["b"]
try:
    valor = temp_dict["b"]
except KeyError as e:
    print(f"   Error: {e}")
    print("   La clave 'b' fue eliminada del diccionario")
