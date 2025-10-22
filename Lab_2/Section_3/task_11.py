# task_11.py
# Sección 3. Detección de Errores
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# ERROR 3: IndexError

"""
En este archivo se documenta un error de índice (IndexError) 
encontrado durante la práctica.
"""

print("="*60)
print("ERROR 3: IndexError - Índice fuera de rango")
print("="*60)

# Código con error
# El siguiente código generó un IndexError:


#Codigo incorrecto:
"""
cronopios = ["verde", "torpe", "feliz"]
print(cronopios[3])  # Intenta acceder al cuarto elemento
"""

# Si ejecutamos el código anterior, Python muestra:
"""
MENSAJE DE ERROR:

(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ /bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_11
============================================================
ERROR 3: IndexError - Índice fuera de rango
============================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2/Section_3/task_11", line 22, in <module>
    print(cronopios[3])  # Intenta acceder al cuarto elemento
IndexError: list index out of range
(base) xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_2$ 
"""

# Explicación del error
print("")
print("Explicación:")
print("------------------------------------------------------------------")
print("Causa:")
print("  - Se intentó acceder a un índice que no existe en la lista")
print("  - La lista tiene 3 elementos con índices: 0, 1, 2")
print("  - Se intentó acceder al índice 3 (cuarto elemento)")
print("  - En Python, los índices comienzan en 0, no en 1")
print("Tipo de error:")
print("  - IndexError: índice de secuencia fuera de rango")
print("Dónde ocurre:")
print("  - En tiempo de ejecución (runtime)")

print("ESTRUCTURA DE LA LISTA:")
print("------------------------------------------------------------------")
print("  Índice:      0         1        2")
print("  Valor:   [verde]   [torpe]  [feliz]")
print("            válido    válido   válido")
print("\n  Índice 3: ¡NO EXISTE! → IndexError")

# solución
print("=============================================")
print("SOLUCION:")
print("=============================================")

# Solución: Usar índice válido
print("Usar un índice válido (0 a 2):")
print("   " + "-" * 56)
cronopios = ["verde", "torpe", "feliz"]
print(f"   cronopios[0] = {cronopios[0]}")
print(f"   cronopios[1] = {cronopios[1]}")
print(f"   cronopios[2] = {cronopios[2]}")

# Solución: Usar índices negativos
print("Usar índices negativos (desde el final):")
print("   " + "-" * 56)
print(f"   cronopios[-1] = {cronopios[-1]}  # Último elemento")
print(f"   cronopios[-2] = {cronopios[-2]}  # Penúltimo")
print(f"   cronopios[-3] = {cronopios[-3]}  # Antepenúltimo")

# Solución: Verificar longitud antes de acceder
print("")
print("Verificar longitud antes de acceder:")
print("----------------------------------------------------------")

indice = 3
if indice < len(cronopios):
    print(f"   cronopios[{indice}] = {cronopios[indice]}")
else:
    print(f"   Error: índice {indice} fuera de rango")
    print(f"   La lista solo tiene {len(cronopios)} elementos")
    print(f"   Índices válidos: 0 a {len(cronopios)-1}")

# Solución: try-except
print("Usar manejo de excepciones (try-except):")
print("----------------------------------------------------------")
try:
    print(f"   Intentando acceder a cronopios[3]...")
    elemento = cronopios[3]
    print(f"   cronopios[3] = {elemento}")
except IndexError:
    print(f"   IndexError capturado")
    print(f"   Usando el último elemento en su lugar:")
    print(f"   cronopios[-1] = {cronopios[-1]}")

print("=============================================")
print("Error corregido")
print("=============================================")

# Errores de IndexError
print("")
print("Errores IndexError:")
print("----------------------------------------------------------")

# Lista vacía
print("")
print("Acceder a una lista vacía:")
lista_vacia = []
try:
    elemento = lista_vacia[0]
except IndexError as e:
    print(f"   Error: {e}")
    print("   Solución: verificar if lista_vacia antes de acceder")

# Error con .pop()
print("")
print("Usar .pop() en índice inválido:")
famas = ["ordenado", "preciso"]
try:
    famas.pop(5)
except IndexError as e:
    print(f"   Error: {e}")
    print(f"   Correcto: famas.pop(1) = {famas[1]}")

# Slicing vs indexing
print("")
print("Diferencia entre slicing e indexing:")
esperanzas = ["calma", "paciencia"]
try:
    print(f"   esperanzas[5] → IndexError")
    elemento = esperanzas[5]
except IndexError as e:
    print(f"   Error: {e}")
print(f"   esperanzas[5:] → {esperanzas[5:]} (slicing no genera error)")
