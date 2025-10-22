# task_7.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# ERROR: IndexError
"""
Se documenta un error de índice (IndexError)
encontrado durante la práctica.
"""

print("=" * 70)
print("ERROR: IndexError - Acceso fuera de rango en lista")
print("=" * 70)

# El siguiente código generó un IndexError:
# Código incorrecto:
"""
numeros = [10, 20, 30, 40, 50]
print(numeros[5])
"""

# En la ejecución del código anterior, Python mostró:
"""
Mensaje de error en la consola:

(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_7
======================================================================
ERROR: IndexError - Acceso fuera de rango en lista
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_3/Section_2/task_7", line 18, in <module>
    print(numeros[5])
IndexError: list index out of range
"""

# Explicación del error
print("")
print("EXPLICACIÓN:")
print("-" * 70)
print("Causa:")
print("- Se intentó acceder al índice 5 en una lista de 5 elementos")
print("- Los índices válidos son: 0, 1, 2, 3, 4")
print("- Python usa indexación basada en 0 (zero-based indexing)")
print("")
print("Demostración con la lista:")
numeros = [10, 20, 30, 40, 50]
print(f"   Lista: {numeros}")
print(f"   Longitud: {len(numeros)} elementos")
print("   Índices válidos: 0 a", len(numeros) - 1)
print("")
for i in range(len(numeros)):
    print(f"   numeros[{i}] = {numeros[i]}")
print("")
print("Tipo de error:")
print("- IndexError: índice de lista fuera de rango")
print("")
print("Dónde ocurre:")
print("- En tiempo de ejecución (runtime)")

# Solución
print("")
print("SOLUCIÓN:")
print("-" * 70)
print("")
print("Opción 1 - Usar índice correcto:")
print("-" * 70)
print(f"   numeros[4] = {numeros[4]}")

print("")
print("Opción 2 - Usar índice negativo (desde el final):")
print("-" * 70)
print(f"   numeros[-1] = {numeros[-1]} (último elemento)")
print(f"   numeros[-2] = {numeros[-2]} (penúltimo)")

print("")
print("Opción 3 - Verificar longitud antes de acceder:")
print("-" * 70)
indice = 5
if indice < len(numeros):
    print(f"   numeros[{indice}] = {numeros[indice]}")
else:
    print(f"   Error evitado: índice {indice} fuera de rango")

print("")
print("Opción 4 - Usar try-except:")
print("-" * 70)
try:
    print(f"   numeros[5] = {numeros[5]}")
except IndexError:
    print("   Error capturado: índice fuera de rango")

print("")
print("=" * 70)
print("Error corregido")
print("=" * 70)

# Errores que se nos presentaron de IndexError
print("")
print("Erro de IndexError:")
print("-" * 70)

# Error 1: Loop con rango incorrecto
print("")
print("1. Loop con rango incorrecto:")
print("   Incorrecto: for i in range(len(lista)+1)")
print("   Correcto:   for i in range(len(lista))")

# Error 2: Lista vacía
print("")
print("2. Acceder a lista vacía:")
try:
    lista_vacia = []
    elemento = lista_vacia[0]
except IndexError as e:
    print(f"   Error: {e}")
    print("   Solución: verificar if len(lista) > 0")

# Error 3: String indexing
print("")
print("3. Índice en string:")
try:
    texto = "Python"
    letra = texto[10]
except IndexError as e:
    print(f"   Error: {e}")
    print(f"   Correcto: texto[0] = '{texto[0]}'")

# Error 4: Off-by-one error en loops
print("")
print("4. Error común en loops (off-by-one):")
lista = [1, 2, 3]
print("   Incorrecto:")
print("   for i in range(1, len(lista)+1):  # índices 1,2,3")
print("       print(lista[i])  # Error en i=3")
print("")
print("   Correcto:")
print("   for i in range(len(lista)):  # índices 0,1,2")
for i in range(len(lista)):
    print(f"       lista[{i}] = {lista[i]}")
