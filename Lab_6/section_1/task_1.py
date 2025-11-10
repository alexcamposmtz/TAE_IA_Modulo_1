# task_1.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Team 6

"""
Task 1: Crear una clase Car con atributos brand, model y color.
Agregar un método show_info() que muestre la información completa del coche.
"""


class Car:
    """
    Clase que representa un coche.
    
    Atributos:
        brand (str): Marca del coche
        model (str): Modelo del coche
        color (str): Color del coche
    """
    
    def __init__(self, brand, model, color):
        """
        Constructor de la clase Car.
        
        Parámetros:
            brand (str): Marca del coche
            model (str): Modelo del coche
            color (str): Color del coche
        """
        self.brand = brand
        self.model = model
        self.color = color
    
    def show_info(self):
        """
        Muestramos la información completa del coche.
        
        Imprimimos en la terminal los detalles del coche: marca, modelo y color.
        """
        print(f"Coche: {self.brand} {self.model}")
        print(f"Color: {self.color}")


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 1: CLASE CAR - INFORMACIÓN DE LOS COCHES")
    print("=" * 70)
    
    print("--- Creando primer coche ---")
    car1 = Car("Toyota", "Corolla", "Rojo")
    car1.show_info()
    
    print("--- Creando segundo coche ---")
    car2 = Car("Honda", "Civic", "Azul")
    car2.show_info()