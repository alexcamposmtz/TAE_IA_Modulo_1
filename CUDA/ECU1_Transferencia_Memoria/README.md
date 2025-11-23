# ECU1: Transferencia de Memoria CPU-GPU

**Curso:** Talento Altamente Especializado - Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Germán Alfonso Pinedo Díaz
**Estudiante:** Alejandro Campos Martínez  
**Team:** 6  
**Fecha:** 22/11/2025

---

## Objetivo

Demostrar la estructura básica de un programa CUDA implementando un kernel simple de copia de datos, y comparar el rendimiento entre:
- CUDA Simulator (CPU emulando GPU)
- GPU Real (NVIDIA RTX 4060 Laptop)

---

## Descripción del Problema

Implementar un kernel CUDA que copie 10 millones de elementos de un array fuente a un array destino, demostrando:
1. Transferencia de datos CPU a GPU
2. Ejecución de kernel en GPU
3. Transferencia de resultados GPU a CPU
4. Medición de tiempos de cada etapa

---

## Implementación

### Kernel CUDA
```python
@cuda.jit
def first_kernel(a, result):
    """
    Kernel simple: copia datos de 'a' a 'result'
    Cada thread procesa un elemento
    """
    idx = cuda.grid(1)
    if idx < a.size:
        result[idx] = a[idx]
```

### Configuración de Ejecución

- **Tamaño del array:** 10,000,000 elementos (40 MB)
- **Threads por bloque:** 256
- **Bloques por grid:** 39,063
- **Total de threads:** 10,000,128 (con padding)

### Pasos del Programa

1. **Inicializar datos en CPU**
```python
   N = 10_000_000
   a_cpu = np.arange(N, dtype=np.float32)
```

2. **Transferir CPU a GPU**
```python
   a_gpu = cuda.to_device(a_cpu)
   result_gpu = cuda.device_array_like(a_cpu)
```

3. **Configurar y lanzar kernel**
```python
   threads_per_block = 256
   blocks_per_grid = (N + threads_per_block - 1) // threads_per_block
   first_kernel[blocks_per_grid, threads_per_block](a_gpu, result_gpu)
   cuda.synchronize()
```

4. **Transferir GPU a CPU**
```python
   result_from_gpu = result_gpu.copy_to_host()
```

5. **Verificar resultados**
```python
   verificacion = np.allclose(result_cpu, result_from_gpu)
```

---

## Resultados

### Versión Simulador (Desktop Ryzen 7 5700G)

**Hardware:**
- Procesador: AMD Ryzen 7 5700G (8c/16t @ 4.6 GHz)
- GPU: AMD Radeon Vega (integrada) - No compatible con CUDA

**Tiempos:**
```
CPU time: [Medición pendiente]
GPU (simulado) kernel execution: ~1,800,000 ms (~30 minutos)
Total GPU time: ~1,800,000+ ms
Speedup: 0.00x (simulador es más lento que CPU)
Verificación correcta: True
```

**Observaciones:**
- El simulador emula cada thread secuencialmente en CPU
- No hay paralelismo real
- Útil solo para verificar lógica, no para medir rendimiento

---

### Versión GPU Real (RTX 4060 Laptop)

**Hardware:**
- GPU: NVIDIA GeForce RTX 4060 Laptop GPU
- Arquitectura: Ada Lovelace
- Compute Capability: 8.9
- Multiprocessors: 24

**Tiempos detallados:**
```
CPU time: 4.60 ms

GPU transfer to device: 4.31 ms
GPU kernel execution: 0.41 ms
GPU transfer to host: 6.41 ms
Total GPU time: 11.14 ms

Speedup (kernel only): 11.15x
Verificación correcta: True
```

**Distribución del tiempo GPU:**
- Transfer CPU a GPU: 38.7%
- Kernel execution: 3.7%
- Transfer GPU a CPU: 57.6%

---

## Análisis de Resultados

### 1. Speedup del Kernel

El kernel es **11.15x más rápido** que la versión CPU equivalente.

**¿Por qué no es 100x o 1000x?**
- Este kernel es trivial (solo copia memoria)
- No hay operaciones computacionalmente intensivas
- La GPU no puede mostrar todo su potencial con operaciones tan simples

### 2. Overhead de Transferencias

**Observación crítica:** Las transferencias de memoria (10.72 ms) toman **26x más tiempo** que la ejecución del kernel (0.41 ms).

