# task_1.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 1: Crear una clase Employee con atributos name y salary, y un metodo 
show_info() que imprima el nombre y salario.
Luego, crear una clase Manager que herede de Employee y agregue un atributo 
department. Sobrescribir show_info() para mostrar tambien el departamento.
"""


class Employee:
    """
    Clase que representa un empleado.
    
    Atributos:
        name (str): Nombre del empleado
        salary (float): Salario del empleado
    """
    
    def __init__(self, name, salary):
        """
        Constructor de la clase Employee.
        
        Parametros:
            name (str): Nombre del empleado
            salary (float): Salario del empleado
        """
        self.name = name
        self.salary = salary
    
    def show_info(self):
        """
        Muestra la informacion del empleado.
        
        Imprime el nombre y salario del empleado.
        """
        print(f"Nombre: {self.name}")
        print(f"Salario: ${self.salary:,.2f}")


class Manager(Employee):
    """
    Clase que representa un gerente, hereda de Employee.
    
    Atributos:
        name (str): Nombre del gerente (heredado)
        salary (float): Salario del gerente (heredado)
        department (str): Departamento del gerente
    """
    
    def __init__(self, name, salary, department):
        """
        Constructor de la clase Manager.
        
        Parametros:
            name (str): Nombre del gerente
            salary (float): Salario del gerente
            department (str): Departamento del gerente
        """
        super().__init__(name, salary)
        self.department = department
    
    def show_info(self):
        """
        Muestra la informacion del gerente.
        
        Sobrescribe el metodo de Employee para incluir el departamento.
        """
        print(f"Nombre: {self.name}")
        print(f"Salario: ${self.salary:,.2f}")
        print(f"Departamento: {self.department}")


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 1: HERENCIA - EMPLOYEE Y MANAGER")
    print("=" * 70)
    
    print("\n--- Creando empleado ---")
    employee1 = Employee("Juan Perez", 25000.00)
    employee1.show_info()
    
    print("\n--- Creando gerente ---")
    manager1 = Manager("Maria Rodriguez", 45000.00, "Ventas")
    manager1.show_info()
    
    print("\n--- Creando otro gerente ---")
    manager2 = Manager("Carlos Lopez", 50000.00, "Tecnologia")
    manager2.show_info()
