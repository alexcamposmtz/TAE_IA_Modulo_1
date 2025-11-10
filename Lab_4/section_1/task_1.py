# task_1.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

import math

def area_circulo(radio=None):
    """
    Calcula el area de un circulo.
    
    Parametros:
        radio (float): Radio del circulo. Valor por defecto: 1.0
    
    Retorna:
        float: Area del circulo
    """
    if radio is None:
        radio = 1.0
        print("AVISO: Usando valor por defecto para el radio: 1.0")
    
    area = math.pi * radio ** 2
    return area


def area_cuadrado(lado=None):
    """
    Calcula el area de un cuadrado.
    
    Parametros:
        lado (float): Longitud del lado del cuadrado. Valor por defecto: 1.0
    
    Retorna:
        float: Area del cuadrado
    """
    if lado is None:
        lado = 1.0
        print("AVISO: Usando valor por defecto para el lado: 1.0")
    
    area = lado ** 2
    return area


def area_triangulo(base=None, altura=None):
    """
    Calcula el area de un triangulo.
    
    Parametros:
        base (float): Base del triangulo. Valor por defecto: 1.0
        altura (float): Altura del triangulo. Valor por defecto: 1.0
    
    Retorna:
        float: Area del triangulo
    """
    usar_defecto_base = False
    usar_defecto_altura = False
    
    if base is None:
        base = 1.0
        usar_defecto_base = True
    
    if altura is None:
        altura = 1.0
        usar_defecto_altura = True
    
    if usar_defecto_base and usar_defecto_altura:
        print("AVISO: Usando valores por defecto para base y altura: 1.0, 1.0")
    elif usar_defecto_base:
        print("AVISO: Usando valor por defecto para la base: 1.0")
    elif usar_defecto_altura:
        print("AVISO: Usando valor por defecto para la altura: 1.0")
    
    area = (base * altura) / 2
    return area


def area_hexagono(lado=None):
    """
    Calcula el area de un hexagono regular.
    
    Parametros:
        lado (float): Longitud del lado del hexagono. Valor por defecto: 1.0
    
    Retorna:
        float: Area del hexagono
    """
    if lado is None:
        lado = 1.0
        print("AVISO: Usando valor por defecto para el lado: 1.0")
    
    area = (3 * math.sqrt(3) / 2) * lado ** 2
    return area


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 1: FUNCIONES DE AREAS CON PARAMETROS POR DEFECTO")
    print("=" * 70)
    
    print("\n--- Prueba 1: Circulo con valor por defecto ---")
    resultado = area_circulo()
    print(f"Area del circulo: {resultado:.2f}\n")
    
    print("--- Prueba 2: Circulo con radio especificado ---")
    resultado = area_circulo(5)
    print(f"Area del circulo con radio 5: {resultado:.2f}\n")
    
    print("--- Prueba 3: Cuadrado con valor por defecto ---")
    resultado = area_cuadrado()
    print(f"Area del cuadrado: {resultado:.2f}\n")
    
    print("--- Prueba 4: Cuadrado con lado especificado ---")
    resultado = area_cuadrado(4)
    print(f"Area del cuadrado con lado 4: {resultado:.2f}\n")
    
    print("--- Prueba 5: Triangulo con valores por defecto ---")
    resultado = area_triangulo()
    print(f"Area del triangulo: {resultado:.2f}\n")
    
    print("--- Prueba 6: Triangulo con base y altura especificadas ---")
    resultado = area_triangulo(6, 8)
    print(f"Area del triangulo con base 6 y altura 8: {resultado:.2f}\n")
    
    print("--- Prueba 7: Hexagono con valor por defecto ---")
    resultado = area_hexagono()
    print(f"Area del hexagono: {resultado:.2f}\n")
    
    print("--- Prueba 8: Hexagono con lado especificado ---")
    resultado = area_hexagono(3)
    print(f"Area del hexagono con lado 3: {resultado:.2f}\n")
