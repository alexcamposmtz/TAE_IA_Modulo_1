"""
Lab 3: Modules and Packages - Main Program
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Este programa principal demuestra el uso de módulos y paquetes personalizados.
"""

# Importar el módulo de utilidades de texto
import text_utils

# Importar el paquete ai_models (dos formas diferentes)
# Forma 1: Importar el paquete completo
import ai_models

# Forma 2: Importar función específica directamente
from ai_models import predict

# También se puede importar el módulo específico
from ai_models import mock_model


def main():
    """
    Función principal que demuestra el uso de módulos y paquetes.
    """
    print("=" * 60)
    print("Lab 3: Modules and Packages Demonstration")
    print("=" * 60)
    print()
    
    # Lista de textos de prueba
    test_texts = [
        "This is a GOOD day for learning Python!",
        "MODULES and PACKAGES are IMPORTANT concepts",
        "I love programming with Python",
        "This is a bad example",
        "Good morning, everyone!"
    ]
    
    print("Testing Module and Package Integration:")
    print("-" * 60)
    print()
    
    for i, text in enumerate(test_texts, 1):
        print(f"Test Case {i}:")
        print(f"Original text: '{text}'")
        
        # Usar el módulo text_utils para limpiar el texto
        cleaned = text_utils.clean_text(text)
        print(f"Cleaned text:  '{cleaned}'")
        
        # Usar el paquete ai_models para predecir el sentimiento
        # Forma 1: Usando la importación directa de predict
        sentiment = predict(cleaned)
        print(f"Sentiment:     {sentiment}")
        
        # Forma 2 alternativa: Usando ai_models.predict
        # sentiment_alt = ai_models.predict(cleaned)
        
        # Forma 3 alternativa: Usando ai_models.mock_model.predict
        # sentiment_alt = mock_model.predict(cleaned)
        
        print()
    
    print("=" * 60)
    print("Lab 3 Complete!")
    print("=" * 60)


def demo_different_imports():
    """
    Demuestra las diferentes formas de importar y usar módulos y paquetes.
    """
    print("\nDifferent Import Methods Demo:")
    print("-" * 60)
    
    test_text = "This is a GOOD example"
    
    # Método 1: import module
    cleaned1 = text_utils.clean_text(test_text)
    print(f"Method 1 (import text_utils): {cleaned1}")
    
    # Método 2: from package import function
    sentiment1 = predict(cleaned1)
    print(f"Method 2 (from ai_models import predict): {sentiment1}")
    
    # Método 3: import package
    sentiment2 = ai_models.predict(cleaned1)
    print(f"Method 3 (import ai_models): {sentiment2}")
    
    # Método 4: from package import module
    sentiment3 = mock_model.predict(cleaned1)
    print(f"Method 4 (from ai_models import mock_model): {sentiment3}")
    
    print()


if __name__ == "__main__":
    """
    Entrada del programa.
    Solo se ejecuta cuando el script se ejecuta directamente.
    """
    main()
    demo_different_imports()
