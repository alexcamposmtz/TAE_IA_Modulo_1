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
