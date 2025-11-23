# Laboratorios CUDA: Comparación Simulador vs GPU Real

**Curso:** Talento Altamente Especializado - Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Germán Alfonso Pinedo Díaz
**Autores:** 
- Alejandro Campos Martínez
- Agustín Jaime Navarro

**Team:** 6  
**Fecha de inicio:** 22/11/2025  
**Fecha de entrega:** 23/11/2025

---

## Introducción

Este proyecto representa un esfuerzo adicional al material estándar del curso de certificación en Inteligencia Artificial. Mientras que los laboratorios originales fueron diseñados para ejecutarse en Google Colab usando el simulador CUDA (CUDASIM) debido a limitaciones de compatibilidad, este trabajo extiende cada ejercicio para demostrar el rendimiento real en hardware NVIDIA.

El objetivo es proporcionar material educativo que beneficie a todos los estudiantes del curso, independientemente de su acceso a hardware especializado. Cada laboratorio se presenta en dos versiones:

1. **Versión Simulador:** Compatible con cualquier máquina, ejecutable en Colab o computadoras sin GPU NVIDIA
2. **Versión GPU Real:** Requiere GPU NVIDIA, demuestra aceleración real y speedups verdaderos

Esta documentación completa permite a los estudiantes comprender tanto los conceptos fundamentales de programación CUDA como el impacto real de la aceleración por GPU en aplicaciones prácticas.

---

## Contexto del Proyecto

### Motivación

Durante el desarrollo de los laboratorios en Google Colab, se encontraron múltiples problemas de compatibilidad entre versiones de Numba, CUDA Toolkit y drivers, que hicieron imposible la ejecución con GPU real en ese ambiente. El instructor proporcionó código adaptado para usar CUDASIM, permitiendo a los estudiantes aprender la sintaxis y estructura de CUDA sin necesidad de hardware especializado.

Al contar con acceso a una laptop con GPU NVIDIA RTX 4060, identifiqué la oportunidad de crear material complementario que demuestre el rendimiento real de CUDA, proporcionando un recurso valioso tanto para el instructor como para compañeros del curso que posteriormente puedan acceder a hardware GPU.

### Alcance

Este proyecto cubre tres laboratorios (ECU1, ECU2, ECU3) con un total de 7 ejercicios diferentes, cada uno implementado en ambas versiones. Se documentan exhaustivamente todos los errores encontrados, soluciones aplicadas, resultados obtenidos y análisis comparativos.

---

## Especificaciones de Hardware

### Ambiente Simulador

**Computadora de Escritorio:**
- **Procesador:** AMD Ryzen 7 5700G
  - 8 cores / 16 threads
  - Frecuencia base: 3.8 GHz
  - Boost: hasta 4.6 GHz
- **GPU:** AMD Radeon Vega (integrada) - No compatible con CUDA
- **Memoria:**
  - 32 Gb
- **Sistema Operativo:** Ubuntu 22.04 LTS

**Propósito:** Verificación de lógica, aprendizaje de sintaxis CUDA

### Ambiente GPU Real

**Laptop:**
- **GPU:** NVIDIA GeForce RTX 4060 Laptop GPU
  - Arquitectura: Ada Lovelace
  - Compute Capability: 8.9
  - Multiprocessors (SMs): 24
  - CUDA Cores: 3072
  - Memoria: 8 GB GDDR6
- **Sistema Operativo:** Ubuntu 22.04 LTS
- **CUDA Toolkit:** 12.6
- **Drivers NVIDIA:** 570.195.03

**Propósito:** Demostración de aceleración real, medición de speedups verdaderos

---

## Configuración del Entorno

Para detalles completos sobre la instalación y configuración de CUDA Toolkit, drivers NVIDIA, y resolución de problemas durante el setup inicial del ambiente de desarrollo, consultar:

**[Informe_Configuracion_Entorno_CUDA.md](Informe_Configuracion_Entorno_CUDA.md)**

Este documento complementario cubre:
- Proceso de instalación de CUDA Toolkit en Ubuntu 22.04
- Configuración de drivers NVIDIA
- Resolución de conflictos de versiones
- Verificación de instalación correcta
- Troubleshooting de problemas comunes durante setup

