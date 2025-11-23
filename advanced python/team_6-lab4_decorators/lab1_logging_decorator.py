"""
Lab 4: Decorators - Lab 1: Logging Decorator
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Este módulo implementa un decorador de logging que registra
el nombre de la función y los argumentos con los que fue llamada.
"""


def logger(func):
    """
    Decorador que registra información sobre las llamadas a funciones.
    
    Este decorador imprime el nombre de la función y todos sus argumentos
    (tanto posicionales como keyword) cada vez que la función es llamada.    
    Args:
        func: La función a decorar        
    Returns:
        wrapper: La función envuelta con capacidad de logging
    """
    def wrapper(*args, **kwargs):
        """
        Función wrapper que añade logging a la función original.
        
        Args:
            *args: Argumentos posicionales pasados a la función
            **kwargs: Argumentos keyword pasados a la función            
        Returns:
            El resultado de la función original
        """
        # Cadena de argumentos posicionales
        args_str = ', '.join([repr(arg) for arg in args])
        
        # Cadena de argumentos keyword
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        
        # Combinamos tipos de argumentos
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        # Imprimimos información de logging
        print(f"[LOG] Calling function '{func.__name__}' with arguments: {all_args}")
        
        # Llamamos a la función original y retornar su resultado
        result = func(*args, **kwargs)
        
        # Log del resultado
        print(f"[LOG] Function '{func.__name__}' returned: {repr(result)}")
        
        return result
    
    return wrapper


# Aplicar el decorador a una función matemática simple
@logger
def add(a, b):
    """
    Suma dos números.    
    Args:
        a: Primer número
        b: Segundo número        
    Returns:
        La suma de a y b
    """
    return a + b


@logger
def multiply(x, y, z=1):
    """
    Multiplica dos o tres números.    
    Args:
        x: Primer número
        y: Segundo número
        z: Tercer número (opcional, por defecto 1)        
    Returns:
        El producto de los números
    """
    return x * y * z


@logger
def greet(name, greeting="Hello"):
    """
    Genera un saludo personalizado.    
    Args:
        name: Nombre de la persona
        greeting: Saludo a usar (por defecto "Hello")        
    Returns:
        Cadena con el saludo
    """
    return f"{greeting}, {name}!"


def main():
    """
    Función principal que demuestra el uso del decorador logger.
    """
    print("=" * 70)
    print("Lab 4: Decorators - Lab 1: Logging Decorator")
    print("=" * 70)
    print()
    
    # Prueba 1: Función add con argumentos posicionales
    print("Test 1: Función add(5, 3)")
    print("-" * 70)
    result1 = add(5, 3)
    print(f"Resultado: {result1}")
    print()
    
    # Prueba 2: Función multiply con argumentos posicionales
    print("Test 2: Función multiply(4, 5)")
    print("-" * 70)
    result2 = multiply(4, 5)
    print(f"Resultado: {result2}")
    print()
    
    # Prueba 3: Función multiply con argumentos keyword
    print("Test 3: Función multiply(2, 3, z=4)")
    print("-" * 70)
    result3 = multiply(2, 3, z=4)
    print(f"Resultado: {result3}")
    print()
    
    # Prueba 4: Función greet con argumentos mixtos
    print("Test 4: Función greet('Alice')")
    print("-" * 70)
    result4 = greet("Agustín")
    print(f"Resultado: {result4}")
    print()
    
    # Prueba 5: Función greet con keyword argument
    print("Test 5: Función greet('Alex', greeting='Hi')")
    print("-" * 70)
    result5 = greet("Alex", greeting="Hi")
    print(f"Resultado: {result5}")
    print()
    
    print("=" * 70)
    print("Lab 1 Complete!")
    print("=" * 70)


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Solo se ejecuta cuando el script se ejecuta directamente.
    """
    main()