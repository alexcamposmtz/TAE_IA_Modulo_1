# task_4.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 4: Composicion
- Crear una clase Engine con un metodo start() que imprima "Engine started".
- Crear una clase Car que tenga un atributo engine (tipo Engine) y un metodo 
  start_car() que llame a engine.start().
"""


class Engine:
    """
    Clase que representa un motor.
    
    Atributos:
        engine_type (str): Tipo de motor
        horsepower (int): Caballos de fuerza
    """
    
    def __init__(self, engine_type, horsepower):
        """
        Constructor de la clase Engine.
        
        Parametros:
            engine_type (str): Tipo de motor (ej: V6, V8, Electric)
            horsepower (int): Caballos de fuerza del motor
        """
        self.engine_type = engine_type
        self.horsepower = horsepower
    
    def start(self):
        """
        Enciende el motor.
        
        Imprime un mensaje indicando que el motor ha arrancado.
        """
        print("Engine started")
    
    def show_specs(self):
        """
        Muestra las especificaciones del motor.
        """
        print(f"Motor: {self.engine_type}")
        print(f"Potencia: {self.horsepower} HP")


class Car:
    """
    Clase que representa un automovil.
    
    Utiliza composicion: tiene un objeto Engine como parte de su estructura.
    
    Atributos:
        brand (str): Marca del automovil
        model (str): Modelo del automovil
        engine (Engine): Motor del automovil (composicion)
    """
    
    def __init__(self, brand, model, engine):
        """
        Constructor de la clase Car.
        
        Parametros:
            brand (str): Marca del automovil
            model (str): Modelo del automovil
            engine (Engine): Objeto Engine que compone al automovil
        """
        self.brand = brand
        self.model = model
        self.engine = engine
    
    def start_car(self):
        """
        Arranca el automovil.
        
        Este metodo utiliza el motor (engine) del automovil
        para realizar el arranque, demostrando composicion.
        """
        print(f"Arrancando {self.brand} {self.model}...")
        self.engine.start()
    
    def show_info(self):
        """
        Muestra la informacion completa del automovil.
        """
        print(f"Automovil: {self.brand} {self.model}")
        self.engine.show_specs()


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 4: COMPOSICION - ENGINE Y CAR")
    print("=" * 70)
    
    print("\nLa composicion es cuando una clase contiene objetos de otra clase.")
    print("En este caso, Car TIENE UN Engine (has-a relationship).")
    print()
    
    print("--- Creando motor 1 ---")
    engine1 = Engine("V8", 450)
    engine1.show_specs()
    
    print("\n--- Creando automovil 1 con motor V8 ---")
    car1 = Car("Ford", "Mustang", engine1)
    car1.show_info()
    
    print("\n--- Arrancando automovil 1 ---")
    car1.start_car()
    
    print("\n" + "-" * 70)
    
    print("\n--- Creando motor 2 ---")
    engine2 = Engine("Electric", 300)
    engine2.show_specs()
    
    print("\n--- Creando automovil 2 con motor electrico ---")
    car2 = Car("Tesla", "Model 3", engine2)
    car2.show_info()
    
    print("\n--- Arrancando automovil 2 ---")
    car2.start_car()
    
    print("\n" + "-" * 70)
    print("\nNota: El automovil usa el motor para arrancar,")
    print("demostrando la relacion de composicion entre Car y Engine.")
