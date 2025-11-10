# task_8.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de indice (IndexError)
encontrado durante la practica.
"""

print("=" * 70)
print("TASK 8: IndexError - Error de Indice")
print("=" * 70)

# CODIGO CON ERROR:
"""
class Classroom:
    def __init__(self, students):
        self.students = students
    
    def get_student_at_position(self, position):
        return self.students[position]
    
    def show_all_students(self):
        print("Lista de estudiantes:")
        for i in range(len(self.students) + 1):  # Error: range va mas alla
            print(f"{i + 1}. {self.students[i]}")

classroom = Classroom(["Ana", "Luis", "Carlos"])
classroom.show_all_students()
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_8.py
======================================================================
TASK 8: IndexError - Error de Indice
======================================================================
Lista de estudiantes:
1. Ana
2. Luis
3. Carlos
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_8.py", line 30, in <module>
    classroom.show_all_students()
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_7/Section_2/task_8.py", line 27, in show_all_students
    print(f"{i + 1}. {self.students[i]}")
IndexError: list index out of range
"""

# Causa: Se intenta acceder a un indice que no existe en la lista

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: IndexError")
print("Causa: Se intenta acceder a un indice fuera del rango de la lista")
print("Mensaje: IndexError: list index out of range")
print("Este error ocurre cuando intentamos acceder a una posicion")
print("que no existe en una lista, tupla o secuencia.")
print()
print("En el codigo con error:")
print("- La lista tiene 3 elementos (indices 0, 1, 2)")
print("- range(len(self.students) + 1) genera: 0, 1, 2, 3")
print("- Al intentar acceder a self.students[3], ocurre el error")
print()
print("Soluciones posibles:")
print("1. Usar range(len(self.students)) sin el +1")
print("2. Iterar directamente sobre los elementos")
print("3. Validar el indice antes de acceder")

print("-" * 70)

# CODIGO CORREGIDO - Solucion 1: Corregir el range
print("\nSolucion 1: Corregir el range")
print("-" * 70)

class Classroom:
    """Clase que representa un salon de clases"""
    
    def __init__(self, students):
        self.students = students
    
    def get_student_at_position(self, position):
        """Obtiene un estudiante en una posicion especifica"""
        return self.students[position]
    
    def show_all_students(self):
        """Muestra todos los estudiantes"""
        print("Lista de estudiantes:")
        for i in range(len(self.students)):  # Corregido: sin +1
            print(f"{i + 1}. {self.students[i]}")

print("Creando salon de clases...")
classroom = Classroom(["Ana", "Luis", "Carlos"])
classroom.show_all_students()

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Iterar directamente
print("\nSolucion 2: Iterar directamente sobre elementos")
print("-" * 70)

class Classroom2:
    """Clase que representa un salon de clases con iteracion directa"""
    
    def __init__(self, students):
        self.students = students
    
    def show_all_students(self):
        """Muestra todos los estudiantes iterando directamente"""
        print("Lista de estudiantes:")
        for index, student in enumerate(self.students, start=1):
            print(f"{index}. {student}")

print("Creando salon de clases con iteracion directa...")
classroom2 = Classroom2(["Maria", "Pedro", "Sofia", "Diego"])
classroom2.show_all_students()

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 3: Validacion de indice
print("\nSolucion 3: Validacion de indice")
print("-" * 70)

class Classroom3:
    """Clase que representa un salon con validacion de indices"""
    
    def __init__(self, students):
        self.students = students
    
    def get_student_at_position(self, position):
        """Obtiene un estudiante con validacion de indice"""
        if 0 <= position < len(self.students):
            return self.students[position]
        else:
            return f"Error: Posicion {position} fuera de rango"
    
    def show_all_students(self):
        """Muestra todos los estudiantes"""
        print("Lista de estudiantes:")
        for i in range(len(self.students)):
            print(f"{i + 1}. {self.students[i]}")

print("Creando salon de clases con validacion...")
classroom3 = Classroom3(["Roberto", "Laura", "Fernando"])
classroom3.show_all_students()

print("\nProbando acceso con validacion:")
print(f"Posicion 1: {classroom3.get_student_at_position(1)}")
print(f"Posicion 5: {classroom3.get_student_at_position(5)}")
