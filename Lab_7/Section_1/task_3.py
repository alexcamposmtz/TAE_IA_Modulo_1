# task_3.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 3: Polimorfismo
- Crear una funcion calculate_payment(worker) que llame al metodo payment() 
  del objeto pasado.
- Crear varias clases (FullTimeEmployee, HourlyEmployee) cada una con su 
  propio metodo payment().
- Probar la funcion con diferentes objetos y ver como el mismo metodo 
  produce resultados diferentes.
"""


def calculate_payment(worker):
    """
    Calcula el pago de un trabajador.
    
    Esta funcion demuestra polimorfismo al llamar al metodo payment()
    de diferentes tipos de objetos, cada uno con su propia implementacion.
    
    Parametros:
        worker: Objeto trabajador con metodo payment()
    """
    print(f"Calculando pago para: {worker.name}")
    worker.payment()
    print()


class FullTimeEmployee:
    """
    Clase que representa un empleado de tiempo completo.
    
    Atributos:
        name (str): Nombre del empleado
        monthly_salary (float): Salario mensual fijo
    """
    
    def __init__(self, name, monthly_salary):
        """
        Constructor de la clase FullTimeEmployee.
        
        Parametros:
            name (str): Nombre del empleado
            monthly_salary (float): Salario mensual fijo
        """
        self.name = name
        self.monthly_salary = monthly_salary
    
    def payment(self):
        """
        Calcula el pago del empleado de tiempo completo.
        
        Los empleados de tiempo completo reciben un salario mensual fijo.
        """
        print(f"Tipo: Empleado Tiempo Completo")
        print(f"Pago mensual: ${self.monthly_salary:,.2f}")


class HourlyEmployee:
    """
    Clase que representa un empleado por horas.
    
    Atributos:
        name (str): Nombre del empleado
        hourly_rate (float): Tarifa por hora
        hours_worked (int): Horas trabajadas
    """
    
    def __init__(self, name, hourly_rate, hours_worked):
        """
        Constructor de la clase HourlyEmployee.
        
        Parametros:
            name (str): Nombre del empleado
            hourly_rate (float): Tarifa por hora
            hours_worked (int): Horas trabajadas en el periodo
        """
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def payment(self):
        """
        Calcula el pago del empleado por horas.
        
        Los empleados por horas reciben pago basado en horas trabajadas.
        """
        total_payment = self.hourly_rate * self.hours_worked
        print(f"Tipo: Empleado por Horas")
        print(f"Tarifa: ${self.hourly_rate:.2f}/hora")
        print(f"Horas trabajadas: {self.hours_worked}")
        print(f"Pago total: ${total_payment:,.2f}")


class FreelanceEmployee:
    """
    Clase que representa un empleado freelance.
    
    Atributos:
        name (str): Nombre del empleado
        project_rate (float): Tarifa por proyecto
        projects_completed (int): Proyectos completados
    """
    
    def __init__(self, name, project_rate, projects_completed):
        """
        Constructor de la clase FreelanceEmployee.
        
        Parametros:
            name (str): Nombre del empleado
            project_rate (float): Tarifa por proyecto
            projects_completed (int): Numero de proyectos completados
        """
        self.name = name
        self.project_rate = project_rate
        self.projects_completed = projects_completed
    
    def payment(self):
        """
        Calcula el pago del empleado freelance.
        
        Los freelancers reciben pago por proyecto completado.
        """
        total_payment = self.project_rate * self.projects_completed
        print(f"Tipo: Freelance")
        print(f"Tarifa por proyecto: ${self.project_rate:,.2f}")
        print(f"Proyectos completados: {self.projects_completed}")
        print(f"Pago total: ${total_payment:,.2f}")


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 3: POLIMORFISMO - CALCULO DE PAGOS")
    print("=" * 70)
    
    print("\nDemostracion de polimorfismo:")
    print("La misma funcion calculate_payment() funciona con diferentes")
    print("tipos de empleados, cada uno con su propia implementacion de payment()")
    print()
    
    # Crear diferentes tipos de empleados
    emp1 = FullTimeEmployee("Ana Garcia", 35000.00)
    emp2 = HourlyEmployee("Luis Martinez", 150.00, 160)
    emp3 = FreelanceEmployee("Sofia Hernandez", 8000.00, 3)
    
    # Usar la misma funcion con diferentes objetos
    print("--- Empleado 1 ---")
    calculate_payment(emp1)
    
    print("--- Empleado 2 ---")
    calculate_payment(emp2)
    
    print("--- Empleado 3 ---")
    calculate_payment(emp3)
    
    print("Nota: Todos los objetos responden al metodo payment() de manera")
    print("diferente, demostrando el polimorfismo en accion.")
