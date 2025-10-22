# task_1.py
# Sección 1. Práctica de programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

#Variable con valor "123"
var = "123"
print(f"Valor original: {var}, Tipo: {type(var)}")

# Conversión a integer
var_int = int(var)
print(f"Integer: {var_int}, Tipo: {type(var_int)}")

# Conversión a float
var_float = float(var)
print(f"Float: {var_float}, Tipo: {type(var_float)}")

# Conversión a boolean
var_bool = bool(var)
print(f"Boolean: {var_bool}, Tipo: {type(var_bool)}")

# Conversión a list
var_list = list(var)
print(f"List: {var_list}, Tipo: {type(var_list)}")

# Conversión a tuple
var_tuple = tuple(var)
print(f"Tuple: {var_tuple}, Tipo: {type(var_tuple)}")

print("\n" + "="*50 + "\n")

#Variable con valor "hello"
var = "hello"
print(f"Nuevo valor: {var}, Tipo: {type(var)}")

# Conversión a integer - ESTO GENERARÁ UN ERROR
try:
    var_int = int(var)
    print(f"Integer: {var_int}, Tipo: {type(var_int)}")
except ValueError as e:
    print(f"Error al convertir a int: {e}")

# Conversión a float - ESTO GENERARÁ UN ERROR
try:
    var_float = float(var)
    print(f"Float: {var_float}, Tipo: {type(var_float)}")
except ValueError as e:
    print(f"Error al convertir a float: {e}")

# Conversión a boolean
var_bool = bool(var)
print(f"Boolean: {var_bool}, Tipo: {type(var_bool)}")

# Conversión a list
var_list = list(var)
print(f"List: {var_list}, Tipo: {type(var_list)}")

# Conversión a tuple
var_tuple = tuple(var)
print(f"Tuple: {var_tuple}, Tipo: {type(var_tuple)}")

print("\n" + "="*50)
print("EXPLICACIÓN:")
print("- Con '123': todas las conversiones funcionan correctamente")
print("- Con 'hello': int() y float() fallan porque no es un número válido")
print("- bool() siempre devuelve True para strings no vacíos")
print("- list() y tuple() convierten cada carácter en un elemento")
