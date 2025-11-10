"""
Paquete geometria_package
Contiene modulos para calcular areas y realizar operaciones con matrices.
"""

from .areas import area_circulo, area_cuadrado, area_triangulo, area_hexagono
from .matrices import multiplicacion_matrices, suma_matrices, resta_matrices, imprimir_matriz

__all__ = [
    'area_circulo',
    'area_cuadrado', 
    'area_triangulo',
    'area_hexagono',
    'multiplicacion_matrices',
    'suma_matrices',
    'resta_matrices',
    'imprimir_matriz'
]
