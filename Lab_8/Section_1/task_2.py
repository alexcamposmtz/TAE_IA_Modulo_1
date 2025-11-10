# task_2.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 2: Generar los puntos de un circulo (o varios circulos concentricos)
usando list comprehension y graficarlos con matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np


def generate_circle_points(radius, num_points=1000):
    """
    Genera los puntos de un circulo usando list comprehension.
    
    Parametros:
        radius (float): Radio del circulo
        num_points (int): Numero de puntos a generar
        
    Retorna:
        tuple: Listas de coordenadas x e y del circulo
    """
    # Generar angulos de 0 a 2*pi
    angles = np.linspace(0, 2 * np.pi, num_points)
    
    # Generar puntos del circulo usando list comprehension
    # x = r * cos(theta), y = r * sin(theta)
    x_points = [radius * np.cos(angle) for angle in angles]
    y_points = [radius * np.sin(angle) for angle in angles]
    
    return x_points, y_points


def generate_concentric_circles(radii, num_points=1000):
    """
    Genera multiples circulos concentricos.
    
    Parametros:
        radii (list): Lista de radios para los circulos
        num_points (int): Numero de puntos por circulo
        
    Retorna:
        list: Lista de tuplas con coordenadas (x, y) de cada circulo
    """
    circles = []
    for radius in radii:
        x, y = generate_circle_points(radius, num_points)
        circles.append((x, y))
    return circles


def plot_circles(circles, radii):
    """
    Grafica los circulos concentricos.
    
    Parametros:
        circles (list): Lista de tuplas con coordenadas de los circulos
        radii (list): Lista de radios correspondientes
    """
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Paleta de colores
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    # Graficar cada circulo
    for i, ((x, y), radius) in enumerate(zip(circles, radii)):
        color = colors[i % len(colors)]
        ax.plot(x, y, linewidth=2.5, color=color, 
                label=f'Radio = {radius}', alpha=0.8)
    
    # Configurar titulo
    ax.set_title('Circulos Concentricos Generados con List Comprehension', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Configurar etiquetas de ejes
    ax.set_xlabel('Eje X', fontsize=14, fontweight='bold')
    ax.set_ylabel('Eje Y', fontsize=14, fontweight='bold')
    
    # Configurar ticks
    max_radius = max(radii)
    tick_values = np.arange(-max_radius, max_radius + 1, 1)
    ax.set_xticks(tick_values)
    ax.set_yticks(tick_values)
    
    # Configurar grid
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.5)
    ax.axvline(x=0, color='black', linewidth=0.8, alpha=0.5)
    
    # Aspecto igual para que los circulos se vean circulares
    ax.set_aspect('equal')
    
    # Leyenda
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    
    # Ajustar limites
    ax.set_xlim([-max_radius - 0.5, max_radius + 0.5])
    ax.set_ylim([-max_radius - 0.5, max_radius + 0.5])
    
    # Ajustar layout
    plt.tight_layout()
    
    # Mostrar grafica
    plt.show()


def plot_individual_circles(circles, radii):
    """
    Grafica cada circulo en un subplot separado.
    
    Parametros:
        circles (list): Lista de tuplas con coordenadas de los circulos
        radii (list): Lista de radios correspondientes
    """
    num_circles = len(circles)
    fig, axes = plt.subplots(1, num_circles, figsize=(5 * num_circles, 5))
    
    if num_circles == 1:
        axes = [axes]
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    for i, ((x, y), radius) in enumerate(zip(circles, radii)):
        color = colors[i % len(colors)]
        axes[i].plot(x, y, linewidth=2.5, color=color)
        axes[i].set_title(f'Circulo Radio = {radius}', 
                         fontsize=12, fontweight='bold')
        axes[i].set_xlabel('X', fontsize=10)
        axes[i].set_ylabel('Y', fontsize=10)
        axes[i].grid(True, alpha=0.3, linestyle='--')
        axes[i].set_aspect('equal')
        axes[i].axhline(y=0, color='black', linewidth=0.5, alpha=0.3)
        axes[i].axvline(x=0, color='black', linewidth=0.5, alpha=0.3)
        
        # Configurar ticks
        tick_values = np.arange(-radius - 1, radius + 2, 1)
        axes[i].set_xticks(tick_values)
        axes[i].set_yticks(tick_values)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 2: CIRCULOS CONCENTRICOS CON MATPLOTLIB")
    print("=" * 70)
    
    print("\n--- Generando circulos con list comprehension ---")
    
    # Definir radios de los circulos concentricos
    radii = [1, 2, 3, 4, 5]
    num_points = 1000
    
    print(f"Numero de circulos: {len(radii)}")
    print(f"Radios: {radii}")
    print(f"Puntos por circulo: {num_points}")
    
    # Generar los circulos
    circles = generate_concentric_circles(radii, num_points)
    
    print("\n--- Circulos generados exitosamente ---")
    print("Cada circulo se genero usando:")
    print("  x = [r * cos(θ) for θ in angles]")
    print("  y = [r * sin(θ) for θ in angles]")
    
    print("\n--- Graficando circulos concentricos ---")
    print("Mostrando grafica con matplotlib...")
    print("La grafica incluye:")
    print("  - Titulo descriptivo")
    print("  - Etiquetas en ambos ejes")
    print("  - Ticks configurados cada 1 unidad")
    print("  - Grid para mejor visualizacion")
    print("  - Leyenda con los radios")
    print("  - Ejes en el centro (x=0, y=0)")
    
    # Graficar todos los circulos juntos
    plot_circles(circles, radii)
    
    print("\n--- Graficando circulos individuales ---")
    print("Mostrando circulos en subplots separados...")
    
    # Graficar circulos individuales
    plot_individual_circles(circles, radii)
    
    print("\nGraficas cerradas.")
