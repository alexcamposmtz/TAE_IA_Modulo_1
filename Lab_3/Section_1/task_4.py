# task_4.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Validador de Contraseñas

"""
Este programa valida la creación de contraseñas según reglas específicas:
- Mínimo 8 caracteres
- Sin espacios
- No puede contener: &, #, %, @
"""

print("=" * 70)
print("VALIDADOR DE CONTRASEÑAS")
print("=" * 70)
print("\nRequisitos de la Contraseña:")
print("- Al menos 8 caracteres de longitud")
print("- No se permiten espacios")
print("- No puede contener: &, #, %, @")
print()

# Caracteres prohibidos
forbidden_chars = ['&', '#', '%', '@']
password_valid = False

while not password_valid:
    # Obtener contraseña del usuario
    password = input("Ingresa tu nueva contraseña: ")
    
    # Inicializamos banderas de validación
    is_valid = True
    errors = []
    
    # Verificación 1: Longitud mínima (al menos 8 caracteres)
    if len(password) < 8:
        is_valid = False
        errors.append("ERROR: La contraseña debe tener al menos 8 caracteres")
    
    # Verificación 2: Sin espacios
    if ' ' in password:
        is_valid = False
        errors.append("ERROR: La contraseña no puede contener espacios")
    
    # Verificación 3: Sin caracteres prohibidos (&, #, %, @)
    found_forbidden = []
    for char in forbidden_chars:
        if char in password:
            found_forbidden.append(char)
            is_valid = False
    
    if found_forbidden:
        errors.append(f"ERROR: La contraseña no puede contener: {', '.join(found_forbidden)}")
    
    # Mostrar resultados
    if is_valid:
        print("\n" + "=" * 60)
        print("CONTRASEÑA ACEPTADA")
        print("=" * 60)
        print(f"Tu contraseña '{password}' cumple con todos los requisitos.")
        print(f"Longitud de la contraseña: {len(password)} caracteres")
        password_valid = True
    else:
        print("\n" + "=" * 60)
        print("CONTRASEÑA INVALIDA")
        print("=" * 60)
        for error in errors:
            print(error)
        print("\nPor favor intenta de nuevo.\n")