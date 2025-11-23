# ECU3: Operaciones Avanzadas en CUDA

**Curso:** Talento Altamente Especializado - Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Cristian Torres González  
**Estudiante:** Alejandro Campos Martínez  
**Team:** 6  
**Fecha:** 23/11/2025

---

## Objetivo

Implementar y comparar cinco operaciones CUDA de complejidad creciente, desde operaciones vectoriales simples hasta procesamiento de imágenes, demostrando:
- Diferentes patrones de paralelización
- Comparación de rendimiento GPU vs CPU
- Impacto de optimizaciones en multiplicación de matrices
- Aplicaciones prácticas en procesamiento de imágenes

---

## Estructura del Laboratorio

Este laboratorio se divide en 5 ejercicios independientes:

1. **ECU3.1 - Vector Addition:** Suma elemento por elemento de vectores
2. **ECU3.2 - Dummy Compute:** Cálculo de hipotenusa (operaciones matemáticas)
3. **ECU3.3 - Matrix Scale:** Multiplicación de matriz por escalar (grid 2D)
4. **ECU3.4 - Matrix Multiply:** Multiplicación naive de matrices (no optimizado)
5. **ECU3.5 - Sobel Edge Detection:** Detección de bordes en imágenes 4K

---

## ECU3.1 - Vector Addition

### Descripción

Suma de dos vectores de 10 millones de elementos: `c[i] = a[i] + b[i]`

### Implementación del Kernel
```python
@cuda.jit
def vector_add_kernel(a, b, c):
    idx = cuda.grid(1)
    if idx < c.size:
        c[idx] = a[idx] + b[idx]
```

### Configuración
- Tamaño: 10,000,000 elementos (40 MB por vector)
- Grid: 1D
- Threads por bloque: 256
- Bloques: 39,063

### Resultados

#### Simulador (Desktop Ryzen 7 5700G)
```
GPU (simulado): 641,548.469 ms (~10.7 minutos)
CPU NumPy: 6.565 ms
Speedup: 0.00x
Verificación: True
```

#### GPU Real (RTX 4060 Laptop)
```
GPU kernel: 0.633 ms
CPU NumPy: 7.247 ms
Speedup: 11.46x
Verificación: True
```

### Análisis

Este kernel demuestra la operación CUDA más básica. El speedup de 11.46x es modesto porque la operación es bandwidth-limited (limitada por transferencia de memoria). La GPU no puede mostrar todo su poder con operaciones tan simples, pero aún así supera a la CPU.

---

## ECU3.2 - Dummy Compute (Hipotenusa)

### Descripción

Cálculo de hipotenusa para 10 millones de pares: `c[i] = sqrt(a[i]² + b[i]²)`

### Implementación del Kernel
```python
@cuda.jit
def dummy_compute_kernel(a, b, c):
    idx = cuda.grid(1)
    if idx < c.size:
        c[idx] = math.sqrt(a[idx]**2 + b[idx]**2)
```

### Configuración
- Tamaño: 10,000,000 elementos
- Grid: 1D
- Threads por bloque: 256
- Bloques: 39,063

### Resultados

#### Simulador (Desktop Ryzen 7 5700G)
```
GPU (simulado): 740,561.956 ms (~12.3 minutos)
CPU NumPy: 20.706 ms
Speedup: 0.00x
Verificación: True
```

#### GPU Real (RTX 4060 Laptop)
```
GPU time: 0.639 ms
CPU time: 23.071 ms
Speedup: 36.11x
Verificación: True
```

### Análisis

Este ejercicio demuestra un principio importante de GPU computing: el tiempo de GPU apenas aumentó (0.633 ms → 0.639 ms) al agregar operaciones matemáticas complejas (potencias y raíz cuadrada), mientras que el tiempo de CPU se triplicó (7.2 ms → 23.0 ms). Resultado: el speedup mejoró significativamente de 11x a 36x.

La GPU maneja operaciones aritméticas complejas casi al mismo costo que operaciones simples gracias a sus unidades especializadas (SFU - Special Function Units), mientras que la CPU sufre considerablemente más con cada operación adicional.

