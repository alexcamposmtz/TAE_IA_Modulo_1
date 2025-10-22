# task_2.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# Filtrado de Diccionarios
"""
Se crea un diccionario con nombres de animales y
genera tres diccionarios filtrados que contienen palabras con
las letras 'a', 'b' y 'y' respectivamente.
"""

print("=" * 70)
print("FILTRADO DE DICCIONARIOS")
print("=" * 70)

# Lista de animales
animals = [
    "Ferret", "boar", "jaguar", "giraffe", "lizard", "locust", "lion", 
    "wolf", "parrot", "raccoon", "butterfly", "jellyfish", "fly", "gnat", 
    "bat", "otter", "bear", "polar bear", "oyster", "sheep", "bee", "eagle", 
    "antelope", "spider", "squirrel", "tuna", "ostrich", "wasp", "whale", 
    "bison", "buffalo", "owl", "donkey", "horse", "goat", "squid", 
    "chameleon", "camel", "crab", "kangaroo", "cat", "dog"
]

# Creamos diccionario principal con todos los animales (clave = índice, valor = nombre del animal)
main_dictionary = {}
for i in range(len(animals)):
    main_dictionary[i] = animals[i]

print("\nDiccionario Principal:")
print(main_dictionary)
print(f"\nTotal de animales: {len(main_dictionary)}")

# Diccionario con palabras que contienen la letra "a"
print("\n" + "=" * 60)
print("a) Palabras que contienen la letra 'a':")
print("=" * 60)

dict_a = {}
for key, value in main_dictionary.items():
    if 'a' in value.lower():  # Convertir a minúsculas para guardar 'a' y 'A'
        dict_a[key] = value

print(dict_a)
print(f"Total de animales con 'a': {len(dict_a)}")

# Diccionario con palabras que contienen la letra "b"
print("\n" + "=" * 60)
print("b) Palabras que contienen la letra 'b':")
print("=" * 60)

dict_b = {}
for key, value in main_dictionary.items():
    if 'b' in value.lower():
        dict_b[key] = value

print(dict_b)
print(f"Total de animales con 'b': {len(dict_b)}")

# Diccionario con palabras que contienen la letra "y"
print("\n" + "=" * 60)
print("c) Palabras que contienen la letra 'y':")
print("=" * 60)

dict_y = {}
for key, value in main_dictionary.items():
    if 'y' in value.lower():
        dict_y[key] = value

print(dict_y)
print(f"Total de animales con 'y': {len(dict_y)}")
