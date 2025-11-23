# ECU2: Debug de Indexación de Threads y Bloques

**Curso:** Talento Altamente Especializado - Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** 
**Estudiante:** Alejandro Campos Martínez  
**Team:** 6  
**Fecha:** 22/11/2025

---

## Objetivo

Comprender la indexación de threads y bloques en CUDA mediante un kernel de debugging que demuestra:
- Cálculo de IDs globales en grid 2D
- Relación entre blockIdx, threadIdx y el ID global
- Diferencias entre implementación en simulador (con print) y GPU real (con arrays)

---

## Descripción del Problema

Implementar un kernel CUDA que muestre información detallada de cada thread:
- ID global del thread
- Posición del bloque (blockIdx.x, blockIdx.y)
- Posición del thread dentro del bloque (threadIdx.x, threadIdx.y)
- Dimensiones del bloque y del grid

**Configuración utilizada:**
- Grid: 2x2 bloques (4 bloques totales)
- Bloques: 4x1 threads (4 threads por bloque)
- Total: 16 threads

---

## Implementación

### Kernel Simulador (con print)
```python
@cuda.jit
def whoami():
    # Calcular ID del bloque en grid 2D
    block_id = (
        cuda.blockIdx.x +
        cuda.blockIdx.y * cuda.gridDim.x
    )

    # Threads por bloque
    threads_per_block = (
        cuda.blockDim.x * cuda.blockDim.y
    )

    # Offset del bloque
    block_offset = block_id * threads_per_block

    # ID del thread dentro del bloque
    thread_offset = (
        cuda.threadIdx.x +
        cuda.threadIdx.y * cuda.blockDim.x
    )

    # ID global del thread
    global_id = block_offset + thread_offset

    # Imprimir información (solo funciona en simulador)
    print(f"{global_id:03d} | Block[x, y]({cuda.blockIdx.x} {cuda.blockIdx.y}) = {block_id:3d} | "
          f"Thread[x, y] ({cuda.threadIdx.x} {cuda.threadIdx.y} ) = {thread_offset:3d}")
```

### Kernel GPU Real (con arrays)
```python
@cuda.jit
def whoami_gpu(global_ids, block_ids_x, block_ids_y, thread_ids_x, thread_ids_y, 
               block_dims_x, block_dims_y, grid_dims_x, grid_dims_y):
    # Mismos cálculos que simulador
    block_id = cuda.blockIdx.x + cuda.blockIdx.y * cuda.gridDim.x
    threads_per_block = cuda.blockDim.x * cuda.blockDim.y
    block_offset = block_id * threads_per_block
    thread_offset = cuda.threadIdx.x + cuda.threadIdx.y * cuda.blockDim.x
    global_id = block_offset + thread_offset
    
    # Guardar en arrays en lugar de print
    global_ids[global_id] = global_id
    block_ids_x[global_id] = cuda.blockIdx.x
    block_ids_y[global_id] = cuda.blockIdx.y
    thread_ids_x[global_id] = cuda.threadIdx.x
    thread_ids_y[global_id] = cuda.threadIdx.y
    # ... etc
```

---

## Conceptos Clave

### 1. Jerarquía de Indexación CUDA
```
Grid (Malla completa)
 └── Block (Bloque de threads)
      └── Thread (Unidad mínima)
```

**Dimensiones disponibles:**
- `gridDim.x, gridDim.y, gridDim.z`: Tamaño del grid en cada dimensión
- `blockDim.x, blockDim.y, blockDim.z`: Tamaño del bloque en cada dimensión
- `blockIdx.x, blockIdx.y, blockIdx.z`: Posición del bloque en el grid
- `threadIdx.x, threadIdx.y, threadIdx.z`: Posición del thread en el bloque

### 2. Cálculo de ID Global

**Para grid 2D (usado en este lab):**
```python
# ID del bloque en el grid
block_id = blockIdx.x + blockIdx.y * gridDim.x

# Threads totales por bloque
threads_per_block = blockDim.x * blockDim.y

# Offset de este bloque
block_offset = block_id * threads_per_block

# ID del thread dentro del bloque
thread_offset = threadIdx.x + threadIdx.y * blockDim.x

# ID global
global_id = block_offset + thread_offset
```

