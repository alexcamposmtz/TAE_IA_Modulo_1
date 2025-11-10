# Lab 9: NumPy I - II

**Curso:** Talento Altamente Especializado – Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Cristian Torres González  
**Equipo:** Team 6
- Alejandro Campos Martínez

**Fecha de asignación:** 31/10/2025  
**Fecha de entrega:** 10/11/2025

---

## Descripción del Laboratorio

Este laboratorio introduce el uso de **NumPy** para computación científica y manipulación de arrays, incluyendo:
- Creación y manipulación de arrays
- Indexación y slicing avanzado
- Operaciones con matrices especiales
- Operaciones estadísticas y matemáticas
- Guardar y cargar arrays
- Detección y corrección de errores comunes con NumPy

---

## Estructura del Laboratorio

```
Lab_9/
├── README.md
├── Section_1/
│   ├── task_1.py    # Operaciones Básicas con Arrays
│   ├── task_2.py    # Matrices Especiales
│   ├── task_3.py    # Arrays y Estadísticas
│   └── task_4.py    # Guardar y Cargar Arrays
└── Section_2/
    ├── task_5.py    # IndexError
    ├── task_6.py    # ValueError (reshape)
    ├── task_7.py    # TypeError
    └── task_8.py    # AttributeError
```

---

## Sección 1: Práctica de Programación

### Task 1: Operaciones Básicas con Arrays
Creación y manipulación de un array con números del 1 al 20.

**Operaciones realizadas:**
- Obtener elementos en índices pares (posiciones 0, 2, 4, ...)
- Calcular la suma de todos los valores impares
- Reemplazar todos los múltiplos de 3 con -1
- Imprimir array resultante

**Características:**
- Uso de `np.arange()` para crear arrays
- Indexación con slicing: `arr[::2]` (paso 2)
- Indexación condicional: `arr[arr % 2 != 0]`
- Máscaras booleanas para filtrado
- Operaciones de modificación in-place

**Ejecución:**
```bash
python3 Section_1/task_1.py
```

**Ejemplo de salida:**
```
Array Original:
A = [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

Elementos en índices pares: [ 1  3  5  7  9 11 13 15 17 19]
Suma de valores impares: 100
Array modificado: [ 1  2 -1  4  5 -1  7  8 -1 10 11 -1 13 14 -1 16 17 -1 19 20]
```

**Conceptos demostrados:**
- **Slicing:** Acceso a subsecuencias con `[start:stop:step]`
- **Indexación condicional:** Selección basada en condiciones booleanas
- **Operaciones elemento por elemento:** Aplicar condiciones a todo el array
- **np.sum():** Suma de elementos en un array

---

### Task 2: Matrices Especiales y Operaciones Básicas
Creación de matrices especiales y operaciones aritméticas.

**Matrices creadas:**
- M1: Matriz 4×4 de unos (`np.ones`)
- M2: Matriz 4×4 llena de 5s (`np.full`)
- I: Matriz identidad 4×4 (`np.eye`)

**Operaciones realizadas:**
- S = M1 + M2 - I
- P = M2 * I (multiplicación elemento por elemento)

**Ejecución:**
```bash
python3 Section_1/task_2.py
```

**Ejemplo de salida:**
```
M1 (Matriz de unos):
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]

S = M1 + M2 - I:
[[5. 6. 6. 6.]
 [6. 5. 6. 6.]
 [6. 6. 5. 6.]
 [6. 6. 6. 5.]]
```

**Conceptos demostrados:**
- **Matrices especiales:** `np.ones()`, `np.full()`, `np.eye()`
- **Operaciones aritméticas:** Suma, resta elemento por elemento
- **Multiplicación Hadamard:** `*` para elemento por elemento
- **Verificación:** Análisis de resultados y patrones

---

### Task 3: Arrays y Operaciones Estadísticas
Generación de arrays y cálculos estadísticos.

**Arrays generados:**
- x: 15 valores equiespaciados entre 0 y 10 (`np.linspace`)
- r: 15 enteros aleatorios entre 0 y 100 (`np.random.randint`)

**Cálculos realizados:**
- Elementos de r mayores que la media de r
- Suma de elementos en x menores que 5
- Valor máximo de r y su posición (índice)

**Ejecución:**
```bash
python3 Section_1/task_3.py
```

**Conceptos demostrados:**
- **np.linspace():** Valores equiespaciados
- **np.random.randint():** Generación de números aleatorios
- **Estadísticas:** `np.mean()`, `np.median()`, `np.std()`
- **np.where():** Encontrar índices que cumplen condición
- **np.argmax():** Índice del valor máximo

