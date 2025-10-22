# task_2.py
# Sección 1. Práctica de programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# Definir números
num_int = 10
num_float = 3.5

print(f"Número entero: {num_int}, Tipo: {type(num_int)}")
print(f"Número flotante: {num_float}, Tipo: {type(num_float)}")
print("\n" + "="*50 + "\n")

# Suma
suma = num_int + num_float
print(f"Suma: {num_int} + {num_float} = {suma}")
print(f"Tipo del resultado: {type(suma)}\n")

# Resta
resta = num_int - num_float
print(f"Resta: {num_int} - {num_float} = {resta}")
print(f"Tipo del resultado: {type(resta)}\n")

# Multiplicación
multiplicacion = num_int * num_float
print(f"Multiplicación: {num_int} * {num_float} = {multiplicacion}")
print(f"Tipo del resultado: {type(multiplicacion)}\n")

# División
division = num_int / num_float
print(f"División: {num_int} / {num_float} = {division}")
print(f"Tipo del resultado: {type(division)}\n")

print("=================================================================")
print("OBSERVACIONES:")
print("- Cuando operamos int con float, el resultado es float")
print("- La división (/) SIEMPRE devuelve float, incluso con dos int")