**Implicaciones:**
- Para kernels simples, las transferencias dominan el tiempo total
- En aplicaciones reales, se debe minimizar transferencias:
  - Mantener datos en GPU
  - Procesar múltiples operaciones antes de transferir de vuelta
  - Usar streams para transferencias asíncronas

### 3. Comparación Simulador vs GPU Real

| Métrica | Simulador | GPU Real | Factor |
|---------|-----------|----------|--------|
| Kernel time | ~1,800,000 ms | 0.41 ms | ~4,390,000x |
| Total time | ~1,800,000+ ms | 11.14 ms | ~161,600x |

El simulador es **millones de veces más lento** que la GPU real.

### 4. Warmup y Compilación JIT

**Primera ejecución:**
- Numba compila el kernel a código PTX
- Tiempo adicional de compilación (no medido)

**Solución aplicada:**
```python
# Warmup - primera ejecución compila JIT
first_kernel[blocks_per_grid, threads_per_block](a_gpu, result_gpu)
cuda.synchronize()

# Ahora medir tiempo real
start = time.time()
first_kernel[blocks_per_grid, threads_per_block](a_gpu, result_gpu)
cuda.synchronize()
kernel_time = time.time() - start
```

---

## Errores Encontrados

### Error 1: AttributeError - total_memory

**Descripción:**
```python
AttributeError: total_memory
```

**Código problemático:**
```python
print(f"Memoria total: {gpu.total_memory / 1e9:.2f} GB")
```

**Solución aplicada:**
```python
# Omitir información de memoria o usar contexto
gpu = cuda.get_current_device()
print(f"GPU detectada: {gpu.name}")
print(f"Compute Capability: {gpu.compute_capability}")
print(f"Multiprocessors: {gpu.MULTIPROCESSOR_COUNT}")
```

### Error 2: ModuleNotFoundError

**Descripción:**
```
ModuleNotFoundError: No module named 'numba'
```

**Causa:**
Ejecutar con Python del sistema en lugar de conda.

**Solución:**
```bash
conda activate cuda_curso
python ecu1_gpu_real.py
```

---

## Archivos del Laboratorio

### ecu1_simulador.py
- Compatible con cualquier máquina (con o sin GPU NVIDIA)
- Usa `os.environ["NUMBA_ENABLE_CUDASIM"] = "1"`
- Tiempos extremadamente lentos
- Propósito: Aprendizaje de sintaxis CUDA

### ecu1_gpu_real.py
- Requiere GPU NVIDIA + CUDA Toolkit
- Speedups reales
- Medición detallada de tiempos
- Propósito: Demostración de aceleración real

---

## Ejecución

### Requisitos

**Para ambas versiones:**
```bash
conda create -n cuda_curso python=3.11
conda activate cuda_curso
conda install numba numpy
```

**Solo para GPU real:**
- GPU NVIDIA (cualquier generación)
- Drivers NVIDIA instalados
- CUDA Toolkit (verificar con `nvidia-smi`)

### Comandos
```bash
# Activar ambiente
conda activate cuda_curso

# Versión simulador (lento, ~30 minutos)
python ecu1_simulador.py

# Versión GPU real (rápido, <1 segundo)
python ecu1_gpu_real.py
```

### Desde Jupyter Notebook
```bash
conda activate cuda_curso
jupyter notebook
# Abrir ECU1.ipynb y ejecutar celdas
```

---

## Conceptos Clave Aprendidos

### 1. Estructura Básica CUDA

Todo programa CUDA sigue estos pasos:
1. Inicializar datos en CPU (Host)
2. Alocar memoria en GPU (Device)
3. Transferir datos CPU a GPU
4. Configurar dimensiones de grid/bloques
5. Lanzar kernel
6. Sincronizar GPU
7. Transferir resultados GPU a CPU
8. Liberar memoria GPU

### 2. Indexación de Threads
```python
idx = cuda.grid(1)  # Para grid 1D

# Equivalente a:
idx = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
```

**Verificación de límites:**
```python
if idx < a.size:  # Prevenir accesos fuera de rango
    result[idx] = a[idx]
```

### 3. Sincronización
```python
cuda.synchronize()  # CRÍTICO: Esperar a que GPU termine
```

Sin sincronización, las mediciones de tiempo serían incorrectas.

### 4. Compilación JIT (Just-In-Time)