---

## Estructura del Proyecto
```
CUDA/
├── ECU1_Transferencia_Memoria
│   ├── ecu1_gpu_real.ipynb
│   ├── ecu1_gpu_real.py
│   ├── ecu_1_simulador.ipynb
│   ├── ecu_1_simulador.py
│   └── README.md
├── ECU2_Debug_Indexacion
│   ├── ecu2_gpu_real.ipynb
│   ├── ecu2_gpu_real.py
│   ├── ecu2_simulador.ipynb
│   ├── ecu2_simulador.py
│   └── README.md
├── ECU3_Operaciones_Avanzadas
│   ├── 3_1
│   │   ├── ecu3_1_vector_add_gpu_real.ipynb
│   │   ├── ecu3_1_vector_add_gpu_real.py
│   │   ├── ecu3_1_vector_add_simulador.ipynb
│   │   └── ecu3_1_vector_add_simulador.py
│   ├── 3_2
│   │   ├── ecu3_2_dummy_compute_gpu_real.ipynb
│   │   ├── ecu3_2_dummy_compute_gpu_real.py
│   │   ├── ecu3_2_dummy_compute_simulador.ipynb
│   │   └── ecu3_2_dummy_compute_simulador.py
│   ├── 3_3
│   │   ├── ecu3_3_matrix_scale_gpu_real.ipynb
│   │   ├── ecu3_3_matrix_scale_gpu_real.py
│   │   ├── ecu3_3_matrix_scale_simulador.ipynb
│   │   └── ecu3_3_matrix_scale_simulador.py
│   ├── 3_4
│   │   ├── ecu3_4_matmul_gpu_real.ipynb
│   │   ├── ecu3_4_matmul_gpu_real.py
│   │   ├── ecu3_4_matmul_simulador.ipynb
│   │   └── ecu3_4_matmul_simulador.py
│   ├── 3_5
│   │   ├── ecu3_5_sobel_gpu_real.py.ipynb
│   │   └── ecu3_5_sobel_simulador.ipynb
│   └── README.md
├── Informe_Configuracion_Entorno_CUDA.md
├── README.md
└── resultados
    ├── sobel_comparison_gpu_real.png
    └── sobel_comparison_simulador.png

```

---

## Resumen de Laboratorios

### ECU1: Transferencia de Memoria CPU-GPU

**Descripción:** Kernel básico de copia de datos que demuestra la estructura fundamental de un programa CUDA.

**Conceptos clave:**
- Inicialización y transferencia de datos
- Configuración de grid/bloques
- Sincronización GPU
- Medición de tiempos

**Resultados destacados:**
- GPU Real: 0.41 ms (kernel), Speedup: 11.15x
- Simulador: ~30 minutos

**Documentación completa:** README.md

---

### ECU2: Debug de Indexación de Threads y Bloques

**Descripción:** Kernel educativo para entender cálculo de IDs globales en grid 2D.

**Conceptos clave:**
- Jerarquía de threads/bloques
- Cálculo de índices globales
- Limitaciones de print() en GPU real
- Técnicas alternativas de debugging

**Resultados destacados:**
- 16 threads en configuración 2x2 bloques, 4x1 threads
- Warning de low occupancy (esperado y documentado)

**Documentación completa:** README.md

---

### ECU3: Operaciones Avanzadas

**Descripción:** Cinco ejercicios de complejidad creciente cubriendo desde operaciones vectoriales hasta procesamiento de imágenes.

**Ejercicios:**
1. Vector Addition (10M elementos)
2. Dummy Compute - Hipotenusa (10M elementos)
3. Matrix Scale (16.7M elementos)
4. Matrix Multiply Naive (1B operaciones)
5. Sobel Edge Detection (8.3M pixels)

**Resultados destacados:**
- Mejor speedup: 36.11x (Dummy Compute)
- Caso educativo: Matrix Multiply naive 5x más lento que CPU
- Aplicación práctica: Sobel 4.3x speedup

**Documentación completa:** README.md

---

## Resultados Consolidados

### Tabla Comparativa General

