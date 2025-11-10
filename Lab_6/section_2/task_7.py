# task_7.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Team 6

"""
Se documenta un error de nombre (NameError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 7: NameError - Error de Nombre")
print("=" * 70)

# CODIGO CON ERROR:
"""
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def show_info(self):
        print(f"Automóvil: {self.brand} {self.model}")
        print(f"Color: {self.color}")
        print(f"Año: {self.year}")  # Error: 'year' no fue definido

car = Car("Toyota", "Corolla", "Rojo")
car.show_info()
"""

# Error presentado:
"""
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_6/section_2/task_7.py", line 15
    car.show_info()
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_6/section_2/task_7.py", line 11, in show_info
    print(f"Año: {self.year}")
                      ^^^^^^^^^
AttributeError: 'Car' object has no attribute 'year'
"""

# Nota: Aunque el error es AttributeError, la causa raíz es un NameError
# (use una variable/atributo que no existe)

# Causa: Intentar usar un atributo 'year' que no fue definido en __init__


print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: AttributeError (causado por NameError conceptual)")
print("Causa: Intentar usar 'self.year' que no fue inicializado")
print("Mensaje: AttributeError: 'Car' object has no attribute 'year'")
print("Este error ocurre cuando:")
print("- Usamos un atributo en un método sin haberlo definido")
print("- Olvidamos inicializar atributos en __init__()")
print("- Escribimos mal el nombre de un atributo existente")
print("Soluciones:")
print("1. Agregar el atributo al constructor")
print("2. Usar valores por defecto si el atributo es opcional")
print("3. Verificar existencia antes de usar con hasattr()")

print("-" * 70)

# CODIGO CORREGIDO - Opción 1: Agregar el atributo faltante
print("\nSolución 1 - Agregar 'year' al constructor:")

class Car:
    """Clase que representa un automóvil"""
    
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year  # ← Atributo agregado
    
    def show_info(self):
        print(f"Automóvil: {self.brand} {self.model}")
        print(f"Color: {self.color}")
        print(f"Año: {self.year}")  # ← Ahora funciona

car1 = Car("Toyota", "Corolla", "Rojo", 2023)
car1.show_info()