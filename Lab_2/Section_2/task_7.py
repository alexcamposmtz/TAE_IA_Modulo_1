# task_7_cronopios.py
# Alejandro Campos Martínez
# Explicación de la expresión s *= n (con cronopios, famas y esperanzas)

"""
La expresión s *= n significa:
Repetir la secuencia s, n veces, y actualizar s con el resultado.

Es equivalente a escribir:
    s = s * n

Para secuencias mutables (como las listas), modifica el objeto en el mismo lugar.
Para secuencias inmutables (como los strings), crea un nuevo objeto.

El valor de n debe ser un entero. Puede ser cero o negativo.

Nota:
Aunque algunos manuales mencionan límites como "entre 0 y 255",
en Python no existe tal restricción. Funcionará con cualquier entero.
"""

# Ejemplo 1: Lista con *= (secuencia mutable)
cronopios = ["verde", "torpe", "feliz"]
print("Lista original:", cronopios)
print("ID original:", id(cronopios))
cronopios *= 2
print("Después de cronopios *= 2:", cronopios)
print("ID después de *=:", id(cronopios))
print("El ID es el mismo: la lista se modificó en el mismo lugar.")
print()

# Ejemplo 2: Con n = 0
famas = ["ordenado", "preciso", "puntual"]
print("Lista original:", famas)
famas *= 0
print("Después de famas *= 0:", famas)
print("Resultado: lista vacía.")
print()

# Ejemplo 3: Con n negativo
esperanzas = ["tranquila", "silenciosa"]
print("Lista original:", esperanzas)
esperanzas *= -3
print("Después de esperanzas *= -3:", esperanzas)
print("Resultado: lista vacía (cualquier n menor que 0 da lista vacía).")
print()

# Ejemplo 4: String con *= (secuencia inmutable)
frase = "cronopio"
print("String original:", frase)
print("ID original:", id(frase))
frase *= 3
print("Después de frase *= 3:", frase)
print("ID después de *=:", id(frase))
print("El ID cambió: se creó un nuevo string.")
print()

# Ejemplo 5: Aplicación práctica - un desfile de cronopios
desfile = ["cronopio"]
desfile *= 5
print("Desfile repetido:", desfile)
print("Cinco cronopios marchan en desorden pero felices.")
print()

# Ejemplo 6: Crear lista con valores iniciales
famas_numerados = [1]
famas_numerados *= 4
print("Lista de famas numerados:", famas_numerados)
print()

# Ejemplo 7: Advertencia con objetos mutables anidados
mal_entendido = [[]]
mal_entendido *= 3
print("Lista anidada repetida:", mal_entendido)
mal_entendido[0].append("cronopio confundido")
print("Después de modificar la primera sublista:", mal_entendido)
print("Cuidado: todas las sublistas son la misma referencia.")
print()

print("="*60)
print("RESUMEN:")
print("="*60)
print("- s *= n repite la secuencia s, n veces.")
print("- Para listas (mutables): modifica en el mismo lugar (mismo ID).")
print("- Para strings (inmutables): crea un nuevo objeto (nuevo ID).")
print("- Si n es menor o igual a 0, el resultado es una secuencia vacía.")
print("- Evitar usar *= con listas que contengan objetos mutables anidados.")
print()
print("Referencia:")
print("Cortázar, J. (2013). Historias de cronopios y de famas. Alfaguara.")
