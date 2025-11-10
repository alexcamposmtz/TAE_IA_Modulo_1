# Lab 4: Modularización

**Curso:** Talento Altamente Especializado - Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Cristian Torres González  
**Fecha de asignación:** 20/10/2025  
**Fecha de entrega:** 26/10/2025
**Estudiante:** Alejandro Campos Martínez

---

## Introducción

Este laboratorio tiene como objetivo revisar y aplicar los conceptos de modularización en Python, incluyendo:
- Creación de funciones con parámetros por defecto
- Implementación de operaciones con matrices
- Organización de código en módulos
- Creación de paquetes de Python
- Detección y corrección de errores comunes

---

## Estructura del Proyecto

```
Lab4/
├── README.md
├── section_1/
│   ├── task_1.py                    # Funciones de áreas con parámetros por defecto
│   ├── task_2.py                    # Operaciones con matrices 4x4
│   ├── areas.py                     # Módulo de funciones de áreas
│   ├── matrices.py                  # Módulo de operaciones con matrices
│   ├── task_3.py                    # Script de prueba de módulos
│   ├── geometria_package/           # Paquete con módulos de geometría
│   │   ├── __init__.py
│   │   ├── areas.py
│   │   └── matrices.py
│   └── task_4.py                    # Script de prueba del paquete
└── section_2/
    ├── task_5.py                    # Ejemplo de SyntaxError
    ├── task_6.py                    # Ejemplo de TypeError
    ├── task_7.py                    # Ejemplo de IndexError
    └── task_8.py                    # Ejemplo de ImportError
```

---

## Sección 1: Práctica de Programación

### Task 1: Funciones de Áreas con Parámetros por Defecto

**Archivo:** `section_1/task_1.py`

Se implementaron cuatro funciones para calcular áreas geométricas:

1. **`area_circulo(radio=1.0)`**
   - Calcula el área de un círculo usando la fórmula: A = π × r²
   - Parámetro por defecto: radio = 1.0

2. **`area_cuadrado(lado=1.0)`**
   - Calcula el área de un cuadrado usando la fórmula: A = lado²
   - Parámetro por defecto: lado = 1.0

3. **`area_triangulo(base=1.0, altura=1.0)`**
   - Calcula el área de un triángulo usando la fórmula: A = (base × altura) / 2
   - Parámetros por defecto: base = 1.0, altura = 1.0

4. **`area_hexagono(lado=1.0)`**
   - Calcula el área de un hexágono regular usando la fórmula: A = (3√3/2) × lado²
   - Parámetro por defecto: lado = 1.0

**Características especiales:**
- Todas las funciones muestran un mensaje cuando se utilizan valores por defecto
- Incluye documentación detallada (docstrings)
- El script incluye pruebas con y sin argumentos

**Ejecución:**
```bash
python section_1/task_1.py
```

---

### Task 2: Operaciones con Matrices 4x4

**Archivo:** `section_1/task_2.py`

Se implementaron tres funciones para operaciones con matrices 4x4:

1. **`multiplicacion_matrices(matriz1, matriz2)`**
   - Realiza la multiplicación de dos matrices 4x4
   - Implementa el algoritmo estándar de multiplicación de matrices

2. **`suma_matrices(matriz1, matriz2)`**
   - Realiza la suma elemento por elemento de dos matrices 4x4

3. **`resta_matrices(matriz1, matriz2)`**
   - Realiza la resta elemento por elemento de dos matrices 4x4

4. **`imprimir_matriz(matriz, nombre="Matriz")`**
   - Función auxiliar para imprimir matrices de forma legible

**Características:**
- Maneja matrices representadas como listas de listas
- Formato de salida profesional y legible
- Incluye matrices de prueba predefinidas

**Ejecución:**
```bash
python section_1/task_2.py
```

---

### Task 3: Creación y Prueba de Módulos

