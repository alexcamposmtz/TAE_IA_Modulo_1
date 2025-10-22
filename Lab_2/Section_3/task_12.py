# task_12.py
# Sección 3. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# ERROR: KeyError

"""
En este archivo se documenta un error de clave (KeyError) 
encontrado durante la práctica.
"""

print("============================================================")
print("ERROR: KeyError - Clave no existe en diccionario")
print("============================================================")

# ========== CÓDIGO CON ERROR ==========
# El siguiente código genera un KeyError:

"""
CÓDIGO INCORRECTO:
------------------

cronopio = {
    "nombre": "Cronopito",
    "edad": 25,
    "color": "verde"
}
print(cronopio["profesion"])  # Intenta acceder a una clave que no existe
"""

# Si ejecutamos el código anterior, Python muestra:
"""
MENSAJE DE ERROR:

(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_12.py
============================================================
ERROR: KeyError - Clave no existe en diccionario
============================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_12.py", line 27, in <module>
    print(cronopio["profesion"])  # Intenta acceder a una clave que no existe
KeyError: 'profesion'
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ 
"""

# Explicación del error
print("EXPLICACIÓN:")
print("----------------------------------------------------------------------")
print("Causa:")
print("  - Se intentó acceder a la clave 'profesion' en el diccionario")
print("  - Esta clave NO existe en el diccionario")
print("  - Las claves disponibles son: nombre, edad, color")
print("  - Python no puede devolver un valor para una clave inexistente")
print("Tipo de error:")
print("  - KeyError: clave no encontrada en el diccionario")
print("Dónde ocurre:")
print("  - En tiempo de ejecución (runtime)")

print("ESTRUCTURA DEL DICCIONARIO:")
print("----------------------------------------------------------------------")
cronopio = {
    "nombre": "Cronopito",
    "edad": 25,
    "color": "verde"
}
print("  cronopio = {")
for clave, valor in cronopio.items():
    print(f"      '{clave}': '{valor}',")
print("  }")
print("   Claves válidas: nombre, edad, color")
print("   'profesion' NO existe → KeyError")

# Solución
print("============================================================")
print("SOLUCIONES:")
print("============================================================")

# Solución 1: Verificar si la clave existe
print("Verificar si la clave existe con 'in':")
print("   " + "-" * 56)
if "profesion" in cronopio:
    print(f"   Profesión: {cronopio['profesion']}")
else:
    print("   La clave 'profesion' no existe en el diccionario")
    print("   Alternativa: asignar un valor por defecto")
    print("   Profesión: Desconocida")

# Solución 2: Usar .get() (retorna None si no existe)
print(". Usar el método .get() (retorna None si no existe):")
print("   " + "-" * 56)
profesion = cronopio.get("profesion")
print(f"   cronopio.get('profesion') = {profesion}")
print("   Nota: retorna None sin generar error")

# Solución 3: Usar .get() con valor por defecto
print("Usar .get() con valor por defecto:")
print("   " + "-" * 56)
profesion = cronopio.get("profesion", "Ser cronopio")
print(f"   cronopio.get('profesion', 'Ser cronopio') = {profesion}")
print("   Nota: retorna el valor por defecto si la clave no existe")

# Solución 4: Usar try-except
print("Usar manejo de excepciones (try-except):")
print("   " + "-" * 56)
try:
    print(f"   Intentando acceder a cronopio['profesion']...")
    profesion = cronopio["profesion"]
    print(f"   Profesión: {profesion}")
except KeyError:
    print(f"   KeyError capturado")
    print(f"   Usando valor por defecto:")
    print(f"   Profesión: Alegre desorganizado")

# Solución 5: Agregar la clave al diccionario
print("\n5. Agregar la clave antes de acceder:")
print("   " + "-" * 56)
cronopio["profesion"] = "Cronopista profesional"
print(f"   Agregado: 'profesion': '{cronopio['profesion']}'")
print(f"   Ahora sí se puede acceder: {cronopio['profesion']}")

print("============================================================")
print("Error corregido")
print("============================================================")

# Errores KeyError
print("============================================================")
print("Errores  KeyError:")
print("============================================================")

# Error: Error tipográfico en la clave
print("Error tipográfico en el nombre de la clave:")
fama = {"nombre": "Famito", "edad": 30}
try:
    print(f"   fama['nobre'] → KeyError (falta 'm')")
    nombre = fama["nobre"]
except KeyError as e:
    print(f"   Error: KeyError: {e}")
    print(f"   Correcto: fama['nombre'] = {fama['nombre']}")

# Error:: Mayúsculas/minúsculas
print("Las claves distinguen mayúsculas/minúsculas:")
esperanza = {"tipo": "paciente"}
try:
    print(f"   esperanza['Tipo'] → KeyError")
    tipo = esperanza["Tipo"]
except KeyError as e:
    print(f"   Error: KeyError: {e}")
    print(f"   Correcto: esperanza['tipo'] = {esperanza['tipo']}")

# Error: .pop() con clave inexistente
print("Usar .pop() con clave inexistente:")
datos = {"a": 1, "b": 2}
try:
    print(f"   datos.pop('c') → KeyError")
    valor = datos.pop("c")
except KeyError as e:
    print(f"   Error: KeyError: {e}")
    print(f"   Correcto: datos.pop('c', 0) = {datos.pop('c', 0)} (con default)")
