"""
ECU1 - Kernel básico de copia de datos
Versión: SIMULADOR (Compatible con Colab y máquinas sin GPU NVIDIA)
Team 6
Autor: Alejandro Campos Martínez

Curso: TAE en IA - COCYTEN Nayarit
Propósito: Demostrar estructura básica de CUDA con transferencias de memoria
"""
import numpy as np
from numba import cuda
import time
import os
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
    # 1. Initialize data on CPU
    N = 10_000_000
    a_cpu = np.arange(N, dtype=np.float32)

    #======================================
    # Computo en CPU
    #======================================
    # Transferencia al GPU
    start = time.time()
    result_cpu = a_cpu
    cpu_time = time.time() -start
    print(f"CPU time: {cpu_time * 1e3:.2f} ms")

    #======================================
    # Computo en GPU
    #======================================
    # Transferencia de CPU a GPU
    start = time.time()
    a_gpu = cuda.to_device(a_cpu)
    result_gpu = cuda.device_array_like(a_cpu) #Reserva Memoria
    transfer_in_time = time.time() - start

    # Configuración y lanzamiento del kernel 
    threads_per_block = 128
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block
    start = time.time()
    first_kernel[blocks_per_grid, threads_per_block](a_gpu, result_gpu) #launch Kernel
    cuda.synchronize()
    kernel_time = time.time() - start

    #Recuperación y medición del tiempo de los resultados.
    start = time.time()
    result_from_gpu = result_gpu.copy_to_host()
    cuda.synchronize()
    transfer_out_time = time.time() -start

    # Reporte
    print(f"GPU transfer to device: {transfer_in_time * 1e3:.2f} ms")
    print(f"GPU kernel execution: {kernel_time * 1e3:.2f} ms")
    print(f"GPU transfer to host: {transfer_out_time * 1e3:.2f} ms")
    print(f"Total GPU time: {(transfer_in_time + kernel_time + transfer_out_time) * 1e3:.2f} ms")

    # Liberación de memoria
    del a_gpu, result_gpu
    cuda.close()

if __name__ == "__main__":
    main()
