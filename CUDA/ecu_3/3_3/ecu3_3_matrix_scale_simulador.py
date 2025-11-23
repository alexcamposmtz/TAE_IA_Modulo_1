"""
ECU3.3 - Matrix Scale (Multiplicación por Escalar)
Versión: SIMULADOR (Compatible con Colab y máquinas sin GPU NVIDIA)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Propósito: Multiplicar cada elemento de una matriz por un escalar usando grid 2D
"""
import os
os.environ["NUMBA_ENABLE_CUDASIM"] = "1"

import numpy as np
from numba import cuda
import math
import time
from numba import config

config.CUDA_ENABLE_PYNVJITLINK = 1

@cuda.jit
def matrix_scale_kernel(mat, scalar, out):
    """
    Scale every element: out[row, col] = mat[row, col] * scalar
    """
    row, col = cuda.grid(2)

    if row < out.shape[0] and col < out.shape[1]:
        out[row, col] = mat[row, col] * scalar

def main():
    print("="*70)
    print("ECU3.3 - Matrix Scale (SIMULADOR)")
    print("Autor: Alejandro Campos Martínez - Team 6")
    print("="*70)
    print("NOTA: Modo simulador - Tiempos no representan rendimiento real\n")
    
    rows, cols = 4096, 4096
    print(f"Tamaño de matriz: {rows} x {cols} = {rows*cols:,} elementos")
    print(f"Memoria: {rows*cols*4/1e6:.2f} MB por matriz")
    
    mat = np.random.randn(rows, cols).astype(np.float32)
    out = np.zeros_like(mat)
    scalar = 2.5
    
    d_mat = cuda.to_device(mat)
    d_out = cuda.to_device(out)

    threads_per_block = (16, 16)
    blocks_per_grid_x = math.ceil(rows / threads_per_block[0])
    blocks_per_grid_y = math.ceil(cols / threads_per_block[1])
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)
    
    print(f"Configuración: ({blocks_per_grid_x}, {blocks_per_grid_y}) bloques")
    print(f"               ({threads_per_block[0]}, {threads_per_block[1]}) threads por bloque")
    print(f"Total threads: {blocks_per_grid_x * blocks_per_grid_y * threads_per_block[0] * threads_per_block[1]:,}")
    print("-"*70)

    # Warmup
    matrix_scale_kernel[blocks_per_grid, threads_per_block](d_mat, scalar, d_out)
    cuda.synchronize()

    # GPU timing
    print("Ejecutando kernel...")
    start = time.time()
    matrix_scale_kernel[blocks_per_grid, threads_per_block](d_mat, scalar, d_out)
    cuda.synchronize()
    gpu_time = (time.time() - start) * 1000

    result = d_out.copy_to_host()

    # CPU timing
    cpu_start = time.time()
    expected = mat * scalar
    cpu_time = (time.time() - cpu_start) * 1000

    print(f"\nGPU kernel time: {gpu_time:.3f} ms")
    print(f"CPU NumPy time: {cpu_time:.3f} ms")
    print(f"Speedup: {cpu_time / gpu_time:.2f}x")
    print(f"Verificación correcta: {np.allclose(result, expected)}")
    print("="*70)

if __name__ == "__main__":
    main()
