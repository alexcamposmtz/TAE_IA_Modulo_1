# task_3.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# TAREA 3: Juego de Adivinar Número
"""
Se implementa un juego donde el usuario
debe adivinar un número aleatorio entre 1 y 100.
El programa proporciona pistas indicando si el número ingresado
es mayor o menor que el número secreto.
"""

import random

print("=" * 70)
print("JUEGO DE ADIVINAR NÚMERO")
print("=" * 70)

# Generar un número aleatorio entre 1 y 100
secret_number = random.randint(1, 100)
attempts = 0
guessed = False

print("\n¡Bienvenido al Juego de Adivinar Números!")
print("Estoy pensando en un número entre 1 y 100.")
print("¡Intenta adivinarlo!\n")

# Loop principal del juego
while not guessed:
    try:
        # Obtener entrada del usuario
        guess = int(input("Ingresa tu intento: "))
        attempts += 1
        
        # Verificar si el intento es correcto
        if guess == secret_number:
            guessed = True
            print("\n" + "=" * 60)
            print("¡FELICITACIONES!")
            print("=" * 60)
            print(f"¡Adivinaste el número {secret_number} correctamente!")
            print(f"Número de intentos: {attempts}")
            
            # Proporcionar retroalimentación según el rendimiento
            if attempts == 1:
                print("¡Increíble! ¡Lo lograste en el primer intento!")
            elif attempts <= 5:
                print("¡Excelente! ¡Eres muy bueno en esto!")
            elif attempts <= 10:
                print("¡Buen trabajo! ¡Fue bastante rápido!")
            else:
                print("¡Bien hecho! ¡La práctica hace al maestro!")
        
        # Proporcionar pistas
        elif guess < secret_number:
            print(f"{guess} es muy bajo. Intenta con un número más alto.\n")
        else:
            print(f"{guess} es muy alto. Intenta con un número más bajo.\n")
    
    except ValueError:
        print("¡Entrada inválida! Por favor ingresa un número válido.\n")

print("\n¡Gracias por jugar!")
