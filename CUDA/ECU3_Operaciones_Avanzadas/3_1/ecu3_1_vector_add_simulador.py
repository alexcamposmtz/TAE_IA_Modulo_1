"""
ECU3.1 - Vector Addition
Versión: SIMULADOR (Compatible con Colab y máquinas sin GPU NVIDIA)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Propósito: Sumar dos vectores elemento por elemento en GPU
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
def vector_add_kernel(a, b, c):
    """
    Each thread computes one element: c[i] = a[i] + b[i]
    """
    idx = cuda.grid(1)
    
    if idx < c.size:
        c[idx] = a[idx] + b[idx]

def main():
    print("="*70)
    print("ECU3.1 - Vector Addition (SIMULADOR)")
    print("Autor: Alejandro Campos Martínez - Team 6")
    print("="*70)
    print("NOTA: Modo simulador \n")
    
    N_large = 10_000_000
    print(f"Tamaño del vector: {N_large:,} elementos")
    
    a = np.random.randn(N_large).astype(np.float32)
    b = np.random.randn(N_large).astype(np.float32)
    c = np.zeros(N_large, dtype=np.float32)

    d_a = cuda.to_device(a)
    d_b = cuda.to_device(b)
    d_c = cuda.to_device(c)

    threads_per_block = 256
    blocks_per_grid = math.ceil(N_large / threads_per_block)
    
    print(f"Configuración: {blocks_per_grid:,} bloques x {threads_per_block} threads")
    print("-"*70)

    # Warmup
    vector_add_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_c)
    cuda.synchronize()

    # GPU timing
    print("Ejecutando kernel...")
    start = time.time()
    vector_add_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_c)
    cuda.synchronize()
    gpu_time = (time.time() - start) * 1000

    result = d_c.copy_to_host()

    # CPU timing
    cpu_start = time.time()
    expected = a + b
    cpu_time = (time.time() - cpu_start) * 1000

    print(f"\nGPU kernel time: {gpu_time:.3f} ms")
    print(f"CPU NumPy time: {cpu_time:.3f} ms")
    print(f"Speedup: {cpu_time / gpu_time:.2f}x")
    print(f"Verificación correcta: {np.allclose(result, expected)}")
    print("="*70)

if __name__ == "__main__":
    main()
