"""
Lab 1: Error Handling
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro
"""

# Excepción integrada
try:
    result = 10 / 0
except ZeroDivisionError as err:
    print("Cannot divide by zero due to {err}")

def division(num1, num2):
    """Método para realizar la operación de división
    y manejar errores de división entre cero y de tipo"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"
    finally:
        print("Always running")

print("="*50)
print("="*50)

# Excepción Personalizada
class AgeTooSmallError(Exception):
    """Excepción lanzada cuando la edad ingresada está por debajo del umbral permitido."""
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}"
        super().__init__(message)

def check_age(age):
    """Verifica si la edad cumple con el requisito mínimo"""
    if age < 18:
        raise AgeTooSmallError(age)
    print("Access granted")

# Ejemplo de uso
try:
    check_age(16)
except AgeTooSmallError as err:
    print(f"Custom exception caught: {err}")

# Excepción Personalizada 1: Edad Demasiado Pequeña
class AgeTooSmallError(Exception):
    """Excepción lanzada cuando la edad ingresada está por debajo del umbral permitido."""
    
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}"
        super().__init__(message)


# Excepción Personalizada 2: Edad Demasiado Grande
class AgeTooLargeError(Exception):
    """Excepción lanzada cuando la edad ingresada está por encima del umbral máximo permitido."""
    
    def __init__(self, age, threshold=120):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is above the maximum allowed threshold of {threshold}"
        super().__init__(message)


def check_age(age):
    """
    Verifica si la edad cumple con los requisitos mínimo y máximo.
    
    Args:
        age (int): La edad a validar
        
    Raises:
        AgeTooSmallError: Si la edad es menor a 18
        AgeTooLargeError: Si la edad es mayor a 120
        
    Returns:
        None: Imprime "Access granted" si la edad es válida
    """
    if age < 18:
        raise AgeTooSmallError(age)
    if age > 120:
        raise AgeTooLargeError(age)
    print("Access granted")


def main():
    """
    Punto de entrada principal del programa.
    Maneja la entrada del usuario y la gestión de excepciones.
    """
    try:
        # Obtener entrada del usuario
        age_input = input("Please enter your age: ")
        
        # Intentar convertir la entrada a entero
        try:
            age = int(age_input)
        except ValueError:
            raise ValueError(f"Invalid input: '{age_input}' is not a valid integer. Please enter a numeric age.")
        
        # Verificar si la edad es válida
        check_age(age)
        print(f"Age {age} is valid and within acceptable range.")
        
    except AgeTooSmallError as err:
        print(f"ERROR: Custom exception caught: {err}")
        print(f"       You must be at least {err.threshold} years old to access this system.")
        
    except AgeTooLargeError as err:
        print(f"ERROR: Custom exception caught: {err}")
        print(f"       Maximum age allowed is {err.threshold} years.")
        
    except ValueError as err:
        print(f"ERROR: ValueError caught: {err}")
        print(f"       Please make sure to enter only numbers.")
        
    except Exception as err:
        print(f"ERROR: Unexpected error occurred: {type(err).__name__}")
        print(f"       Details: {err}")
        
    finally:
        print("\n" + "="*50)
        print("Code processing finished!")
        print("="*50)


if __name__ == "__main__":
    """
    Esto asegura que main() solo se ejecute cuando el script se ejecuta directamente,
    no cuando el archivo se importa como un módulo.
    """
    print("="*50)
    print("Lab 1: Age Validation System")
    print("="*50)
    print()
    main()