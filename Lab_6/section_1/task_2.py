# task_2.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Team 6

"""
Task 2: Crear una clase Person con constructor que recibe name, age y city.
Agregar un método greet() que muestre un mensaje de saludo personalizado.
"""


class Person:
    """
    Clase que representa una persona.
    
    Atributos:
        name (str): Nombre de la persona
        age (int): Edad de la persona
        city (str): Ciudad donde vive la persona
    """
    
    def __init__(self, name, age, city):
        """
        Constructor de la clase Person.
        
        Parámetros:
            name (str): Nombre de la persona
            age (int): Edad de la persona
            city (str): Ciudad donde vive la persona
        """
        self.name = name
        self.age = age
        self.city = city
    
    def greet(self):
        """
        Muestra un mensaje de saludo personalizado.
        
        Imprime un saludo que incluye el nombre, edad y ciudad de la persona.
        """
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años y vivo en {self.city}.")


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 2: CLASE PERSON - SALUDOS PERSONALIZADOS")
    print("=" * 70)
    
    print("\n--- Creando primera persona ---")
    person1 = Person("Ana", 25, "México")
    person1.greet()
    
    print("\n--- Creando segunda persona ---")
    person2 = Person("Carlos", 30, "Guadalajara")
    person2.greet()
    
    print("\n--- Creando tercera persona ---")
    person3 = Person("María", 28, "Monterrey")
    person3.greet()