**Para grid 1D (más común):**
```python
global_id = cuda.grid(1)
# Equivalente a:
global_id = blockIdx.x * blockDim.x + threadIdx.x
```

### 3. Limitación de print() en CUDA

**Simulador:**
- `print()` funciona normalmente
- Cada thread puede imprimir
- Útil para debugging

**GPU Real:**
- `print()` NO funciona en kernels
- No hay salida en pantalla
- Alternativa: Guardar en arrays y mostrar en CPU

---

## Resultados

### Configuración
```
Bloques en grid: 2 x 2 = 4 bloques
Threads por bloque: 4 x 1 = 4 threads
Total de threads: 16 threads
```

### Salida del Kernel (RTX 4060 Laptop GPU)
```
000 | Block[x, y](0 0) =   0 | Thread[x, y] (0 0 ) =   0 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
001 | Block[x, y](0 0) =   0 | Thread[x, y] (1 0 ) =   1 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
002 | Block[x, y](0 0) =   0 | Thread[x, y] (2 0 ) =   2 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
003 | Block[x, y](0 0) =   0 | Thread[x, y] (3 0 ) =   3 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
004 | Block[x, y](1 0) =   1 | Thread[x, y] (0 0 ) =   0 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
005 | Block[x, y](1 0) =   1 | Thread[x, y] (1 0 ) =   1 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
006 | Block[x, y](1 0) =   1 | Thread[x, y] (2 0 ) =   2 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
007 | Block[x, y](1 0) =   1 | Thread[x, y] (3 0 ) =   3 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
008 | Block[x, y](0 1) =   2 | Thread[x, y] (0 0 ) =   0 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
009 | Block[x, y](0 1) =   2 | Thread[x, y] (1 0 ) =   1 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
010 | Block[x, y](0 1) =   2 | Thread[x, y] (2 0 ) =   2 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
011 | Block[x, y](0 1) =   2 | Thread[x, y] (3 0 ) =   3 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
012 | Block[x, y](1 1) =   3 | Thread[x, y] (0 0 ) =   0 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
013 | Block[x, y](1 1) =   3 | Thread[x, y] (1 0 ) =   1 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
014 | Block[x, y](1 1) =   3 | Thread[x, y] (2 0 ) =   2 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
015 | Block[x, y](1 1) =   3 | Thread[x, y] (3 0 ) =   3 BlockDim.x 4 BlockDim.y 1 GridDim.x 2 GridDim.y 2
```

---

## Análisis de Resultados

### Patrón Observado

**Threads 0-3 (Block 0,0):**
- Todos tienen blockIdx = (0,0)
- threadIdx.x varía de 0 a 3
- global_id = 0 a 3

**Threads 4-7 (Block 1,0):**
- Todos tienen blockIdx = (1,0)
- threadIdx.x varía de 0 a 3
- global_id = 4 a 7

**Threads 8-11 (Block 0,1):**
- Todos tienen blockIdx = (0,1)
- threadIdx.x varía de 0 a 3
- global_id = 8 a 11

**Threads 12-15 (Block 1,1):**
- Todos tienen blockIdx = (1,1)
- threadIdx.x varía de 0 a 3
- global_id = 12 a 15

### Fórmula Verificada

Para cada thread, la relación se mantiene consistentemente:
```
global_id = (blockIdx.x + blockIdx.y * gridDim.x) * (blockDim.x * blockDim.y) 
            + (threadIdx.x + threadIdx.y * blockDim.x)
```

**Ejemplo - Thread con global_id = 9:**
- blockIdx = (0, 1)
- threadIdx = (1, 0)
- block_id = 0 + 1*2 = 2
- block_offset = 2 * 4 = 8
- thread_offset = 1 + 0*4 = 1
- global_id = 8 + 1 = 9

---

## Errores y Warnings Encontrados

### Warning: NumbaPerformanceWarning - Low Occupancy

**Descripción:**
```
/home/xandro/anaconda3/lib/python3.12/site-packages/numba/cuda/dispatcher.py:536: 
NumbaPerformanceWarning: Grid size 4 will likely result in GPU under-utilization 
due to low occupancy.
  warn(NumbaPerformanceWarning(msg))
```

**Contexto:**

