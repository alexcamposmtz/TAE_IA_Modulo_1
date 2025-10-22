# task_5.py
# Explicación del método .sort() aplicado a listas
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6


"""
El método .sort() ordena los elementos de una lista in-place (modifica la lista original).

Sintaxis: lista.sort(key=None, reverse=False)

Parámetros:
- key: función que se aplica a cada elemento antes de comparar (opcional)
- reverse: si es True, ordena en orden descendente (opcional, default=False)

Nota: .sort() modifica la lista original y retorna None
"""

# Ejemplo 1: Ordenar números de forma ascendente
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {numeros}")
numeros.sort()
print(f"Después de .sort(): {numeros}\n")

# Ejemplo 2: Ordenar en orden descendente
numeros2 = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {numeros2}")
numeros2.sort(reverse=True)
print(f"Orden descendente: {numeros2}\n")

# Ejemplo 3: Ordenar strings alfabéticamente
frutas = ["guanabana", "platano", "nanchi", "guayaba", "lima"]
print(f"Lista original: {frutas}")
frutas.sort()
print(f"Orden alfabético: {frutas}\n")

# Ejemplo 4: Ordenar por longitud usando key
palabras = ["Universidad", "Autonoma", "de", "Nayarit", "Amado", "Nervo"]
print(f"Lista original: {palabras}")
palabras.sort(key=len)
print(f"Ordenado por longitud: {palabras}\n")

# Ejemplo 5: Ordenar strings ignorando mayúsculas/minúsculas
nombres = ["carlos", "Ana", "JUAN", "maría"]
print(f"Lista original: {nombres}")
nombres.sort(key=str.lower)
print(f"Ordenado (case-insensitive): {nombres}\n")

# Ejemplo 6: Diferencia entre .sort() y sorted()
numeros3 = [5, 2, 8, 1, 9]
print(f"Lista original: {numeros3}")
resultado = numeros3.sort()
print(f".sort() retorna: {resultado}")
print(f"Lista después de .sort(): {numeros3}\n")

print("="*50)
print("CONCLUSIÓN:")
print("- .sort() modifica la lista original")
print("- Retorna None (no devuelve una nueva lista)")
print("- Es más eficiente en memoria que sorted()")