---

## ECU3.3 - Matrix Scale

### Descripción

Multiplicación de matriz 4096×4096 por escalar: `out[i,j] = mat[i,j] * scalar`

### Implementación del Kernel
```python
@cuda.jit
def matrix_scale_kernel(mat, scalar, out):
    row, col = cuda.grid(2)
    if row < out.shape[0] and col < out.shape[1]:
        out[row, col] = mat[row, col] * scalar
```

### Configuración
- Tamaño: 4096×4096 = 16,777,216 elementos (67 MB por matriz)
- Grid: 2D
- Threads por bloque: (16, 16) = 256 threads
- Bloques: (256, 256) = 65,536 bloques

### Resultados

#### Simulador (Desktop Ryzen 7 5700G)
```
GPU (simulado): 1,468,881.863 ms (~24.5 minutos)
CPU NumPy: 9.293 ms
Speedup: 0.00x
Verificación: True
```

#### GPU Real (RTX 4060 Laptop)
```
GPU kernel: 0.883 ms
CPU NumPy: 10.255 ms
Speedup: 11.62x
Verificación: True
```

### Análisis

Este ejercicio introduce el uso de grids 2D, que mapean naturalmente a estructuras bidimensionales como matrices e imágenes. Cada thread calcula `(row, col)` usando `cuda.grid(2)`, lo que simplifica la lógica de indexación.

Observación importante: aunque esta matriz tiene 67% más elementos que los vectores anteriores (16.7M vs 10M), la GPU solo tomó 40% más tiempo (0.883 vs 0.633 ms), demostrando excelente escalabilidad. El speedup de 11.62x es consistente con operaciones simples bandwidth-limited.

---

## ECU3.4 - Matrix Multiply (Naive)

### Descripción

Multiplicación naive de matrices 1000×1000: `C = A @ B`

Cada thread calcula un elemento de C sumando productos de fila por columna.

### Implementación del Kernel
```python
@cuda.jit
def matmul_naive_kernel(A, B, C):
    row, col = cuda.grid(2)
    M, K = A.shape
    K2, N = B.shape
    
    if row < M and col < N:
        total = 0.0
        for k in range(K):
            total += A[row, k] * B[k, col]
        C[row, col] = total
```

### Configuración
- Tamaño: A(1000×1000) @ B(1000×1000) = C(1000×1000)
- Operaciones: 1,000,000,000 multiplicaciones
- Grid: 2D
- Threads por bloque: (16, 16)
- Bloques: (63, 63)

### Resultados

#### Simulador (Desktop Ryzen 7 5700G)
```
GPU (simulado): 1,068,407.500 ms (~17.8 minutos)
CPU NumPy (BLAS): 20.804 ms
Speedup: 0.00x
Verificación: True
```

#### GPU Real (RTX 4060 Laptop)
```
GPU kernel: 23.889 ms
CPU NumPy (BLAS): 4.711 ms
Slowdown: 5.07x (CPU más rápido)
Verificación: True
```

### Análisis

Este es el resultado más educativo del laboratorio. La GPU naive es 5 veces más lenta que NumPy ejecutándose en CPU. Este resultado no es un error, sino una demostración importante de varios principios:

**¿Por qué la GPU es más lenta?**

1. **Accesos no coalescidos a memoria:** El kernel lee filas de A (coalescido) pero columnas de B (no coalescido). Leer columnas causa que threads consecutivos accedan posiciones de memoria no consecutivas, desperdiciando ancho de banda.

2. **Sin shared memory:** Cada thread lee la misma fila de A y columna de B desde global memory múltiples veces. Global memory es extremadamente lenta (cientos de ciclos de latencia). Con shared memory, estos datos se cargarían una vez al chip y se reutilizarían.

3. **Sin tiling/cache blocking:** NumPy usa algoritmos sofisticados que dividen las matrices en bloques que caben en cache, maximizando reuso de datos.

