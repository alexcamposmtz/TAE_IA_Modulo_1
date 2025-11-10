# task_1.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 1: Generar dos señales de onda seno con diferentes frecuencias,
multiplicarlas punto por punto usando list comprehension, y graficarlas
usando matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np


def generate_sine_waves():
    """
    Genera dos señales de onda seno con diferentes frecuencias,
    las multiplica punto por punto y las grafica.
    """
    # Generar puntos en el eje x de 0 a 4*pi
    x = np.linspace(0, 4 * np.pi, 1000)
    
    # Generar dos ondas seno con diferentes frecuencias usando list comprehension
    # Frecuencia 1: 1 Hz
    sine_wave_1 = [np.sin(xi) for xi in x]
    
    # Frecuencia 2: 3 Hz
    sine_wave_2 = [np.sin(3 * xi) for xi in x]
    
    # Multiplicar las ondas punto por punto usando list comprehension
    product_wave = [sine_wave_1[i] * sine_wave_2[i] for i in range(len(x))]
    
    return x, sine_wave_1, sine_wave_2, product_wave


def plot_sine_waves(x, sine_wave_1, sine_wave_2, product_wave):
    """
    Grafica las dos ondas seno y su producto.
    
    Parametros:
        x: Valores del eje x
        sine_wave_1: Primera onda seno
        sine_wave_2: Segunda onda seno
        product_wave: Producto de las dos ondas
    """
    # Crear figura y subplots
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # Configuracion de colores y estilos
    color1 = '#2E86AB'
    color2 = '#A23B72'
    color3 = '#F18F01'
    
    # Subplot 1: Primera onda seno
    axes[0].plot(x, sine_wave_1, color=color1, linewidth=2, label='Onda 1 (f=1 Hz)')
    axes[0].set_title('Onda Seno - Frecuencia 1 Hz', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Tiempo (radianes)', fontsize=12)
    axes[0].set_ylabel('Amplitud', fontsize=12)
    axes[0].grid(True, alpha=0.3, linestyle='--')
    axes[0].legend(loc='upper right', fontsize=10)
    axes[0].set_xlim([0, 4 * np.pi])
    axes[0].set_ylim([-1.2, 1.2])
    # Configurar ticks en el eje x
    axes[0].set_xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
    axes[0].set_xticklabels(['0', 'π', '2π', '3π', '4π'])
    axes[0].set_yticks([-1, -0.5, 0, 0.5, 1])
    
    # Subplot 2: Segunda onda seno
    axes[1].plot(x, sine_wave_2, color=color2, linewidth=2, label='Onda 2 (f=3 Hz)')
    axes[1].set_title('Onda Seno - Frecuencia 3 Hz', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Tiempo (radianes)', fontsize=12)
    axes[1].set_ylabel('Amplitud', fontsize=12)
    axes[1].grid(True, alpha=0.3, linestyle='--')
    axes[1].legend(loc='upper right', fontsize=10)
    axes[1].set_xlim([0, 4 * np.pi])
    axes[1].set_ylim([-1.2, 1.2])
    # Configurar ticks en el eje x
    axes[1].set_xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
    axes[1].set_xticklabels(['0', 'π', '2π', '3π', '4π'])
    axes[1].set_yticks([-1, -0.5, 0, 0.5, 1])
    
    # Subplot 3: Producto de las ondas
    axes[2].plot(x, product_wave, color=color3, linewidth=2, label='Producto (Onda 1 × Onda 2)')
    axes[2].set_title('Producto de las Dos Ondas Seno', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Tiempo (radianes)', fontsize=12)
    axes[2].set_ylabel('Amplitud', fontsize=12)
    axes[2].grid(True, alpha=0.3, linestyle='--')
    axes[2].legend(loc='upper right', fontsize=10)
    axes[2].set_xlim([0, 4 * np.pi])
    axes[2].set_ylim([-1.2, 1.2])
    # Configurar ticks en el eje x
    axes[2].set_xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
    axes[2].set_xticklabels(['0', 'π', '2π', '3π', '4π'])
    axes[2].set_yticks([-1, -0.5, 0, 0.5, 1])
    
    # Ajustar espaciado entre subplots
    plt.tight_layout()
    
    # Mostrar grafica
    plt.show()


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 1: ONDAS SENO CON MATPLOTLIB")
    print("=" * 70)
    
    print("\n--- Generando ondas seno con list comprehension ---")
    x, sine_wave_1, sine_wave_2, product_wave = generate_sine_waves()
    
    print(f"Numero de puntos generados: {len(x)}")
    print(f"Rango de x: 0 a {4 * np.pi:.2f} radianes")
    print("\nOndas generadas:")
    print("  - Onda 1: sin(x) con frecuencia 1 Hz")
    print("  - Onda 2: sin(3x) con frecuencia 3 Hz")
    print("  - Producto: Onda 1 × Onda 2 (punto por punto)")
    
    print("\n--- Graficando ondas ---")
    print("Mostrando grafica con matplotlib...")
    print("La grafica incluye:")
    print("  - Titulo en cada subplot")
    print("  - Etiquetas en ambos ejes")
    print("  - Ticks configurados en ambos ejes")
    print("  - Grid para mejor visualizacion")
    print("  - Leyendas para identificar cada onda")
    
    plot_sine_waves(x, sine_wave_1, sine_wave_2, product_wave)
    
    print("\nGrafica cerrada.")
