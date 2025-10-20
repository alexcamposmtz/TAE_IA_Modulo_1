# Lab 3: Control Structures
**Talento Altamente Especializado – Inteligencia Artificial 2025**  
**COCYTEN-Nayarit**

## Información del Laboratorio
**Instructor:** Cristian Torres González  
**Fecha de Asignación:** 14/10/2025  
**Fecha de Entrega:** 19/10/2025  
**Estudiante:** Alejandro Campos Martínez

---

## Introducción
Este laboratorio se enfoca en la práctica de estructuras de control en Python, elementos fundamentales para el desarrollo de algoritmos. Los temas incluyen:

- Ciclos (Loops): sentencias `for` y `while`
- Estructuras condicionales: `if`, `elif`, `else`
- Control de flujo: `break`, `continue`
- Operaciones con matrices sin usar librerías externas
- Manejo de errores y técnicas de depuración

**Recordatorio: Multiplicación de Matrices**  
Para multiplicar matrices A × B = C:

Cada elemento `C[i][j] = Σ(A[i][k] × B[k][j])` para k = 0 hasta n  
Se requieren tres loops anidados  
Las dimensiones deben ser compatibles  

Ejemplo:  
`C[0][0] = A[0][0]×B[0][0] + A[0][1]×B[1][0] + A[0][2]×B[2][0] + A[0][3]×B[3][0]`

---

## Estructura del Proyecto
```
lab3/
├── README.md
├── section_1/          (Práctica de Programación)
│   ├── task_1.py      → Multiplicación de Matrices 4x4
│   ├── task_2.py      → Filtrado de Diccionarios
│   ├── task_3.py      → Juego de Adivinar Número
│   └── task_4.py      → Validador de Contraseñas
└── section_2/          (Detección de Errores)
    ├── task_5.py      → SyntaxError
    ├── task_6.py      → TypeError
    ├── task_7.py      → IndexError
    └── task_8.py      → KeyError
```

---

## Sección 1: Práctica de Programación

### Task 1: Multiplicación de Matrices 4x4
**Objetivo:** Implementar multiplicación de matrices 4×4 sin usar librerías.

**Características:**
- Tres loops anidados para calcular cada elemento
- Inicialización de matriz resultado con ceros
- Ejemplos de cálculo detallado
- Sin uso de NumPy u otras librerías

**Algoritmo:**
```python
for i in range(4):           # Filas de A
    for j in range(4):       # Columnas de B
        C[i][j] = 0
        for k in range(4):   # Producto punto
            C[i][j] += A[i][k] * B[k][j]
```
**Archivo:** `section_1/task_1.py`

---

### Task 2: Filtrado de Diccionarios
**Objetivo:** Crear y filtrar diccionarios basados en letras específicas.

**Requisitos:**
- Diccionario principal con 42 nombres de animales
- Tres diccionarios filtrados que contienen palabras con:
  - Letra "a"
  - Letra "b"
  - Letra "y"

**Técnicas utilizadas:**
- Iteración sobre diccionarios con `.items()`
- Búsqueda case-insensitive con `.lower()`
- Creación de diccionarios dinámicos
- Conteo de elementos filtrados

**Archivo:** `section_1/task_2.py`

---

### Task 3: Juego de Adivinar Número
**Objetivo:** Crear un juego interactivo de adivinanza de números.

**Características:**
- Generación de número aleatorio entre 1-100
- Sistema de pistas (mayor/menor)
- Contador de intentos
- Validación de entrada con `try-except`
- Retroalimentación según rendimiento

**Estructuras de control usadas:**
- `while` para continuación del juego
- `if-elif-else` para comparación
- `try-except` para validación de entrada

**Archivo:** `section_1/task_3.py`

---

### Task 4: Validador de Contraseñas
**Objetivo:** Validar creación de contraseñas con reglas de seguridad.

**Reglas de validación:**
- Mínimo 8 caracteres
- Sin espacios
- No puede contener: &, #, %, @

**Características:**
- Validación múltiple simultánea
- Mensajes de error claros
- Loop de reintentos
- Tips de seguridad adicionales

**Archivo:** `section_1/task_4.py`

---

## Sección 2: Detección de Errores
Cada archivo de error sigue el formato estándar:
- Código incorrecto comentado
- Mensaje de error real
- Explicación detallada
- Múltiples soluciones
- Ejemplos adicionales

---

### Task 5: SyntaxError
**Tipo:** Error de Sintaxis
**Causa común:** Falta de dos puntos (:) en estructuras de control

**Ejemplo del error:**
```python
# Incorrecto
while contador < 5
    print(contador)
```

**Solución:**
```python
# Correcto
while contador < 5:
    print(contador)
```



**Archivo:** `section_2/task_5.py`

---

### Task 6: TypeError
**Tipo:** Error de Tipos
**Causa común:** Operaciones entre tipos incompatibles

**Ejemplo del error:**
```python
# Incorrecto
edad = 25
mensaje = "Tengo " + edad + " años"
```

**Soluciones:**
```python
# Conversión con str()
mensaje = "Tengo " + str(edad) + " años"

# F-strings (recomendado)
mensaje = f"Tengo {edad} años"
```

**Archivo:** `section_2/task_6.py`

---

### Task 7: IndexError
**Tipo:** Error de Índice
**Causa común:** Acceso a índice fuera del rango

**Ejemplo del error:**
```python
# Incorrecto
numeros = [10, 20, 30, 40, 50]
print(numeros[5])  # Fuera de rango
```

**Soluciones:**
```python
# Índice correcto
print(numeros[4])

# Índice negativo
print(numeros[-1])

# Verificar longitud
if index < len(numeros):
    print(numeros[index])
```

**Archivo:** `section_2/task_7.py`

---

### Task 8: KeyError
**Tipo:** Error de Clave
**Causa común:** Acceso a clave inexistente en diccionario

**Ejemplo del error:**
```python
# Incorrecto
estudiantes = {"Ana": 95}
nota = estudiantes["Pedro"]
```

**Soluciones:**
```python
# Verificar con 'in'
if "Pedro" in estudiantes:
    nota = estudiantes["Pedro"]

# Usar .get() (RECOMENDADO)
nota = estudiantes.get("Pedro", "No encontrado")
```


**Archivo:** `section_2/task_8.py`

---

## Cómo Ejecutar
**Sección 1 - Práctica:**
```bash
cd section_1
python task_1.py  # Multiplicación de matrices
python task_2.py  # Filtrado de diccionarios
python task_3.py  # Juego (interactivo)
python task_4.py  # Validador (interactivo)
```

**Sección 2 - Errores:**
```bash
cd section_2
python task_5.py  # SyntaxError
python task_6.py  # TypeError
python task_7.py  # IndexError
python task_8.py  # KeyError
```

---

## Referencias
- Python Documentation
- Control Flow
- Data Structures
- Errors and Exceptions

---

## Buenas Prácticas

**Programación Defensiva:**
- Validar entrada de usuario
- Verificar límites antes de acceder
- Usar tipos de datos apropiados
- Verificar claves en diccionarios

**Manejo de Errores:**
- Usar `try-except` apropiadamente
- Mensajes de error claros
- Retroalimentación al usuario

---

**Laboratorio completado por:**  Alejandro Campos Martínez
**Fecha:** 19 de octubre de 2025  
**COCYTEN-Nayarit · Inteligencia Artificial 2025**