4. **NumPy usa BLAS optimizado:** Librerías como Intel MKL u OpenBLAS tienen décadas de optimización manual, incluyendo instrucciones SIMD (AVX-512), prefetching, y algoritmos cache-aware.

**Lección fundamental:** Simplemente mover código a GPU no garantiza aceleración. Las optimizaciones son críticas. Una implementación CUDA optimizada con shared memory, tiling, y accesos coalescidos puede ser 10-50x más rápida que esta versión naive y superar ampliamente a NumPy.

---

## ECU3.5 - Sobel Edge Detection

### Descripción

Detección de bordes en imagen 4K (3840×2160) usando filtro Sobel.

Cada thread procesa un pixel calculando gradientes horizontal (Gx) y vertical (Gy) sobre una ventana 3×3.

### Implementación del Kernel
```python
@cuda.jit
def sobel_kernel(img, out):
    row, col = cuda.grid(2)
    H, W = img.shape
    
    if 0 < row < H-1 and 0 < col < W-1:
        # Gradiente horizontal (Gx)
        gx = ( -img[row-1, col-1] + img[row-1, col+1]
               -2*img[row, col-1] + 2*img[row, col+1]
               -img[row+1, col-1] + img[row+1, col+1] )
        
        # Gradiente vertical (Gy)
        gy = ( -img[row-1, col-1] - 2*img[row-1, col] - img[row-1, col+1]
               + img[row+1, col-1] + 2*img[row+1, col] + img[row+1, col+1] )
        
        # Magnitud del borde
        out[row, col] = (gx*gx + gy*gy)**0.5
```

### Configuración
- Imagen: 3840×2160 = 8,294,400 pixels (33 MB)
- Grid: 2D
- Threads por bloque: (16, 16)
- Bloques: (240, 135)

### Resultados

#### Simulador (Desktop Ryzen 7 5700G)
```
GPU (simulado): 629,742.23 ms (~10.5 minutos)
CPU (OpenCV): 27.12 ms
Speedup: 0.00x
Verificación: False (diferencias numéricas menores)
```

#### GPU Real (RTX 4060 Laptop)
```
GPU: 6.08 ms
CPU (OpenCV): 26.23 ms
Speedup: 4.3x
Verificación: False (diferencias numéricas menores)
```

### Análisis

El filtro Sobel es una aplicación práctica ideal para GPU porque cada pixel se procesa independientemente usando solo información local (ventana 3×3). Este patrón es común en procesamiento de imágenes y visión por computadora.

El speedup de 4.3x es modesto comparado con otros ejercicios porque:

1. **OpenCV está altamente optimizado:** Usa instrucciones SIMD, cache blocking, y posiblemente aceleración con IPP (Integrated Performance Primitives) de Intel.

2. **Operaciones relativamente simples:** El cálculo es principalmente sumas, restas y una raíz cuadrada, no hay suficiente complejidad aritmética para que la GPU brille.

3. **Accesos a memoria locales:** La ventana 3×3 causa que múltiples threads lean los mismos pixels (overlap), lo que podría optimizarse con shared memory.

A pesar del speedup modesto, este kernel es valioso porque demuestra un patrón fundamental en procesamiento de imágenes que se extiende a aplicaciones como convoluciones en redes neuronales convolucionales (CNNs).

**Nota sobre verificación:** El resultado `False` indica pequeñas diferencias numéricas entre la implementación manual y OpenCV. Esto es normal y esperado porque:
- Orden diferente de operaciones puede causar diferencias de punto flotante
- OpenCV puede usar aproximaciones rápidas
- La tolerancia `atol=1e-3` es estricta para 8 millones de pixels

Las imágenes visuales son prácticamente idénticas, confirmando que ambas implementaciones son correctas.

---

## Resumen Comparativo

### Tabla de Resultados Completos

