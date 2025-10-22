# task_4.py
# Sección 1. Práctica de programación
# Alejandro Campos Martínez
# Agustín Jaime Navarro
# Team 6

# Diccionario de estudiantes con sus calificaciones
estudiantes = {
    "Agustín": [85, 90, 78, 92, 88],
    "Juan": [70, 75, 80, 85, 90],
    "Hector": [95, 92, 98, 94, 96],
    "Cristian": [60, 65, 70, 68, 72],
    "Gerardo": [88, 85, 90, 87, 91]
}

print("Calificaciones:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n" + "="*50 + "\n")

# Se crea un nuevo diccionario con promedios
promedios = {}

for nombre, calificaciones in estudiantes.items():
    # sum() suma todos los elementos de la lista
    # Dividir entre el número de calificaciones
    promedio = sum(calificaciones) / 5  # Son 5 materias
    promedios[nombre] = promedio

print("Promedios de estudiantes:")
for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")
