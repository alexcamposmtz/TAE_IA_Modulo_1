# task_5.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Team 6

"""
Se documenta un error de tipo (TypeError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 5: TypeError - Error de Tipo")
print("=" * 70)

# CODIGO CON ERROR:
"""
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def greet(self):
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años")

# Intentar crear objeto sin pasar todos los argumentos requeridos
person = Person("Ana", 25)  # Falta el argumento 'city'
person.greet()
"""

# Error presentado:
"""
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_6/section_2/task_5.py", line 15
    person = Person("Ana", 25)
             ^^^^^^^^^^^^^^^^^
TypeError: Person.__init__() missing 1 required positional argument: 'city'
"""

# Causa: Falta pasar el argumento 'city' requerido por el constructor


print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: TypeError")
print("Causa: Faltan argumentos al instanciar el objeto Person")
print("Mensaje: TypeError: Person.__init__() missing 1 required positional argument: 'city'")
print("Este error ocurre cuando no pasamos todos los parámetros")
print("requeridos por el constructor __init__()")
print("Soluciones:")
print("1. Pasar todos los argumentos requeridos")
print("2. Usar valores por defecto en el constructor")
print("3. Usar *args o **kwargs para argumentos variables")

print("-" * 70)

# CODIGO CORREGIDO - Opción 1: Pasar todos los argumentos
print("Solución - Pasar todos los argumentos requeridos:")

class Person:
    """Clase que representa una persona"""
    
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def greet(self):
        """Muestra un saludo personalizado"""
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años y vivo en {self.city}")

person1 = Person("Ana", 25, "México")  # ← Ahora con todos los argumentos
person1.greet()