**Archivos:**
- `section_1/areas.py` - Módulo con funciones de áreas
- `section_1/matrices.py` - Módulo con operaciones de matrices
- `section_1/task_3.py` - Script de prueba

Se organizó el código en módulos reutilizables:

**Módulo `areas.py`:**
- Contiene todas las funciones de cálculo de áreas
- Puede importarse en cualquier script que necesite cálculos geométricos

**Módulo `matrices.py`:**
- Contiene todas las funciones de operaciones con matrices
- Incluye función auxiliar para impresión

**Script `task_3.py`:**
- Importa ambos módulos
- Demuestra el uso de las funciones de ambos módulos
- Ejecuta pruebas completas

**Ejecución:**
```bash
python section_1/task_3.py
```

---

### Task 4: Creación de Paquete

**Directorio:** `section_1/geometria_package/`

Se creó un paquete completo que incluye:

**Estructura del paquete:**
```
geometria_package/
├── __init__.py      # Define el paquete y exporta funciones
├── areas.py         # Módulo de áreas
└── matrices.py      # Módulo de matrices
```

**Archivo `__init__.py`:**
- Importa todas las funciones de los módulos
- Define `__all__` para controlar las exportaciones
- Permite importar directamente desde el paquete

**Script `task_4.py`:**
- Importa funciones específicas del paquete
- Calcula el área de un hexágono
- Realiza multiplicación de matrices
- Demuestra el uso profesional de paquetes

**Ejecución:**
```bash
python section_1/task_4.py
```

---

## Sección 2: Detección de Errores

### Task 5: SyntaxError

**Archivo:** `section_2/task_5.py`

**Descripción del error:**
- Ocurre cuando el código no sigue las reglas de sintaxis de Python
- Se detecta antes de la ejecución del programa

**Ejemplo implementado:**
```python
# Error: Falta cerrar paréntesis
print("Hola, " + nombre
```

**Causas comunes:**
1. Paréntesis, corchetes o llaves sin cerrar
2. Olvidar dos puntos después de def, if, for, while
3. Usar = en lugar de == en comparaciones
4. Indentación incorrecta
5. Palabras reservadas como nombres de variables

**Solución:**
```python
# Correcto
print("Hola, " + nombre)
```

**Ejecución:**
```bash
python section_2/task_5.py
```

---

### Task 6: TypeError

**Archivo:** `section_2/task_6.py`

**Descripción del error:**
- Ocurre al intentar operaciones con tipos de datos incompatibles
- Común al mezclar strings y números sin conversión

**Ejemplo implementado:**
```python
# Error: Concatenar string con entero
edad = 25
mensaje = "Tengo " + edad + " años"
```

**Soluciones:**
1. Conversión explícita: `"Tengo " + str(edad) + " años"`
2. F-strings: `f"Tengo {edad} años"`
3. Format: `"Tengo {} años".format(edad)`

**Causas comunes:**
1. Concatenar tipos incompatibles
2. Número incorrecto de argumentos en funciones
3. Intentar sumar tipos incompatibles (str + list)
4. Usar índices en tipos no iterables

**Ejecución:**
```bash
python section_2/task_6.py
```

---

### Task 7: IndexError

**Archivo:** `section_2/task_7.py`

**Descripción del error:**
- Ocurre al intentar acceder a un índice inexistente en una secuencia
- Común al no verificar el tamaño de listas o arrays

**Ejemplo implementado:**
```python
# Error: Acceder a índice fuera de rango
numeros = [10, 20, 30, 40, 50]
elemento = numeros[5]  # Índices válidos: 0-4
```

**Soluciones:**
1. Verificación previa del tamaño
2. Uso de try-except
3. Usar índices válidos (0 a len-1)
4. Usar índices negativos correctamente

**Causas comunes:**
1. Acceder a índices fuera de rango
2. No considerar que los índices empiezan en 0
3. Confundir longitud con índice máximo
4. Modificar lista mientras se itera

