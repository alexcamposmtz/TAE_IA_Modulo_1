"""
ECU1 - Kernel básico de copia de datos
Versión: GPU REAL (Requiere NVIDIA GPU + CUDA Toolkit)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Hardware: NVIDIA RTX 6040
Propósito: Demostrar estructura básica de CUDA con transferencias de memoria
"""
import numpy as np
from numba import cuda
import time
from numba import config
config.CUDA_ENABLE_PYNVJITLINK = 1

#Pasos para usar CUDA:
#Inicializar datos desde la CPU
#Transferir de CPU a GPU
#Ejecutar Kernel con tamaño de grid/block definido (Hilos)
#Transferir resultados de GPU a CPU
#Limpiar memoria

# CUDA kernel Device
@cuda.jit
def first_kernel(a, result):
    idx = cuda.grid(1)
    if idx < a.size:
        result[idx] = a[idx]

#Host
def main():
    print("="*70)
    print("ECU1 - Transferencia de Memoria CPU-GPU (GPU REAL)")
    print("Autor: Alejandro Campos Martínez - Team 6")
    print("="*70)
    
    gpu = cuda.get_current_device()
    print(f"GPU detectada: {gpu.name}")
    print(f"Compute Capability: {gpu.compute_capability}")
    print(f"Memoria total: {gpu.total_memory / 1e9:.2f} GB")
    print(f"Multiprocessors: {gpu.MULTIPROCESSOR_COUNT}")
    print("-"*70)
    
    # 1. Initialize data on CPU
    N = 10_000_000
    print(f"Tamaño del array: {N:,} elementos ({N*4/1e6:.2f} MB)")
    a_cpu = np.arange(N, dtype=np.float32)

    #======================================
    # Computo en CPU
    #======================================
    start = time.time()
    result_cpu = a_cpu.copy()
    cpu_time = time.time() - start
    print(f"\nCPU time: {cpu_time * 1e3:.2f} ms")

    #======================================
    # Computo en GPU
    #======================================
    # Transferencia de CPU a GPU
    start = time.time()
    a_gpu = cuda.to_device(a_cpu)
    result_gpu = cuda.device_array_like(a_cpu) #Reserva Memoria
    transfer_in_time = time.time() - start

    # Configuración y lanzamiento del kernel
    threads_per_block = 256
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block
    print(f"Grid: {blocks_per_grid:,} bloques x {threads_per_block} threads")
    
    # Warmup - primera ejecución compila JIT
    first_kernel[blocks_per_grid, threads_per_block](a_gpu, result_gpu)
    cuda.synchronize()
    
    # Medición de tiempo del kernel
    start = time.time()
    first_kernel[blocks_per_grid, threads_per_block](a_gpu, result_gpu)
    cuda.synchronize()
    kernel_time = time.time() - start

    # Recuperación y medición del tiempo de los resultados
    start = time.time()
    result_from_gpu = result_gpu.copy_to_host()
    cuda.synchronize()
    transfer_out_time = time.time() - start

    # Reporte
    print(f"\nGPU transfer to device: {transfer_in_time * 1e3:.2f} ms")
    print(f"GPU kernel execution: {kernel_time * 1e3:.2f} ms")
    print(f"GPU transfer to host: {transfer_out_time * 1e3:.2f} ms")
    total_gpu = transfer_in_time + kernel_time + transfer_out_time
    print(f"Total GPU time: {total_gpu * 1e3:.2f} ms")
    
    print(f"\nSpeedup (kernel only): {cpu_time / kernel_time:.2f}x")
    print(f"Verificación correcta: {np.allclose(result_cpu, result_from_gpu)}")
    
    print("="*70)
    print("NOTA: Este kernel es trivial (solo copia), por eso el speedup")
    print("      es bajo. En operaciones complejas verás 100-1000x")
    print("="*70)

    # Liberación de memoria
    del a_gpu, result_gpu
    cuda.close()

if __name__ == "__main__":
    main()