Este warning apareció al ejecutar el código en la RTX 4060. Numba detectó que la configuración de grid (4 bloques, 16 threads totales) resulta en una utilización muy baja de la GPU, aproximadamente 17% de ocupación (4 de 24 multiprocessors activos).

**Análisis:**

El código original del laboratorio fue diseñado para ejecución en simulador (Colab) con propósitos educativos, usando una configuración pequeña para facilitar la comprensión de la indexación de threads. Al adaptarlo para GPU real, mantuve la misma configuración para preservar la comparabilidad entre ambas versiones.

**Observaciones:**

- La baja ocupación es resultado de mantener la configuración original del laboratorio
- En aplicaciones de producción, una GPU como la RTX 4060 típicamente usaría configuraciones con cientos o miles de bloques
- Para este ejercicio específico de debugging de indexación, la configuración pequeña facilita la verificación manual de resultados

---

## Diferencias Entre Versiones

| Aspecto | Simulador | GPU Real |
|---------|-----------|----------|
| **print() en kernel** | Funciona | No funciona |
| **Método de output** | Impresión directa | Arrays intermedios |
| **Complejidad código** | Más simple | Más elaborado |
| **Propósito** | Aprendizaje rápido | Producción real |
| **Velocidad** | Muy lento | Instantáneo |

---

## Archivos del Laboratorio

### ecu2_simulador.py
- Usa print() directamente en kernel
- Solo funciona con CUDASIM activado
- Propósito: Aprendizaje y debugging

### ecu2_gpu_real.py
- Guarda información en arrays
- Funciona en cualquier GPU NVIDIA
- Propósito: Técnica aplicable en entorno real

---

## Ejecución

### Requisitos
```bash
conda create -n cuda_curso python=3.11
conda activate cuda_curso
conda install numba numpy
```

### Comandos
```bash
# Activar ambiente
conda activate cuda_curso

# Versión simulador
python ecu2_simulador.py

# Versión GPU real
python ecu2_gpu_real.py
```

---

## Aplicaciones Prácticas

### 1. Debugging de Kernels Complejos
Entender qué thread procesa qué dato es crucial para:
- Verificar correctitud de algoritmos
- Optimizar accesos a memoria
- Detectar race conditions

### 2. Procesamiento de Imágenes
En convoluciones 2D, cada thread procesa un pixel:
```python
row = blockIdx.y * blockDim.y + threadIdx.y
col = blockIdx.x * blockDim.x + threadIdx.x
pixel = image[row, col]
```

### 3. Multiplicación de Matrices
Cada thread calcula un elemento de la matriz resultado:
```python
row = blockIdx.y * blockDim.y + threadIdx.y
col = blockIdx.x * blockDim.x + threadIdx.x
C[row, col] = dot(A[row, :], B[:, col])
```

---

## Conclusiones

Este laboratorio demuestra un concepto fundamental en programación CUDA que a menudo genera confusión entre programadores nuevos. La indexación de threads es la base sobre la cual se construyen todos los algoritmos paralelos en GPU. Comprender cómo se relacionan los índices locales del thread dentro de su bloque con el índice global dentro de toda la malla de ejecución es esencial para escribir kernels correctos.

La diferencia entre las versiones de simulador y GPU real presenta una limitación importante del desarrollo CUDA. Mientras que en programación tradicional podemos usar print statements libremente para debugging, en CUDA debemos adoptar estrategias diferentes. La técnica de guardar información en arrays para su posterior análisis en la CPU no solo es un workaround para la limitación de print, sino que representa una mejor práctica general para debugging de alto rendimiento.

El patrón de indexación 2D presentado en este laboratorio es particularmente relevante para procesamiento de imágenes y operaciones con matrices, dos pilares fundamentales en aplicaciones de inteligencia artificial. La capacidad de mapear cada thread a una posición específica en una estructura de datos bidimensional permite paralelizar naturalmente operaciones que de otro modo serían secuenciales.

---

## Referencias

- NVIDIA CUDA Programming Guide: https://docs.nvidia.com/cuda/
- Numba CUDA Documentation: https://numba.readthedocs.io/en/stable/cuda/
- Material del curso TAE en IA - COCYTEN Nayarit

---

**Autor:** Alejandro Campos Martínez  
**Team:** 6  
**Versión:** 1.0  
**Hardware:** NVIDIA GeForce RTX 4060 Laptop GPU