| Lab | Ejercicio | Elementos | Simulador (Ryzen) | GPU Real (RTX 4060) | Speedup GPU vs CPU | Factor GPU/Simulador |
|-----|-----------|-----------|-------------------|---------------------|---------------------|----------------------|
| ECU1 | Transferencia Memoria | 10M | ~1,800,000 ms | 0.41 ms | 11.15x | ~4,390,000x |
| ECU2 | Debug Indexación | 16 | N/A | <1 ms | N/A | N/A |
| ECU3.1 | Vector Add | 10M | 641,548 ms | 0.633 ms | 11.46x | ~1,013,000x |
| ECU3.2 | Dummy Compute | 10M | 740,562 ms | 0.639 ms | 36.11x | ~1,159,000x |
| ECU3.3 | Matrix Scale | 16.7M | 1,468,882 ms | 0.883 ms | 11.62x | ~1,664,000x |
| ECU3.4 | Matrix Multiply | 1M (1B ops) | 1,068,408 ms | 23.889 ms | 0.20x (CPU gana) | ~44,700x |
| ECU3.5 | Sobel Filter | 8.3M | 629,742 ms | 6.08 ms | 4.3x | ~103,500x |

### Gráfica de Speedups (GPU Real vs CPU)
```
Speedup GPU Real vs CPU:
────────────────────────────────────────────────────────
ECU1 Transferencia  ███████████ 11.15x
ECU3.1 Vector Add   ███████████ 11.46x
ECU3.2 Dummy Comp.  ████████████████████████████████████ 36.11x
ECU3.3 Matrix Scale ████████████ 11.62x
ECU3.4 MatMul Naive ██ 0.20x (CPU más rápido)
ECU3.5 Sobel Filter ████ 4.3x
```

### Patrones Observados

**Operaciones Bandwidth-Limited (11-12x speedup):**
- ECU1, ECU3.1, ECU3.3
- Limitadas por velocidad de memoria
- Operaciones simples

**Operaciones Compute-Intensive (30-40x speedup):**
- ECU3.2
- Beneficiadas por SFUs de GPU
- Operaciones matemáticas complejas

**Operaciones Mal Optimizadas (slowdown):**
- ECU3.4
- Accesos no coalescidos
- Sin shared memory
- CPU con BLAS optimizado gana

**Aplicaciones Prácticas (4-5x speedup):**
- ECU3.5
- Competencia con código CPU altamente optimizado
- Speedup modesto pero valioso en escala

---

## Errores Encontrados y Soluciones

### Error 1: CUDA_ERROR_UNSUPPORTED_PTX_VERSION (Colab)

**Contexto:** Durante ejecución en Google Colab

**Descripción:**
```
LinkerError: [222] Call to cuLinkAddData results in CUDA_ERROR_UNSUPPORTED_PTX_VERSION
ptxas application ptx input, line 9; fatal : Unsupported .version 8.5; current version is '8.4'
```

**Causa:**
Incompatibilidad entre versión de PTX generada por Numba (8.5) y la soportada por drivers CUDA de Colab (8.4).

**Intentos de solución:**
1. Forzar compute capability: `os.environ['NUMBA_CUDA_DEFAULT_PTX_CC'] = '(7, 5)'` - No funcionó
2. Downgrade a numba 0.59.1, 0.59.0, 0.58.1 - Conflictos de dependencias
3. Reinstalación múltiples versiones de llvmlite - Persistió el error

**Solución final:**
- En Google Colab: Usar CUDASIM (simulador)
- En máquina local con GPU NVIDIA: Usar GPU real con ambiente conda aislado

**Lección aprendida:** Google Colab tiene limitaciones con versiones recientes de CUDA/Numba. Ambientes locales ofrecen mejor control sobre dependencias.

---

### Error 2: AttributeError - total_memory

**Contexto:** Al intentar mostrar información de GPU

**Descripción:**
```python
AttributeError: total_memory
```

**Código problemático:**
```python
print(f"Memoria total: {gpu.total_memory / 1e9:.2f} GB")
```

**Causa:**
El atributo `total_memory` no existe en el objeto Device de Numba en versiones recientes.