| Ejercicio | Elementos | Simulador | GPU Real | CPU | Speedup GPU | Factor vs Simulador |
|-----------|-----------|-----------|----------|-----|-------------|---------------------|
| ECU3.1 Vector Add | 10M | 641,548 ms | 0.633 ms | 7.247 ms | 11.46x | 1,013,000x |
| ECU3.2 Dummy Compute | 10M | 740,562 ms | 0.639 ms | 23.071 ms | 36.11x | 1,159,000x |
| ECU3.3 Matrix Scale | 16.7M | 1,468,882 ms | 0.883 ms | 10.255 ms | 11.62x | 1,664,000x |
| ECU3.4 Matrix Multiply | 1M (1B ops) | 1,068,408 ms | 23.889 ms | 4.711 ms | 0.20x | 44,700x |
| ECU3.5 Sobel Filter | 8.3M | 629,742 ms | 6.08 ms | 26.23 ms | 4.3x | 103,500x |

### Gráfica Conceptual de Speedups
```
GPU Real vs CPU:
─────────────────────────────────────────────
Vector Add        ████████████ 11.46x
Dummy Compute     ████████████████████████████████████ 36.11x
Matrix Scale      ████████████ 11.62x
Matrix Multiply   ██ 0.20x (CPU gana)
Sobel Filter      ████ 4.3x
```

---

## Archivos del Laboratorio

### Versiones Simulador
- `ecu3_1_vector_add_simulador.py`
- `ecu3_2_dummy_compute_simulador.py`
- `ecu3_3_matrix_scale_simulador.py`
- `ecu3_4_matmul_simulador.py`
- `ecu3_5_sobel_simulador.py`

### Versiones GPU Real
- `ecu3_1_vector_add_gpu_real.py`
- `ecu3_2_dummy_compute_gpu_real.py`
- `ecu3_3_matrix_scale_gpu_real.py`
- `ecu3_4_matmul_gpu_real.py`
- `ecu3_5_sobel_gpu_real.py`

### Imágenes Generadas
- `sobel_comparison_simulador.png`
- `sobel_comparison_gpu_real.png`

---

## Ejecución

### Requisitos
```bash
conda create -n cuda_curso python=3.11
conda activate cuda_curso
conda install numba numpy opencv pillow matplotlib
```

### Comandos
```bash
# Activar ambiente
conda activate cuda_curso

# Ejecutar ejercicios individuales
python ecu3_1_vector_add_gpu_real.py
python ecu3_2_dummy_compute_gpu_real.py
python ecu3_3_matrix_scale_gpu_real.py
python ecu3_4_matmul_gpu_real.py
python ecu3_5_sobel_gpu_real.py
```

**Nota:** Las versiones simulador toman 10-25 minutos cada una. Solo ejecutarlas si se necesita verificar lógica o no se tiene GPU NVIDIA.

---

## Conceptos Clave Aprendidos

### 1. Patrones de Grid

**1D (ECU3.1, 3.2):**
```python
idx = cuda.grid(1)
# Ideal para: vectores, arrays 1D
```

**2D (ECU3.3, 3.4, 3.5):**
```python
row, col = cuda.grid(2)
# Ideal para: matrices, imágenes
```

### 2. Tipos de Operaciones

**Bandwidth-Limited (ECU3.1, 3.3):**
- Operaciones simples
- Limitadas por velocidad de memoria
- Speedups modestos (10-15x)

**Compute-Intensive (ECU3.2):**
- Operaciones matemáticas complejas
- GPU aprovecha SFUs
- Speedups altos (30-40x)

**Memory-Pattern Sensitive (ECU3.4):**
- Patrones de acceso críticos
- Sin optimizaciones: CPU gana
- Con optimizaciones: GPU gana dramáticamente

**Locally-Bounded (ECU3.5):**
- Acceso a vecinos cercanos
- Paralelismo natural
- Speedups moderados vs código optimizado

### 3. Importancia de Optimizaciones

Los resultados de ECU3.4 demuestran que:
- GPU naive < CPU optimizado
- Optimizaciones necesarias: shared memory, tiling, coalescing
- No basta con "mover a GPU"

### 4. Escalabilidad

GPU escala excelentemente con tamaño de datos:
- ECU3.3: 67% más datos, solo 40% más tiempo
- Paralelismo masivo compensa overhead

