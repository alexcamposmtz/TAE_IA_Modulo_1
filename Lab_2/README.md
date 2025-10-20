# Lab 2: Python Introduction

**Estudiante:** Alejandro Campos Martínez  
**Instructor:** Cristian Torres González  
**Fecha de asignación:** 14/10/2025  
**Fecha de entrega:** 19/10/2025

---

## Descripción

Este laboratorio aplica los conceptos de Python vistos en clase a través de tres secciones:

1. **Sección 1: Práctica de Programación** - Ejercicios prácticos con tipos de datos, operaciones y estructuras básicas
2. **Sección 2: Investigación de Documentación** - Investigación de métodos y funciones de Python
3. **Sección 3: Detección de Errores** - Identificación y corrección de errores comunes

---

## Sección 1: Práctica de Programación

### Task 1: Conversión de tipos de datos
Convierte una variable string ("123" y "hello") a integer, float, boolean, list y tuple. Demuestra qué conversiones funcionan y cuáles generan errores.

### Task 2: Operaciones aritméticas
Realiza suma, resta, multiplicación y división con números int y float. Verifica el tipo de dato de cada resultado.

### Task 3: Máximo, mínimo y longitud
Encuentra el elemento máximo, mínimo y la longitud de una lista usando únicamente métodos de lista (`.copy()`, `.sort()`, `.pop()`). No se permite usar `len()`, `min()` o `max()`.

### Task 4: Diccionario de estudiantes
Calcula el promedio de calificaciones para cada estudiante usando un diccionario. Crea un nuevo diccionario con nombres y promedios usando la función `sum()`.

---

## Sección 2: Investigación de Documentación

### Task 5: Método .sort()
Investiga y explica el método `.sort()` para ordenar listas. Incluye ejemplos con parámetros `key` y `reverse`, y la diferencia con `sorted()`.

### Task 6: Método .replace()
Investiga y explica el método `.replace()` para strings. Incluye ejemplos de reemplazo simple, con límite, y reemplazos encadenados.

### Task 7: Expresión s *= n
Explica la expresión `s *= n` para secuencias mutables. Demuestra la diferencia entre secuencias mutables (listas) e inmutables (strings, tuplas) usando `id()`.

### Task 8: Función input()
Explica la función `input()` para leer entrada del usuario. Incluye ejemplos de conversión de tipos, validación y manejo de excepciones.

---

## Sección 3: Detección de Errores

### Task 9: SyntaxError
Error de paréntesis sin cerrar en una función `print()`. Se explica la causa y la solución.

### Task 10: TypeError
Error al intentar concatenar un string con un entero usando `+`. Se presentan cuatro soluciones: `str()`, f-strings, `.format()` y comas en print.

### Task 11: IndexError
Error al intentar acceder a un índice que no existe en una lista. Se explican cuatro soluciones: índices válidos, índices negativos, verificación de longitud y try-except.

### Task 12: KeyError
Error al intentar acceder a una clave que no existe en un diccionario. Se presentan cinco soluciones: verificar con `in`, método `.get()`, `.get()` con valor por defecto, try-except, y agregar la clave.

---

## Estructura de archivos

```
lab2/
├── README.md
├── section_1/
│   ├── task_1.py
│   ├── task_2.py
│   ├── task_3.py
│   └── task_4.py
├── section_2/
│   ├── task_5.py
│   ├── task_6.py
│   ├── task_7.py
│   └── task_8.py
└── section_3/
    ├── task_9.py
    ├── task_10.py
    ├── task_11.py
    └── task_12.py
```

---

## Notas

- Todos los archivos incluyen comentarios explicativos
- Los archivos de la Sección 3 muestran el error comentado para evitar que el código falle al ejecutar
- Se incluyen múltiples ejemplos y soluciones para cada concepto