**Solución aplicada:**
Omitir información de memoria o usar contexto CUDA:
```python
gpu = cuda.get_current_device()
print(f"GPU detectada: {gpu.name}")
print(f"Compute Capability: {gpu.compute_capability}")
print(f"Multiprocessors: {gpu.MULTIPROCESSOR_COUNT}")
```

**Alternativa con contexto:**
```python
meminfo = cuda.current_context().get_memory_info()
print(f"Memoria total: {meminfo.total / 1e9:.2f} GB")
```

---

### Error 3: ModuleNotFoundError

**Contexto:** Ejecutar scripts desde terminal en sistema base

**Descripción:**
```
ModuleNotFoundError: No module named 'numba'
```

**Causa:**
Intentar ejecutar con Python del sistema en lugar del ambiente conda donde están instaladas las dependencias.

**Solución:**
```bash
conda activate cuda_curso
python script.py
```

**Alternativa:** Usar Jupyter Notebook con kernel del ambiente conda apropiado.

---

### Warning: NumbaPerformanceWarning - Low Occupancy (ECU2)

**Contexto:** Ejecución de ECU2 en RTX 4060

**Descripción:**
```
NumbaPerformanceWarning: Grid size 4 will likely result in GPU under-utilization 
due to low occupancy.
```

**Análisis:**
La configuración de ECU2 (4 bloques, 16 threads) utiliza solo ~17% de la GPU (4 de 24 SMs activos). Esto es intencional para propósitos educativos, permitiendo visualizar y verificar manualmente cada thread.

**Observaciones:**
- La baja ocupación es resultado de mantener la configuración original del laboratorio
- En aplicaciones de producción se usarían configuraciones con cientos o miles de bloques
- Para este ejercicio específico, la configuración pequeña facilita la verificación manual

**No requiere corrección:** Es un comportamiento esperado y documentado como parte del proceso de aprendizaje.

---

### Error 4: PIL Image Loading (ECU3.5)

**Contexto:** Descarga y apertura de imagen en ECU3.5 Sobel

**Descripción:**
```python
AttributeError: _im
```

**Diagnóstico:**
La imagen se descarga correctamente (verificado con prueba aislada), pero podía haber archivo corrupto de ejecuciones anteriores.

**Solución:**
Limpiar archivo antes de descargar:
```python
import os
if os.path.exists("image.jpg"):
    os.remove("image.jpg")
    
urllib.request.urlretrieve("https://picsum.photos/3840/2160", "image.jpg")
img = Image.open("image.jpg").convert('L')
```

**Alternativa implementada:** Código con manejo robusto de errores que crea imagen sintética si falla la descarga.

---

## Instalación y Configuración

### Requisitos Previos

**Para versiones simulador:**
- Python 3.11+
- No requiere GPU NVIDIA

**Para versiones GPU real:**
- GPU NVIDIA (cualquier generación con soporte CUDA)
- Drivers NVIDIA instalados
- CUDA Toolkit compatible

### Instalación de Ambiente Conda
```bash
# Crear ambiente
conda create -n cuda_curso python=3.11

# Activar ambiente
conda activate cuda_curso

# Instalar dependencias básicas
conda install numba numpy

# Instalar dependencias adicionales (para ECU3.5)
conda install opencv pillow matplotlib

# Verificar instalación
python -c "import numba; print(f'Numba: {numba.__version__}')"
python -c "from numba import cuda; print(f'CUDA available: {cuda.is_available()}')"
```

### Verificación de GPU
```bash
# Verificar drivers NVIDIA
nvidia-smi

# Verificar CUDA toolkit
nvcc --version

# Verificar en Python
python -c "from numba import cuda; print(cuda.get_current_device().name)"
```

---

## Ejecución de Laboratorios

