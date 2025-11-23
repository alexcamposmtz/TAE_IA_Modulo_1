"""
Lab 3: Modules and Packages - Part 2
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Módulo mock_model: Contiene funciones para predicción de sentimiento simulada.
"""


def predict(text):
    """
    Realiza una predicción de sentimiento simple basada en palabras clave.
    """
    # Convertir a minúsculas para hacer la búsqueda case-insensitive
    text_lower = text.lower()
    
    # Verificar si la palabra "good" está en el texto
    if "good" in text_lower:
        return "positive"
    else:
        return "negative"


if __name__ == "__main__":
    # Pruebas del módulo
    print("Testing predict() function:")
    print("-" * 40)
    
    test_cases = [
        "This is a good day",
        "This is a bad day",
        "The weather is good today",
        "I don't like this",
        "Good morning everyone",
        "Have a great day"
    ]
    
    for test in test_cases:
        result = predict(test)
        print(f"Text: '{test}'")
        print(f"Sentiment: {result}")
        print()
