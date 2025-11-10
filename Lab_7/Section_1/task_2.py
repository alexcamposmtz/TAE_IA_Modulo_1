# task_2.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 2: Herencia Multiple
- Crear una clase Accountant con un metodo generate_report() que imprima 
  "Generating financial report".
- Crear una clase Technician con un metodo repair_machine() que imprima 
  "Repairing machine".
- Crear una clase Boss que herede de ambas clases y probar ambos metodos.
"""


class Accountant:
    """
    Clase que representa un contador.
    """
    
    def generate_report(self):
        """
        Genera un reporte financiero.
        
        Imprime un mensaje indicando que se esta generando un reporte.
        """
        print("Generating financial report")


class Technician:
    """
    Clase que representa un tecnico.
    """
    
    def repair_machine(self):
        """
        Repara una maquina.
        
        Imprime un mensaje indicando que se esta reparando una maquina.
        """
        print("Repairing machine")


class Boss(Accountant, Technician):
    """
    Clase que representa un jefe, hereda de Accountant y Technician.
    
    Utiliza herencia multiple para combinar capacidades de ambas clases.
    """
    
    def __init__(self, name):
        """
        Constructor de la clase Boss.
        
        Parametros:
            name (str): Nombre del jefe
        """
        self.name = name
    
    def show_info(self):
        """
        Muestra la informacion del jefe.
        """
        print(f"Jefe: {self.name}")
        print("Capacidades: Contabilidad y Tecnicas")


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 2: HERENCIA MULTIPLE - ACCOUNTANT, TECHNICIAN, BOSS")
    print("=" * 70)
    
    print("\n--- Creando contador ---")
    accountant = Accountant()
    accountant.generate_report()
    
    print("\n--- Creando tecnico ---")
    technician = Technician()
    technician.repair_machine()
    
    print("\n--- Creando jefe con herencia multiple ---")
    boss = Boss("Roberto Sanchez")
    boss.show_info()
    
    print("\n--- Probando metodo heredado de Accountant ---")
    boss.generate_report()
    
    print("\n--- Probando metodo heredado de Technician ---")
    boss.repair_machine()
