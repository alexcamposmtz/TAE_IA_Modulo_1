"""
ECU3.4 - Matrix Multiply Naive
Versión: GPU REAL (Requiere NVIDIA GPU + CUDA Toolkit)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Hardware: NVIDIA RTX 4060 Laptop GPU
Propósito: Multiplicación de matrices naive (sin optimizaciones) para demostrar
           la importancia de optimizaciones como shared memory
"""
import numpy as np
from numba import cuda
import math
import time
from numba import config

config.CUDA_ENABLE_PYNVJITLINK = 1

@cuda.jit
def matmul_naive_kernel(A, B, C):
    """
    Naive matrix multiply: C = A @ B
    Each thread computes one element of C.
    """
    row, col = cuda.grid(2)

    M, K = A.shape
    K2, N = B.shape

    if row < M and col < N:
        total = 0.0
        for k in range(K):
            total += A[row, k] * B[k, col]
        C[row, col] = total

def main():
    print("="*70)
    print("ECU3.4 - Matrix Multiply Naive (GPU REAL)")
    print("Autor: Alejandro Campos Martínez - Team 6")
    print("="*70)
    
    gpu = cuda.get_current_device()
    print(f"GPU detectada: {gpu.name}")
    print(f"Compute Capability: {gpu.compute_capability}")
    print(f"Multiprocessors: {gpu.MULTIPROCESSOR_COUNT}")
    print("-"*70)
    print("ADVERTENCIA: Este kernel naive es ineficiente por diseño")
    
    M, K, N = 1000, 1000, 1000
    print(f"Tamaño de matrices: A({M}x{K}) @ B({K}x{N}) = C({M}x{N})")
    print(f"Total elementos resultado: {M*N:,}")
    print(f"Operaciones: {M*N*K:,} multiplicaciones")
    
    A = np.random.randn(M, K).astype(np.float32)
    B = np.random.randn(K, N).astype(np.float32)
    C = np.zeros((M, N), dtype=np.float32)

    threads_per_block = (16, 16)
    d_A = cuda.to_device(A)
    d_B = cuda.to_device(B)
    d_C = cuda.to_device(C)

    blocks_per_grid_x = (M + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_per_grid_y = (N + threads_per_block[1] - 1) // threads_per_block[1]
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)
    
    print(f"Configuración: ({blocks_per_grid_x}, {blocks_per_grid_y}) bloques")
    print(f"               ({threads_per_block[0]}, {threads_per_block[1]}) threads por bloque")
    print("-"*70)

    # Warmup
    matmul_naive_kernel[blocks_per_grid, threads_per_block](d_A, d_B, d_C)
    cuda.synchronize()

    # GPU timing
    start = time.time()
    matmul_naive_kernel[blocks_per_grid, threads_per_block](d_A, d_B, d_C)
    cuda.synchronize()
    gpu_time = (time.time() - start) * 1000

    C_gpu = d_C.copy_to_host()

    # CPU timing
    cpu_start = time.time()
    C_cpu = A @ B
    cpu_time = (time.time() - cpu_start) * 1000

    print(f"\nGPU kernel time: {gpu_time:.4f} ms")
    print(f"CPU NumPy time: {cpu_time:.4f} ms")
    
    if cpu_time < gpu_time:
        print(f"Slowdown: {gpu_time / cpu_time:.2f}x")
        print("NOTA: Este resultado demuestra la importancia de optimizaciones")
        print("      NumPy usa BLAS con shared memory, cache blocking, etc.")
    else:
        print(f"Speedup: {cpu_time / gpu_time:.2f}x")
    
    print(f"Verificación correcta: {np.allclose(C_gpu, C_cpu, atol=1e-3)}")
    print("="*70)

if __name__ == "__main__":
    main()