### Ejecución Individual
```bash
# Activar ambiente
conda activate cuda_curso

# ECU1
python ECU1_Transferencia_Memoria/ecu1_gpu_real.py

# ECU2
python ECU2_Debug_Indexacion/ecu2_gpu_real.py

# ECU3 (ejecutar cada ejercicio)
python ECU3_Operaciones_Avanzadas/ecu3_1_vector_add_gpu_real.py
python ECU3_Operaciones_Avanzadas/ecu3_2_dummy_compute_gpu_real.py
python ECU3_Operaciones_Avanzadas/ecu3_3_matrix_scale_gpu_real.py
python ECU3_Operaciones_Avanzadas/ecu3_4_matmul_gpu_real.py
python ECU3_Operaciones_Avanzadas/ecu3_5_sobel_gpu_real.py
```

### Ejecución desde Jupyter Notebook
```bash
# Iniciar Jupyter con ambiente activado
conda activate cuda_curso
jupyter notebook

# Abrir notebooks correspondientes y ejecutar
```

### Tiempos Estimados de Ejecución

**GPU Real (RTX 4060):**
- ECU1: <1 segundo
- ECU2: <1 segundo
- ECU3.1-3.3: <1 segundo cada uno
- ECU3.4: ~1 segundo
- ECU3.5: ~1 segundo (incluyendo descarga de imagen)

**Simulador (AMD Ryzen 7 5700G):**
- ECU1: ~30 minutos
- ECU2: Variable según configuración
- ECU3.1: ~11 minutos
- ECU3.2: ~12 minutos
- ECU3.3: ~25 minutos
- ECU3.4: ~18 minutos
- ECU3.5: ~11 minutos

---

## Conceptos Clave de CUDA

### 1. Jerarquía de Ejecución
```
Grid (Malla completa en GPU)
 └── Blocks (Grupos de threads que se ejecutan en un SM)
      └── Threads (Unidad mínima de ejecución)
```

**Dimensiones:**
- Grids pueden ser 1D, 2D o 3D
- Blocks pueden ser 1D, 2D o 3D
- Configuración típica: bloques de 256 threads (potencia de 2)

### 2. Modelo de Memoria

**Global Memory:**
- Accesible por todos los threads
- Alta latencia (~400-600 ciclos)
- Gran capacidad (GB)

**Shared Memory:**
- Compartida dentro de un bloque
- Baja latencia (~20 ciclos)
- Capacidad limitada (48-96 KB por SM)

**Registers:**
- Privados a cada thread
- Latencia mínima (1 ciclo)
- Cantidad limitada (~255 registros por thread)

### 3. Patrones de Acceso

**Coalesced Access (Óptimo):**
```
Threads consecutivos acceden direcciones consecutivas
Thread 0 → addr[0]
Thread 1 → addr[1]
Thread 2 → addr[2]
...
```

**Non-Coalesced Access (Ineficiente):**
```
Threads consecutivos acceden direcciones dispersas
Thread 0 → addr[0]
Thread 1 → addr[1000]
Thread 2 → addr[2000]
...
```

### 4. Sincronización

**Within Block:**
```python
cuda.syncthreads()  # Barrera dentro del bloque
```

**Across Grid:**
```python
cuda.synchronize()  # Espera a que todos los threads terminen
```

### 5. Tipos de Kernels

**Element-wise Operations:**
- Un thread por elemento
- Altamente paralelizable
- Ejemplo: Vector addition

**Reduction Operations:**
- Múltiples threads colaboran
- Requiere sincronización
- Ejemplo: Sum, Max, Min

**Stencil Operations:**
- Cada thread usa vecinos
- Común en imágenes/matrices
- Ejemplo: Sobel, Convolución

---

## Lecciones Aprendidas

### Sobre Compatibilidad de Software

La configuración de ambientes CUDA puede ser compleja debido a múltiples capas de dependencias. Google Colab, aunque conveniente, tiene limitaciones con versiones recientes de herramientas. Ambientes locales con conda proporcionan mejor control pero requieren más configuración inicial. La inversión en tiempo para establecer un ambiente estable paga dividendos en productividad a largo plazo.

### Sobre el Simulador CUDA

El simulador CUDASIM es invaluable para aprendizaje y verificación de lógica, pero no debe usarse nunca para medir rendimiento. Los tiempos de ejecución en simulador son millones de veces más lentos que GPU real, haciendo imposible cualquier análisis de performance. Sin embargo, el simulador permite que estudiantes sin acceso a hardware GPU comprendan completamente la sintaxis y estructura de programación CUDA, democratizando el acceso al conocimiento.

