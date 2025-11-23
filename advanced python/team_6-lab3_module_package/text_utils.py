"""
Lab 3: Modules and Packages - Part 1
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Este módulo proporciona utilidades básicas para procesamiento de texto.
"""


def clean_text(text):
    """
    Limpia y normaliza el texto convirtiéndolo a minúsculas.
    
    Args:
        text (str): El texto a procesar
        
    Returns:
        str: El texto convertido a minúsculas
     """
    return text.lower()


if __name__ == "__main__":
    # Pruebas del módulo
    print("Testing clean_text() function:")
    print("-" * 40)
    
    test_cases = [
        "HELLO WORLD",
        "Python Programming",
        "This Is A Test",
        "GOOD morning"
    ]
    
    for test in test_cases:
        result = clean_text(test)
        print(f"Input:  '{test}'")
        print(f"Output: '{result}'")
        print()