---

### Task 4: Guardar y Cargar Matrices
Persistencia de arrays usando archivos .npy.

**Operaciones realizadas:**
- Generar matriz 3×3 con enteros aleatorios de 1 a 9
- Guardar en "matrix_original.npy"
- Cargar el archivo en variable B
- Elevar al cuadrado todos los elementos
- Guardar como "matrix_squared.npy"
- Verificar que ningún elemento coincide (excepto el 1)

**Ejecución:**
```bash
python3 Section_1/task_4.py
```

**Ejemplo de salida:**
```
Matriz Original:
[[7 4 8]
 [5 7 4]
 [2 7 7]]

Matriz al Cuadrado:
[[49 16 64]
 [25 49 16]
 [ 4 49 49]]

Ningún elemento coincide ✓
```

**Conceptos demostrados:**
- **np.save():** Guardar arrays en formato binario
- **np.load():** Cargar arrays desde archivos .npy
- **Operaciones potencia:** `arr ** 2` para elevar al cuadrado
- **Comparación booleana:** `arr1 == arr2` elemento por elemento

---

## Sección 2: Detección de Errores

Esta sección documenta **cuatro tipos de errores** encontrados durante la práctica con NumPy.

### Task 5: IndexError
**Error:** Intentar acceder a un índice que está fuera del rango del array.

```python
arr = np.arange(10)  # Array de 10 elementos (índices 0-9)
value = arr[10]       # Error: índice 10 no existe
```

**Mensaje de error:**
```
IndexError: index 10 is out of bounds for axis 0 with size 10
```

**Causa:** Los arrays de tamaño N tienen índices válidos de 0 a N-1. Intentar acceder al índice N o mayor causa IndexError.

**Soluciones:**
1. Verificar tamaño con `len(arr)` antes de acceder
2. Usar índices válidos (0 hasta `len(arr)-1`)
3. Usar índices negativos (-1 para último elemento)
4. Usar slicing (no genera error, retorna array vacío)

**Ejecución:**
```bash
python3 Section_2/task_5.py
```

---

### Task 6: ValueError (Reshape)
**Error:** Intentar hacer reshape a dimensiones incompatibles.

```python
arr = np.arange(12)    # 12 elementos
reshaped = arr.reshape(4, 4)  # Error: 4×4 = 16 ≠ 12
```

**Mensaje de error:**
```
ValueError: cannot reshape array of size 12 into shape (4,4)
```

**Causa:** El número total de elementos debe ser igual al producto de las nuevas dimensiones. 12 elementos no caben en una matriz 4×4 (que requiere 16 elementos).

**Soluciones:**
1. Usar dimensiones compatibles: `reshape(3, 4)` → 3×4 = 12 ✓
2. Calcular dimensión automáticamente: `reshape(3, -1)` o `reshape(-1, 4)`
3. Usar `np.resize()` para cambiar tamaño (rellena si es necesario)
4. Ajustar el número de elementos antes de reshape

**Ejecución:**
```bash
python3 Section_2/task_6.py
```

---

### Task 7: TypeError
**Error:** Operaciones con tipos de datos incompatibles.

```python
arr = np.array([1, 2, 3])
result = arr + "texto"  # Error: no se puede sumar array con string
```

**Mensaje de error:**
```
TypeError: unsupported operand type(s) for +: 'numpy.ndarray' and 'str'
```

**Causa:** Intentar realizar operaciones matemáticas entre arrays numéricos y tipos no numéricos (strings, None, etc.).

**Soluciones:**
1. Convertir todos los operandos a arrays con `np.array()`
2. Verificar tipos con `isinstance()` y `np.issubdtype()`
3. Usar validación de tipos en funciones
4. Especificar dtype correcto al crear arrays

**Ejecución:**
```bash
python3 Section_2/task_7.py
```

---

### Task 8: AttributeError
**Error:** Intentar usar métodos que no existen en arrays de NumPy.

```python
arr = np.array([1, 2, 3])
arr.append(4)  # Error: arrays de NumPy no tienen método append()
```

**Mensaje de error:**
```
AttributeError: 'numpy.ndarray' object has no attribute 'append'
```

**Causa:** Los arrays de NumPy no son listas de Python. No tienen métodos como `append()`, `extend()`, `insert()`, etc.

**Diferencias clave:**
- **Listas Python:** Métodos `.append()`, `.extend()`, `.pop()`, etc.
- **Arrays NumPy:** Funciones `np.append()`, `np.concatenate()`, etc.

**Soluciones:**
1. Usar `np.append(arr, value)` (función, no método)
2. Usar `np.concatenate()` para unir arrays
3. Crear array con tamaño correcto desde el inicio
4. Usar listas si necesitas modificaciones dinámicas

