"""
ECU2 - Debug de indexación de Threads y Bloques
Versión: GPU REAL (Requiere NVIDIA GPU + CUDA Toolkit)
Team 6
Autor: Alejandro Campos Martínez
Curso: TAE en IA - COCYTEN Nayarit
Hardware: NVIDIA RTX 4060 Laptop GPU
Propósito: Demostrar cálculo de IDs globales en grid 2D guardando en arrays
"""
import numpy as np
import time
from numba import cuda
from numba import config

config.CUDA_ENABLE_PYNVJITLINK = 1

@cuda.jit
def whoami_gpu(global_ids, block_ids_x, block_ids_y, thread_ids_x, thread_ids_y, 
               block_dims_x, block_dims_y, grid_dims_x, grid_dims_y):
    """
    Kernel de debugging para GPU real: Guarda información en arrays
    Ya que print() no funciona en GPU real
    """
    # Compute block id in a 2D grid
    block_id = (
        cuda.blockIdx.x +
        cuda.blockIdx.y * cuda.gridDim.x
    )

    # Threads per block
    threads_per_block = (
        cuda.blockDim.x * cuda.blockDim.y
    )

    # Offset of this block
    block_offset = block_id * threads_per_block

    # Compute thread id inside block
    thread_offset = (
        cuda.threadIdx.x +
        cuda.threadIdx.y * cuda.blockDim.x
    )

    # Global thread id across all blocks
    global_id = block_offset + thread_offset
    
    # Guardar información en arrays (en lugar de print)
    global_ids[global_id] = global_id
    block_ids_x[global_id] = cuda.blockIdx.x
    block_ids_y[global_id] = cuda.blockIdx.y
    thread_ids_x[global_id] = cuda.threadIdx.x
    thread_ids_y[global_id] = cuda.threadIdx.y
    block_dims_x[global_id] = cuda.blockDim.x
    block_dims_y[global_id] = cuda.blockDim.y
    grid_dims_x[global_id] = cuda.gridDim.x
    grid_dims_y[global_id] = cuda.gridDim.y


def main():
    print("="*70)
    print("ECU2 - Debug de Indexación de Threads y Bloques (GPU REAL)")
    print("Autor: Alejandro Campos Martínez - Team 6")
    print("="*70)
    
    gpu = cuda.get_current_device()
    print(f"GPU detectada: {gpu.name}")
    print(f"Compute Capability: {gpu.compute_capability}")
    print(f"Multiprocessors: {gpu.MULTIPROCESSOR_COUNT}")
    print("-"*70)
    
    # Configuración de grid 2D
    b_x, b_y = 2, 2  # 2x2 bloques
    t_x, t_y = 4, 1  # 4x1 threads por bloque

    blocks_per_grid = (b_x, b_y)
    threads_per_block = (t_x, t_y)

    total_blocks = b_x * b_y
    total_threads_per_block = t_x * t_y
    total_threads = total_blocks * total_threads_per_block
    
    print(f"\nConfiguración:")
    print(f"  Bloques en grid: {b_x} x {b_y} = {total_blocks} bloques")
    print(f"  Threads por bloque: {t_x} x {t_y} = {total_threads_per_block} threads")
    print(f"  Total de threads: {total_threads} threads")
    print("-"*70)
    
    # Crear arrays para guardar información
    global_ids = np.zeros(total_threads, dtype=np.int32)
    block_ids_x = np.zeros(total_threads, dtype=np.int32)
    block_ids_y = np.zeros(total_threads, dtype=np.int32)
    thread_ids_x = np.zeros(total_threads, dtype=np.int32)
    thread_ids_y = np.zeros(total_threads, dtype=np.int32)
    block_dims_x = np.zeros(total_threads, dtype=np.int32)
    block_dims_y = np.zeros(total_threads, dtype=np.int32)
    grid_dims_x = np.zeros(total_threads, dtype=np.int32)
    grid_dims_y = np.zeros(total_threads, dtype=np.int32)
    
    # Transferir a GPU
    d_global_ids = cuda.to_device(global_ids)
    d_block_ids_x = cuda.to_device(block_ids_x)
    d_block_ids_y = cuda.to_device(block_ids_y)
    d_thread_ids_x = cuda.to_device(thread_ids_x)
    d_thread_ids_y = cuda.to_device(thread_ids_y)
    d_block_dims_x = cuda.to_device(block_dims_x)
    d_block_dims_y = cuda.to_device(block_dims_y)
    d_grid_dims_x = cuda.to_device(grid_dims_x)
    d_grid_dims_y = cuda.to_device(grid_dims_y)

    # Launch kernel
    whoami_gpu[blocks_per_grid, threads_per_block](
        d_global_ids, d_block_ids_x, d_block_ids_y,
        d_thread_ids_x, d_thread_ids_y,
        d_block_dims_x, d_block_dims_y,
        d_grid_dims_x, d_grid_dims_y
    )
    cuda.synchronize()
    
    # Copiar resultados
    global_ids = d_global_ids.copy_to_host()
    block_ids_x = d_block_ids_x.copy_to_host()
    block_ids_y = d_block_ids_y.copy_to_host()
    thread_ids_x = d_thread_ids_x.copy_to_host()
    thread_ids_y = d_thread_ids_y.copy_to_host()
    block_dims_x = d_block_dims_x.copy_to_host()
    block_dims_y = d_block_dims_y.copy_to_host()
    grid_dims_x = d_grid_dims_x.copy_to_host()
    grid_dims_y = d_grid_dims_y.copy_to_host()
    
    # Mostrar resultados
    print("\nResultados del kernel:\n")
    for i in range(total_threads):
        block_id = block_ids_x[i] + block_ids_y[i] * grid_dims_x[i]
        thread_offset = thread_ids_x[i] + thread_ids_y[i] * block_dims_x[i]
        
        print(f"{global_ids[i]:03d} | "
              f"Block[x, y]({block_ids_x[i]} {block_ids_y[i]}) = {block_id:3d} | "
              f"Thread[x, y] ({thread_ids_x[i]} {thread_ids_y[i]} ) = {thread_offset:3d} "
              f"BlockDim.x {block_dims_x[i]} BlockDim.y {block_dims_y[i]} "
              f"GridDim.x {grid_dims_x[i]} GridDim.y {grid_dims_y[i]}")
    
    print("\n" + "="*70)
    print("Ejecución completada")
    print("="*70)

if __name__ == "__main__":
    main()
