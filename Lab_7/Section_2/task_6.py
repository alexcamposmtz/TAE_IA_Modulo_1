# task_6.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de atributo (AttributeError)
encontrado durante la practica.
"""

print("=" * 70)
print("TASK 6: AttributeError - Error de Atributo")
print("=" * 70)

# CODIGO CON ERROR:
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Estudiante: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Grado: {self.grade}")  # Error: self.grade no existe

student = Student("Pedro", 20)
student.show_info()
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_6.py
======================================================================
TASK 6: AttributeError - Error de Atributo
======================================================================
Estudiante: Pedro
Edad: 20
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_6.py", line 28, in <module>
    student.show_info()
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_6.py", line 25, in show_info
    print(f"Grado: {self.grade}")  # Error: self.grade no existe
AttributeError: 'Student' object has no attribute 'grade'
"""

# Causa: Se intenta acceder a un atributo que no fue definido en __init__

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: AttributeError")
print("Causa: Se intenta acceder al atributo 'grade' que no existe")
print("Mensaje: AttributeError: 'Student' object has no attribute 'grade'")
print("Este error ocurre cuando intentamos acceder a un atributo")
print("que no ha sido definido en el constructor o en la clase.")
print()
print("Soluciones posibles:")
print("1. Agregar el atributo 'grade' en el constructor __init__()")
print("2. Verificar que el atributo existe antes de usarlo")
print("3. Inicializar el atributo con un valor por defecto")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Agregar atributo en constructor
print("\nSolucion 1: Agregar atributo en constructor")
print("-" * 70)

class Student:
    """Clase que representa un estudiante"""
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Atributo agregado
    
    def show_info(self):
        """Muestra la informacion del estudiante"""
        print(f"Estudiante: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Grado: {self.grade}")

print("Creando objeto Student con grado...")
student = Student("Pedro", 20, "Tercer Semestre")
student.show_info()

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Valor por defecto
print("\nSolucion 2: Usar valor por defecto")
print("-" * 70)

class Student2:
    """Clase que representa un estudiante con grado opcional"""
    
    def __init__(self, name, age, grade="No especificado"):
        self.name = name
        self.age = age
        self.grade = grade  # Valor por defecto
    
    def show_info(self):
        """Muestra la informacion del estudiante"""
        print(f"Estudiante: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Grado: {self.grade}")

print("Creando objeto Student2 sin especificar grado...")
student2 = Student2("Maria", 19)
student2.show_info()