**Ejecución:**
```bash
python3 Section_2/task_8.py
```

---

## Ejecución del Laboratorio

### Requisitos:
```bash
pip install numpy
```

### Ejecutar todas las tareas de la Sección 1:
```bash
cd Lab_9
python3 Section_1/task_1.py
python3 Section_1/task_2.py
python3 Section_1/task_3.py
python3 Section_1/task_4.py
```

### Ejecutar todas las tareas de la Sección 2:
```bash
python3 Section_2/task_5.py
python3 Section_2/task_6.py
python3 Section_2/task_7.py
python3 Section_2/task_8.py
```

---

## Conceptos Clave Aprendidos

### 1. Creación de Arrays
- **np.array():** Crear desde lista
- **np.arange():** Rango de valores (similar a `range()`)
- **np.linspace():** Valores equiespaciados
- **np.zeros():** Array de ceros
- **np.ones():** Array de unos
- **np.full():** Array con valor específico
- **np.eye():** Matriz identidad
- **np.random.randint():** Números aleatorios

### 2. Indexación y Slicing
- **Índice simple:** `arr[5]`
- **Índices negativos:** `arr[-1]` (último elemento)
- **Slicing:** `arr[start:stop:step]`
- **Índices pares:** `arr[::2]`
- **Indexación condicional:** `arr[arr > 5]`
- **Máscaras booleanas:** `arr[mask]`

### 3. Operaciones Matemáticas
- **Elemento por elemento:** `+`, `-`, `*`, `/`, `**`
- **Funciones universales:** `np.sin()`, `np.cos()`, `np.exp()`
- **Agregaciones:** `np.sum()`, `np.mean()`, `np.std()`
- **Comparaciones:** `arr > 5`, `arr == 3`

### 4. Operaciones Estadísticas
- **np.mean():** Media aritmética
- **np.median():** Mediana
- **np.std():** Desviación estándar
- **np.min():** Valor mínimo
- **np.max():** Valor máximo
- **np.argmin():** Índice del mínimo
- **np.argmax():** Índice del máximo

### 5. Manipulación de Forma
- **reshape():** Cambiar forma del array
- **transpose():** Transponer matriz
- **flatten():** Convertir a 1D
- **ravel():** Aplanar array (vista)

### 6. Persistencia
- **np.save():** Guardar array en formato .npy
- **np.load():** Cargar array desde .npy
- **np.savetxt():** Guardar en texto
- **np.loadtxt():** Cargar desde texto

---

## Errores Comunes con NumPy

1. **IndexError**
   - Verificar rango de índices
   - Usar `len(arr)` o `arr.shape`

2. **ValueError en reshape**
   - Producto de dimensiones debe igualar número de elementos
   - Usar -1 para calcular automáticamente

3. **TypeError en operaciones**
   - Asegurar tipos compatibles
   - Convertir con `np.array()` si es necesario

4. **AttributeError**
   - Arrays NO son listas
   - Usar funciones `np.*` en lugar de métodos

5. **Broadcasting incorrecto**
   - Verificar formas de arrays
   - Entender reglas de broadcasting

---

## Buenas Prácticas

**Creación de arrays:**
- Especificar dtype cuando sea necesario
- Pre-asignar arrays de tamaño conocido
- Usar funciones específicas (zeros, ones, etc.)

**Operaciones:**
- Aprovechar vectorización (evitar bucles)
- Usar operaciones elemento por elemento
- Aplicar máscaras booleanas para filtrado

**Memoria y rendimiento:**
- Usar vistas en lugar de copias cuando sea posible
- Evitar crear arrays temporales innecesarios
- Considerar dtype para optimizar memoria

**Depuración:**
- Verificar shapes: `arr.shape`
- Verificar tipos: `arr.dtype`
- Imprimir arrays pequeños para verificar

---

## Diferencias: Listas Python vs Arrays NumPy

| Característica | Listas Python | Arrays NumPy |
|---|---|---|
| Tamaño | Dinámico | Fijo |
| Tipos | Mixtos | Homogéneo |
| Operaciones | Limitadas | Vectorizadas |
| Velocidad | Lenta | Rápida |
| Memoria | Mayor overhead | Eficiente |
| Métodos append/extend | ✓ | ✗ |
| Operaciones matemáticas | Limitadas | Completas |

---

## Recursos Adicionales

- [Documentación oficial de NumPy](https://numpy.org/doc/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)
- Slides del curso: NumPy I y II

---

**Team 6**  
Noviembre 2025
