# task_4.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Team 6

"""
Se documenta un error de sintaxis (SyntaxError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 4: SyntaxError - Error de Sintaxis")
print("=" * 70)

# CODIGO CON ERROR:
"""
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def show_info(self)
        print(f"Automóvil: {self.brand} {self.model}")
        print(f"Color: {self.color}")
"""

# Error presentado:
"""
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_6/section_2/task_4.py", line 8
    def show_info(self)
                       ^
SyntaxError: expected ':'
"""

# Causa: Falta el símbolo de dos puntos (:) después de la definición del método


print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: SyntaxError")
print("Causa: Falta el símbolo ':' al final de la definición del método")
print("Mensaje: SyntaxError: expected ':'")
print("Este es un error común al definir métodos en clases POO")
print("En Python, todas las definiciones (def, class, if, for, etc.)")
print("deben terminar con dos puntos (:)")
print("Solución:")
print("Agregar ':' al final de la línea:")
print('def show_info(self):')

print("-" * 70)

# CODIGO CORREGIDO:
class Car:
    """Clase que representa un automóvil"""
    
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def show_info(self):  # ← Dos puntos agregados aquí
        """Muestra la información del automóvil"""
        print(f"Automóvil: {self.brand} {self.model}")
        print(f"Color: {self.color}")

print("Prueba con codigo corregido:")
print("Creando objeto Car...")
car = Car("Ford", "Mustang", "Negro")
car.show_info()
