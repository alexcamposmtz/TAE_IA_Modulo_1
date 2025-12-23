"""
Lab 5: Lambda Expressions y Closures
Advanced Python - CINVESTAV Guadalajara

Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Este laboratorio demuestra el uso de closures que retornan
expresiones lambda para realizar operaciones de suma.
"""


def adder(x):
    """
    Closure que captura un valor y retorna una lambda expression
    para sumar ese valor con otro valor dado.
    
    Args:
        x: Primer valor a sumar (será capturado por el closure)
        
    Returns:
        Lambda function que toma un segundo valor y retorna la suma
    """
    # La lambda captura la variable 'x' del scope externo (closure)
    # y la suma con el parámetro 'y' que recibe
    return lambda y: x + y


def test_user_input():
    """
    Primera prueba: Solicita dos valores enteros al usuario
    y utiliza el closure adder para sumarlos.
    """
    print("=" * 50)
    print("PRUEBA 1: Suma con Entrada del Usuario")
    print("=" * 50)
    
    try:
        # Solicitar el primer valor al usuario
        input_str = input("Ingrese el primer valor entero: ")
        valor1 = int(input_str.strip())
        
        # Solicitar el segundo valor al usuario
        input_str = input("Ingrese el segundo valor entero: ")
        valor2 = int(input_str.strip())
        
        # Crear el closure con el primer valor
        suma_funcion = adder(valor1)
        
        # Aplicar la lambda con el segundo valor
        resultado = suma_funcion(valor2)
        
        print(f"\nResultado: {valor1} + {valor2} = {resultado}")
        print("Prueba 1 completada exitosamente!")
        
    except (ValueError, EOFError):
        print("Error: Por favor ingrese valores enteros validos.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def test_list_sum():
    """
    Segunda prueba: Suma un valor entero con cada elemento
    de una lista usando el closure adder.
    """
    print("\n" + "=" * 50)
    print("PRUEBA 2: Entero + Elementos de Lista")
    print("=" * 50)
    
    try:
        # Solicitar el valor entero base
        input_str = input("Ingrese un valor entero para sumar a la lista: ")
        valor_base = int(input_str.strip())
        
        # Crear una lista con 5 elementos
        lista_numeros = [10, 20, 30, 40, 50]
        print(f"\nLista de numeros: {lista_numeros}")
        
        # Crear el closure con el valor base
        suma_funcion = adder(valor_base)
        
        # Aplicar la lambda a cada elemento de la lista usando map
        resultados = list(map(suma_funcion, lista_numeros))
        
        print(f"\nValor base: {valor_base}")
        print(f"Resultados despues de sumar {valor_base} a cada elemento:")
        
        # Mostrar los resultados detalladamente
        for i, (original, resultado) in enumerate(zip(lista_numeros, resultados)):
            print(f"  Posicion {i}: {valor_base} + {original} = {resultado}")
        
        print(f"\nLista de resultados final: {resultados}")
        print("Prueba 2 completada exitosamente!")
        
    except (ValueError, EOFError):
        print("Error: Por favor ingrese un valor entero valido.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def main():
    """
    Función principal que ejecuta ambas pruebas del laboratorio.
    """
    print("\n")
    print("*" * 50)
    print("LABORATORIO DE LAMBDA Y CLOSURES")
    print("Equipo 6 - Advanced Python")
    print("*" * 50)
    print("\n")
    
    # Ejecutar la primera prueba
    test_user_input()
    
    print("\n" + "-" * 50 + "\n")
    
    # Ejecutar la segunda prueba
    test_list_sum()
    
    print("\n" + "*" * 50)
    print("Laboratorio completado!")
    print("*" * 50 + "\n")


if __name__ == "__main__":
    main()