### Sobre Optimización de GPU

El resultado de ECU3.4 (Matrix Multiply naive) enseña una lección fundamental que todo programador de GPU debe internalizar: mover código a GPU no garantiza aceleración. Las GPUs son herramientas poderosas pero complejas que requieren algoritmos específicamente diseñados para su arquitectura. Accesos coalescidos a memoria, uso de shared memory, tiling, y otras optimizaciones no son opcionales sino necesarias para obtener buen rendimiento. Una GPU mal utilizada puede ser varios órdenes de magnitud más lenta que CPU bien optimizada.

### Sobre Diferentes Tipos de Operaciones

Las operaciones se comportan muy diferente en GPU dependiendo de si son bandwidth-limited o compute-intensive. Operaciones simples como copias y sumas muestran speedups modestos (10-15x) porque están limitadas por velocidad de memoria, no por capacidad de cómputo. En contraste, operaciones con alta intensidad aritmética como el cálculo de hipotenusa pueden alcanzar speedups de 30-40x porque aprovechan las unidades de funciones especiales de la GPU. Entender esta distinción es crucial para predecir qué código se beneficiará de aceleración GPU.

### Sobre Herramientas de Alto Nivel

Los resultados de Sobel muestran que librerías como OpenCV están extraordinariamente bien optimizadas. Incluso con GPU, el speedup es modesto (4.3x) porque la versión CPU ya está usando instrucciones SIMD, cache blocking, y otras optimizaciones avanzadas. Esto no diminuye el valor de GPU sino que resalta la importancia de usar librerías maduras cuando están disponibles. En producción, es mejor usar cuBLAS, cuDNN y otras librerías NVIDIA optimizadas que escribir kernels propios excepto para casos muy específicos.

### Sobre Escalabilidad

Una observación consistente a través de todos los ejercicios es que las GPUs escalan excepcionalmente bien con el tamaño de datos. ECU3.3 con 67% más elementos que ECU3.1 solo tomó 40% más tiempo. Esta escalabilidad es lo que hace a las GPUs ideales para deep learning moderno donde modelos pueden tener billones de parámetros. El paralelismo masivo compensa overhead de lanzamiento de kernel y transferencias de memoria cuando los datasets son suficientemente grandes.

---

## Conclusiones Generales

Este proyecto ha documentado exhaustivamente el proceso de implementar y ejecutar programas CUDA en dos ambientes completamente diferentes: simulador en CPU y GPU real. La experiencia proporciona perspectiva única sobre las capacidades, limitaciones y mejores prácticas de programación GPU.

Los tres laboratorios cubrieron progresivamente conceptos desde transferencias básicas de memoria hasta aplicaciones prácticas de procesamiento de imágenes. Cada ejercicio aportó lecciones específicas pero todos compartieron temas comunes: la importancia de entender la arquitectura de memoria, la necesidad de optimizaciones apropiadas, y el poder transformador del paralelismo masivo cuando se aplica correctamente.

La comparación directa entre simulador y GPU real revela diferencias de varios órdenes de magnitud en rendimiento. El simulador, tomando típicamente 10-30 minutos por ejercicio, ejecuta secuencialmente lo que la GPU procesa en milisegundos usando paralelismo masivo. Esta diferencia dramática no solo demuestra el poder de las GPUs sino que también subraya por qué se han vuelto indispensables para inteligencia artificial moderna, simulaciones científicas y procesamiento de grandes volúmenes de datos.

El material generado cumple su propósito dual de servir como recurso educativo para compañeros sin GPU NVIDIA mientras demuestra rendimiento real para aquellos con acceso a hardware. La documentación detallada de errores, soluciones y análisis de resultados proporciona valor adicional más allá de simplemente mostrar código funcionando.

Para el curso de certificación en IA, estos ejercicios establecen fundamentos esenciales. Las operaciones exploradas (multiplicación matricial, convoluciones, operaciones elemento-wise) son exactamente las que dominan el tiempo de ejecución en redes neuronales. Entender cómo estas operaciones se mapean a hardware GPU y qué factores afectan su rendimiento es conocimiento fundamental para cualquier persona trabajando en machine learning moderno.

