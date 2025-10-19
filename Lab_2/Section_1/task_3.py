# task_3.py
# Sección 1. Práctica de programación
# Alejandro Campos Martínez

# Definir lista de ejemplo
numeros = [45, 12, 89, 23, 67, 34, 91, 5, 78]
print(f"Lista original: {numeros}\n")

# MÁXIMO: Ordenar y tomar el último
lista_max = numeros.copy()
lista_max.sort()
maximo = lista_max.pop()  # Último elemento (el mayor)
print(f"Elemento máximo: {maximo}")

# MÍNIMO: Ordenar y tomar el primero
lista_min = numeros.copy()
lista_min.sort()
minimo = lista_min.pop(0)  # Primer elemento (el menor)
print(f"Elemento mínimo: {minimo}")

# LONGITUD: Contar con pop()
lista_len = numeros.copy()
longitud = 0
while lista_len:
    lista_len.pop()
    longitud += 1
print(f"Longitud de la lista: {longitud}")

print("\n" + "="*50)
print("MÉTODOS UTILIZADOS:")
print("- .copy(): crea una copia de la lista")
print("- .sort(): ordena la lista in-place")
print("- .pop(): elimina y retorna elementos")
