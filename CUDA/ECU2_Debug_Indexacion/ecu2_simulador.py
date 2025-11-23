"""
ECU2 - Debug de indexación de Threads y Bloques
Versión: SIMULADOR (Compatible con Colab y máquinas sin GPU NVIDIA)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Propósito: Demostrar cálculo de IDs globales en grid 2D
"""
import os
# Activar simulador antes que numba
os.environ["NUMBA_ENABLE_CUDASIM"] = "1"

import numpy as np
import time
from numba import cuda
from numba import config

config.CUDA_ENABLE_PYNVJITLINK = 1

@cuda.jit
def whoami():
    """
    Kernel de debugging: Cada thread imprime su configuración
    Demuestra cálculo de IDs en grid 2D
    """
    # Calcular el identificador de bloque en una cuadrícula 3D
    block_id = (
        cuda.blockIdx.x +
        cuda.blockIdx.y * cuda.gridDim.x +
        cuda.gridDim.x * cuda.gridDim.y
    )

    # Hilos por bloque
    threads_per_block = (
        cuda.blockDim.x * cuda.blockDim.y
    )

    # Desplazamiento de este bloque
    block_offset = block_id * threads_per_block

    # Calcular el identificador de hilo dentro del bloque
    thread_offset = (
        cuda.threadIdx.x +
        cuda.threadIdx.y * cuda.blockDim.x +
        cuda.blockDim.x * cuda.blockDim.y
    )

    # Identificador de hilo global a través de todos los bloques
    global_id = block_offset + thread_offset

    print(f"{global_id:03d} | Block[x, y]({cuda.blockIdx.x} {cuda.blockIdx.y}) = {block_id:3d} | "
          f"Thread[x, y] ({cuda.threadIdx.x} {cuda.threadIdx.y} ) = {thread_offset:3d} "
          f"BlockDim.x {cuda.blockDim.x} BlockDim.y {cuda.blockDim.y} "
          f"GridDim.x {cuda.gridDim.x} GridDim.y {cuda.gridDim.y}")


def main():
    print("="*70)
    print("ECU2 - Debug de Indexación de Threads y Bloques (SIMULADOR)")
    print("Alejandro Campos Martínez - Team 6")
    print("="*70)
    print("NOTA: Este kernel usa print() que solo funciona en simulador")
    print("      En GPU real, los prints no se muestran")
    print("-"*70)
    
    # Configuración de grid 2D
    b_x, b_y = 2, 2  # 2x2 bloques
    t_x, t_y = 4, 1  # 4x1 threads por bloque

    blocks_per_grid = (b_x, b_y)
    threads_per_block = (t_x, t_y)

    total_blocks = b_x * b_y
    total_threads = t_x * t_y
    
    print(f"\nConfiguración:")
    print(f"  Bloques en grid: {b_x} x {b_y} = {total_blocks} bloques")
    print(f"  Threads por bloque: {t_x} x {t_y} = {total_threads} threads")
    print(f"  Total de threads: {total_blocks * total_threads} threads")
    print("-"*70)
    print("\nSalida del kernel:\n")

    # Lanza el kernel
    whoami[blocks_per_grid, threads_per_block]()

    # Espera a que la GPU termine de procesar
    cuda.synchronize()
    
    print("\n" + "="*70)
    print("Ejecución completada")
    print("="*70)

if __name__ == "__main__":
    main()
