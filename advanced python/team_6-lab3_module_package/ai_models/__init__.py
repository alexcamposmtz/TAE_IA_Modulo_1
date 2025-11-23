"""
Lab 3: Modules and Packages - Part 2
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Paquete ai_models: Contiene módulos para inferencia de modelos simulados.
"""

# Importar la función predict del módulo mock_model
from .mock_model import predict

# Definir qué se exporta cuando se hace "from ai_models import *"
__all__ = ['predict']

# Información del paquete
__version__ = '1.0.0'
__author__ = 'Team 6'
