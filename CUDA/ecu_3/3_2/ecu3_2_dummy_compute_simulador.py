"""
ECU3.2 - Dummy Compute (Cálculo de Hipotenusa)
Versión: SIMULADOR (Compatible con Colab y máquinas sin GPU NVIDIA)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Propósito: Cálculo de sqrt(a^2 + b^2) para demostrar operaciones matemáticas
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
def dummy_compute_kernel(a, b, c):
    """
    Simple compute to measure timing: c[i] = sqrt(a[i]^2 + b[i]^2)
    """
    idx = cuda.grid(1)
    if idx < c.size:
        c[idx] = math.sqrt(a[idx]**2 + b[idx]**2)

def main():
    print("="*70)
    print("ECU3.2 - Dummy Compute / Hipotenusa (SIMULADOR)")
    print("Autor: Alejandro Campos Martínez - Team 6")
    print("="*70)
    print("NOTA: Modo simulador - Tiempos no representan rendimiento real\n")
    
    N = 10_000_000
    print(f"Tamaño del vector: {N:,} elementos")
    
    a = np.random.randn(N).astype(np.float32)
    b = np.random.randn(N).astype(np.float32)
    c = np.zeros(N, dtype=np.float32)

    d_a = cuda.to_device(a)
    d_b = cuda.to_device(b)
    d_c = cuda.to_device(c)

    threads_per_block = 256
    blocks_per_grid = math.ceil(N / threads_per_block)
    
    print(f"Configuración: {blocks_per_grid:,} bloques x {threads_per_block} threads")
    print("-"*70)
    
    # Warmup
    dummy_compute_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_c)
    cuda.synchronize()

    # GPU timing
    print("Ejecutando kernel...")
    start = time.time()
    dummy_compute_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_c)
    cuda.synchronize()
    gpu_time = (time.time() - start) * 1000

    result = d_c.copy_to_host()

    # CPU timing
    cpu_start = time.time()
    expected = np.sqrt(a**2 + b**2)
    cpu_time = (time.time() - cpu_start) * 1000

    print(f"\nGPU time: {gpu_time:.3f} ms")
    print(f"CPU time: {cpu_time:.3f} ms")
    print(f"Speedup: {cpu_time / gpu_time:.2f}x")
    print(f"Verificación correcta: {np.allclose(result, expected)}")
    print("="*70)

if __name__ == "__main__":
    main()