- Primera ejecución: Compila kernel a PTX/SASS
- Ejecuciones subsecuentes: Usa código compilado
- Siempre hacer "warmup" antes de medir tiempos

---

## Mejores Prácticas Demostradas

### 1. Medición de Tiempos
```python
# CORRECTO: Warmup + Sincronización
first_kernel[blocks, threads](a_gpu, result_gpu)
cuda.synchronize()  # Warmup

start = time.time()
first_kernel[blocks, threads](a_gpu, result_gpu)
cuda.synchronize()  # Importante
kernel_time = time.time() - start
```
```python
# INCORRECTO: Sin sincronización
start = time.time()
first_kernel[blocks, threads](a_gpu, result_gpu)
kernel_time = time.time() - start  # Tiempo incorrecto
```

### 2. Configuración de Grid
```python
# CORRECTO: Manejar tamaños no múltiplos de block size
threads_per_block = 256
blocks_per_grid = (N + threads_per_block - 1) // threads_per_block
```
```python
# INCORRECTO: División simple
blocks_per_grid = N // threads_per_block  # Pierde elementos
```

### 3. Verificación de Resultados
```python
# CORRECTO: Comparación con tolerancia
verificacion = np.allclose(result_cpu, result_gpu)
```
```python
# INCORRECTO: Comparación exacta
verificacion = (result_cpu == result_gpu).all()  # Falla por punto flotante
```

---

## Conclusiones

### Lecciones Clave

El simulador CUDA ha demostrado ser una herramienta exclusivamente educativa. Si bien permite aprender la sintaxis y estructura de programación CUDA sin necesidad de hardware especializado, no debe utilizarse para medir rendimiento real. Su utilidad radica en la verificación de la lógica del código antes de ejecutarlo en hardware real.

Uno de los hallazgos más importantes de este laboratorio es el impacto de las transferencias de memoria entre CPU y GPU. En este ejemplo particular, las transferencias consumen el 96% del tiempo total de ejecución, lo que evidencia que minimizar estos movimientos de datos es fundamental en aplicaciones reales. La estrategia más efectiva consiste en mantener los datos en la GPU el mayor tiempo posible y procesar múltiples operaciones antes de transferir los resultados de vuelta a la CPU.

El speedup observado de 11x es modesto pero esperado para un kernel tan simple como la copia de memoria. Este kernel no presenta operaciones computacionalmente intensivas que permitan a la GPU demostrar todo su potencial. Sin embargo, este resultado es significativo porque demuestra que incluso operaciones triviales se benefician de la arquitectura paralela. En aplicaciones reales con operaciones más complejas, como multiplicaciones de matrices o convoluciones, los speedups pueden alcanzar fácilmente factores de 100 a 1000 veces.

La capacidad de la GPU para procesar 10 millones de elementos en apenas 0.41 milisegundos, equivalente a aproximadamente 24 millones de elementos por milisegundo, ilustra claramente el poder del procesamiento masivamente paralelo. Esta capacidad de escala es precisamente lo que hace a las GPUs indispensables para aplicaciones de inteligencia artificial modernas.

### Aplicación en IA

Los conceptos demostrados en este laboratorio son fundamentales para entender cómo funcionan las operaciones básicas en frameworks de deep learning. Las operaciones de redes neuronales, como las multiplicaciones matriz-vector durante la propagación hacia adelante, dependen de estos mismos principios de paralelización. El procesamiento de imágenes mediante convoluciones, el entrenamiento de modelos a través de backpropagation, y la inferencia en tiempo real son todas aplicaciones que se benefician directamente de la arquitectura que hemos explorado en este ejercicio.

---

## Referencias

- NVIDIA CUDA Programming Guide: https://docs.nvidia.com/cuda/
- Numba CUDA Documentation: https://numba.readthedocs.io/en/stable/cuda/
- Material del curso TAE en IA - COCYTEN Nayarit
- ecu_1_simulador.ipynb - https://colab.research.google.com/drive/1DtPd2H1m0ZMhdU3ngsoQOJs4-OPyMDCT?usp=sharing 
- ecu1_gpu_real.ipynb - https://colab.research.google.com/drive/1NRJV6cTTHWaKMFoo4SJ501M2kjtZcq-Z?usp=sharing
*****************************
---

**Autor:** Alejandro Campos Martínez  
**Team:** 6  
**Versión:** 1.0  
**Hardware:** NVIDIA GeForce RTX 4060 Laptop GPU