El ejercicio más valioso educativamente resultó ser el que mostró rendimiento negativo. La multiplicación de matrices naive siendo 5 veces más lenta que CPU enseña humildad y respeto por la complejidad de optimización de GPU. Este resultado negativo es un recordatorio que el hardware por sí solo no es suficiente, el software debe estar cuidadosamente diseñado para aprovechar las características únicas de la arquitectura paralela.

Mirando hacia el futuro del curso, estos fundamentos preparan el terreno para trabajo más avanzado con frameworks de deep learning. PyTorch y TensorFlow abstraen muchos detalles de implementación CUDA, pero entender qué sucede bajo el capó permite tomar mejores decisiones de arquitectura, identificar cuellos de botella de rendimiento, y apreciar el trabajo de ingeniería que hace posible entrenar modelos masivos en tiempos razonables.

---

### Documentación Oficial

- **NVIDIA CUDA Programming Guide:** https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- **Numba CUDA Documentation:** https://numba.readthedocs.io/en/stable/cuda/
- **CUDA Best Practices Guide:** https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/

---

## Contacto y Contribuciones

Este material fue desarrollado como parte del curso de certificación TAE en IA 2025. Está disponible para uso educativo por compañeros del curso y futuros estudiantes.

**Autores:** 
- Alejandro Campos Martínez
- Agustín Jaime Navarro

**Institución:**
- Universidad Autónoma de Nayarit
- Universidad Tecnológica de Nayarit
**Team:** 6  

Para preguntas, sugerencias o correcciones, por favor contactar a los autores o instructor del curso.

---

## Anexos

### A. Configuración Completa del Ambiente
```bash
# Crear ambiente desde cero
conda create -n cuda_curso python=3.11 -y
conda activate cuda_curso

# Instalar dependencias
conda install -c conda-forge numba numpy opencv pillow matplotlib -y

# Verificar instalación
python -c "import numba; from numba import cuda; import cv2; import PIL; import matplotlib; print('All imports successful')"

# Verificar GPU
python -c "from numba import cuda; print(f'CUDA available: {cuda.is_available()}'); print(f'GPU: {cuda.get_current_device().name if cuda.is_available() else 'N/A'}')"
```

### B. Script de Verificación Rápida
```python
"""
quick_check.py - Verificación rápida de ambiente CUDA
"""
from numba import cuda
import numpy as np

@cuda.jit
def test_kernel(x, y):
    idx = cuda.grid(1)
    if idx < x.size:
        y[idx] = x[idx] * 2

def main():
    print("Verificando ambiente CUDA...")
    
    if not cuda.is_available():
        print("CUDA NO disponible - usar simulador")
        return
    
    gpu = cuda.get_current_device()
    print(f"GPU: {gpu.name}")
    print(f"Compute Capability: {gpu.compute_capability}")
    
    # Test rápido
    x = np.arange(1000, dtype=np.float32)
    y = np.zeros_like(x)
    
    d_x = cuda.to_device(x)
    d_y = cuda.to_device(y)
    
    test_kernel[4, 256](d_x, d_y)
    cuda.synchronize()
    
    result = d_y.copy_to_host()
    
    if np.allclose(result, x * 2):
        print("Test PASSED - Ambiente funcionando correctamente")
    else:
        print("Test FAILED - Revisar configuración")

if __name__ == "__main__":
    main()
```

### C. Troubleshooting Común

**Problema:** `ImportError: cannot import name 'cuda'`  
**Solución:** Reinstalar numba: `conda install -c conda-forge numba --force-reinstall`

**Problema:** GPU no detectada  
**Solución:** Verificar drivers: `nvidia-smi`, reinstalar si es necesario

**Problema:** Out of memory  
**Solución:** Reducir tamaño de datos o liberar memoria: `cuda.close()`

---

**Versión del Documento:** 1.0  
**Última Actualización:** 23/11/2025  
**Palabra Clave:** CUDA, GPU Computing, Deep Learning, Numba, Python

---

**FIN DEL DOCUMENTO**
