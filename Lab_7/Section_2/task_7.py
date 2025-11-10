# task_7.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de tipo (TypeError)
encontrado durante la practica.
"""

print("=" * 70)
print("TASK 7: TypeError - Error de Tipo")
print("=" * 70)

# CODIGO CON ERROR:
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price

product = Product("Laptop", 15000)
# Error: Se pasa un string en lugar de un numero
final_price = product.apply_discount("20")
print(f"Precio con descuento: ${final_price}")
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_7.py
======================================================================
TASK 7: TypeError - Error de Tipo
======================================================================
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_7.py", line 28, in <module>
    final_price = product.apply_discount("20")
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_7.py", line 23, in apply_discount
    discounted_price = self.price - (self.price * discount / 100)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
"""

# Causa: Se intenta dividir un string por un entero

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: TypeError")
print("Causa: Se intenta realizar operacion matematica con tipos incompatibles")
print("Mensaje: TypeError: unsupported operand type(s) for /: 'str' and 'int'")
print("Este error ocurre cuando intentamos usar operadores con tipos de")
print("datos incompatibles. En este caso, division de string entre entero.")
print()
print("Soluciones posibles:")
print("1. Pasar el argumento con el tipo de dato correcto (numero)")
print("2. Convertir el argumento al tipo correcto dentro del metodo")
print("3. Validar el tipo de dato antes de realizar la operacion")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Pasar tipo correcto
print("\nSolucion 1: Pasar argumento con tipo correcto")
print("-" * 70)

class Product:
    """Clase que representa un producto"""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self, discount):
        """Aplica un descuento al producto"""
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price

print("Creando producto...")
product = Product("Laptop", 15000)
print(f"Producto: {product.name}")
print(f"Precio original: ${product.price:,.2f}")

# Pasar numero en lugar de string
final_price = product.apply_discount(20)  # 20 en lugar de "20"
print(f"Precio con 20% descuento: ${final_price:,.2f}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Validacion de tipo
print("\nSolucion 2: Validacion y conversion de tipo")
print("-" * 70)

class Product2:
    """Clase que representa un producto con validacion"""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self, discount):
        """Aplica un descuento al producto con validacion"""
        try:
            # Intentar convertir a float
            discount = float(discount)
            discounted_price = self.price - (self.price * discount / 100)
            return discounted_price
        except ValueError:
            print(f"Error: '{discount}' no es un numero valido")
            return self.price

print("Creando producto con validacion...")
product2 = Product2("Tablet", 8000)
print(f"Producto: {product2.name}")
print(f"Precio original: ${product2.price:,.2f}")

# Ahora puede manejar strings numericos
final_price2 = product2.apply_discount("15")
print(f"Precio con 15% descuento: ${final_price2:,.2f}")

# Y tambien numeros directamente
final_price3 = product2.apply_discount(25)
print(f"Precio con 25% descuento: ${final_price3:,.2f}")