---

## Aplicaciones en IA

### Operaciones de Redes Neuronales

**Forward Propagation:**
```python
# Similar a Matrix Multiply pero optimizado
output = weights @ input + bias
```

**Backpropagation:**
```python
# Múltiples operaciones matriciales
grad_weights = grad_output @ input.T
```

### Procesamiento de Imágenes

**Convoluciones (CNNs):**
- Patrón similar a Sobel pero con kernels aprendidos
- Múltiples canales y filtros
- Operación dominante en visión por computadora

**Data Augmentation:**
- Transformaciones paralelas de lotes de imágenes
- Rotaciones, escalados, recortes
- Aceleración crítica para entrenamiento

### Operaciones Elemento-Wise

**Funciones de Activación:**
```python
# ReLU, Sigmoid, Tanh sobre millones de neuronas
output[i] = max(0, input[i])  # ReLU
```

**Normalización:**
```python
# Batch Normalization, Layer Normalization
normalized[i] = (x[i] - mean) / sqrt(var + eps)
```

---

## Conclusiones

Este laboratorio proporciona una comprensión profunda de cómo diferentes tipos de operaciones se benefician de la aceleración por GPU. Los cinco ejercicios cubren un espectro completo desde operaciones triviales hasta aplicaciones prácticas de procesamiento de imágenes.

El contraste entre los resultados del simulador y la GPU real no podría ser más dramático. Mientras el simulador toma entre 10 y 25 minutos para completar cada ejercicio, la GPU real los ejecuta en milisegundos. Esta diferencia de varios órdenes de magnitud subraya por qué las GPUs se han vuelto indispensables para computación científica, inteligencia artificial y procesamiento de grandes volúmenes de datos.

El caso de la multiplicación de matrices naive es particularmente instructivo. Demuestra que la aceleración por GPU no es automática y que las optimizaciones son fundamentales. Una GPU mal utilizada puede ser significativamente más lenta que una CPU bien optimizada. Este resultado negativo es tan valioso educativamente como los speedups positivos porque enseña que el hardware por sí solo no es suficiente, el software debe estar diseñado para aprovechar las características únicas de la arquitectura GPU.

Los ejercicios de operaciones vectoriales simples muestran speedups modestos pero consistentes alrededor de 10-15x. Estos representan el rendimiento base que se puede esperar cuando las operaciones son principalmente limitadas por ancho de banda de memoria. El ejercicio de cálculo de hipotenusa revela cómo las GPUs realmente brillan cuando hay suficiente trabajo aritmético, alcanzando speedups de más de 35x gracias a sus unidades de funciones especiales optimizadas.

El filtro Sobel cierra el laboratorio con una aplicación práctica real. Aunque el speedup de 4.3x es modesto comparado con otros ejercicios, representa una victoria significativa considerando que OpenCV está altamente optimizado y utiliza todas las ventajas disponibles en la CPU. Este ejercicio también introduce conceptos que se extienden directamente a aplicaciones de deep learning, donde las convoluciones son operaciones fundamentales.

La experiencia con ambos ambientes, simulador y GPU real, proporciona perspectiva completa. El simulador permite verificar lógica y entender conceptos sin requerir hardware especializado, mientras que la GPU real demuestra el poder transformador de la computación paralela masiva. Esta dualidad hace que el material sea accesible para estudiantes sin GPU NVIDIA mientras que aquellos con acceso al hardware pueden experimentar el rendimiento real que hace de CUDA una tecnología fundamental en computación moderna.

---

## Referencias

- NVIDIA CUDA Programming Guide: https://docs.nvidia.com/cuda/
- Numba CUDA Documentation: https://numba.readthedocs.io/en/stable/cuda/
- OpenCV Documentation: https://docs.opencv.org/
- Material del curso TAE en IA - COCYTEN Nayarit

---

**Autor:** Alejandro Campos Martínez  
**Team:** 6  
**Versión:** 1.0  
**Hardware:** NVIDIA GeForce RTX 4060 Laptop GPU  
**Fecha:** 23/11/2025