**Ejecución:**
```bash
python section_2/task_7.py
```

---

### Task 8: ImportError / ModuleNotFoundError

**Archivo:** `section_2/task_8.py`

**Descripción del error:**
- Ocurre cuando Python no puede encontrar o importar un módulo
- ModuleNotFoundError es un subtipo específico (Python 3.6+)

**Ejemplo implementado:**
```python
# Error: Módulo inexistente
import matematicas_avanzadas

# Error: Función mal escrita
from math import raiz_cuadrada  # Correcto: sqrt
```

**Soluciones:**
1. Verificar ortografía del módulo
2. Instalar módulos faltantes: `pip install nombre_modulo`
3. Verificar que el módulo esté en el PATH
4. Usar try-except para importaciones opcionales

**Causas comunes:**
1. Módulo no instalado
2. Error de ortografía en el nombre
3. Módulo no está en el PATH de Python
4. Importar desde paquete sin `__init__.py`
5. Nombre de función incorrecta

**Ejecución:**
```bash
python section_2/task_8.py
```

---

## Cómo Ejecutar el Laboratorio

### Prerrequisitos
- Python 3.6 o superior
- No se requieren paquetes externos

### Ejecución Individual

Para ejecutar cada tarea individualmente:

```bash
# Sección 1
python section_1/task_1.py
python section_1/task_2.py
python section_1/task_3.py
python section_1/task_4.py

# Sección 2
python section_2/task_5.py
python section_2/task_6.py
python section_2/task_7.py
python section_2/task_8.py
```

### Notas Importantes

1. **Para task_3.py:** Asegúrese de que los módulos `areas.py` y `matrices.py` estén en el mismo directorio.

2. **Para task_4.py:** El paquete `geometria_package` debe estar en el mismo directorio del script.

3. **Estructura de directorios:** Mantenga la estructura de carpetas como se indica para evitar errores de importación.

---

## Conceptos Clave Aprendidos

### 1. Funciones con Parámetros por Defecto
- Permiten llamar funciones sin todos los argumentos
- Mejoran la flexibilidad del código
- Útiles para valores comunes o típicos

### 2. Módulos
- Organizan código relacionado
- Facilitan la reutilización
- Mejoran el mantenimiento
- Pueden importarse completos o parcialmente

### 3. Paquetes
- Colección organizada de módulos
- Requieren archivo `__init__.py`
- Permiten estructura jerárquica
- Facilitan distribución de código

### 4. Manejo de Errores
- SyntaxError: Errores de sintaxis
- TypeError: Tipos de datos incompatibles
- IndexError: Índices fuera de rango
- ImportError: Problemas de importación

---

## Mejores Prácticas Aplicadas

1. **Documentación:**
   - Docstrings en todas las funciones
   - Comentarios explicativos
   - README completo

2. **Organización:**
   - Código modular y reutilizable
   - Separación de responsabilidades
   - Estructura de directorios clara

3. **Nomenclatura:**
   - Nombres descriptivos
   - Snake_case para funciones y variables
   - Constantes en MAYÚSCULAS

4. **Manejo de Errores:**
   - Ejemplos educativos de errores comunes
   - Soluciones múltiples
   - Explicaciones detalladas

---

## Conclusiones

Este laboratorio demuestra:

1. La importancia de la modularización en Python
2. Cómo organizar código de forma profesional
3. El uso efectivo de parámetros por defecto
4. La creación y uso de módulos y paquetes
5. La identificación y corrección de errores comunes

El código está listo para ser utilizado como referencia en proyectos futuros y demuestra buenas prácticas de programación en Python.

---

## Referencias

- Documentación oficial de Python: https://docs.python.org/3/
- PEP 8 - Style Guide for Python Code
- Material del curso de Modularización
- Presentación del Instructor: Cristian Torres González

---

**Autor:** Alejandro Campos Martínez 
**Fecha:** 25/10/2025  
**Versión:** 1.0
