# Lab 8: Matplotlib & Generadores

**Curso:** Talento Altamente Especializado – Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Cristian Torres González  
**Equipo:** Team 6
- Alejandro Campos Martínez

**Fecha de asignación:** 31/10/2025  
**Fecha de entrega:** 10/11/2025

---

## Descripción del Laboratorio

Este laboratorio introduce la **visualización de datos con Matplotlib** y el uso de **List Comprehensions** para generar datos, incluyendo:
- Generación de señales (ondas seno)
- Visualización de formas geométricas (círculos concéntricos)
- Configuración avanzada de gráficas
- List comprehensions para procesamiento de datos
- Detección y corrección de errores comunes con matplotlib

---

## Estructura del Laboratorio

```
Lab_8/
├── README.md
├── Section_1/
│   ├── task_1.py    # Ondas Seno
│   └── task_2.py    # Círculos Concéntricos
└── Section_2/
    ├── task_3.py    # ModuleNotFoundError
    ├── task_4.py    # ValueError
    ├── task_5.py    # NameError
    └── task_6.py    # KeyError
```

---

## Sección 1: Práctica de Programación

### Task 1: Ondas seno con matplotlib
Generación y visualización de dos señales de onda seno con diferentes frecuencias.

**Características:**
- Generación de ondas usando list comprehension
- Primera onda: frecuencia 1 Hz
- Segunda onda: frecuencia 3 Hz
- Multiplicación punto por punto de las dos ondas
- Visualización en tres subplots separados

**Configuración de gráficas incluye:**
- Títulos descriptivos en cada subplot
- Etiquetas en ambos ejes (X: tiempo en radianes, Y: amplitud)
- Ticks configurados en el eje X con valores π
- Ticks configurados en el eje Y
- Grid para mejor visualización
- Leyendas para identificar cada onda
- Colores diferenciados para cada señal

**Ejecución:**
```bash
python3 Section_1/task_1.py
```

**Conceptos demostrados:**
- **List comprehension:** Generación eficiente de secuencias de datos
- **Matplotlib subplots:** Organización de múltiples gráficas
- **Configuración de ejes:** Ticks personalizados con símbolos matemáticos
- **Multiplicación elemento por elemento:** Procesamiento de señales

---

### Task 2: Círculos concéntricos
Generación y visualización de círculos concéntricos usando ecuaciones paramétricas.

**Características:**
- Generación de puntos de círculos usando list comprehension
- Ecuaciones paramétricas: x = r·cos(θ), y = r·sin(θ)
- Múltiples círculos con radios: 1, 2, 3, 4, 5
- 1000 puntos por círculo para suavidad
- Dos visualizaciones: círculos superpuestos e individuales

**Configuración de gráficas incluye:**
- Título general descriptivo
- Etiquetas en ambos ejes
- Ticks configurados cada 1 unidad
- Grid para referencia
- Ejes en el centro (x=0, y=0)
- Aspecto igual (círculos no distorsionados)
- Leyenda con radios de cada círculo
- Colores diferenciados

**Ejecución:**
```bash
python3 Section_1/task_2.py
```

**Conceptos demostrados:**
- **Geometría paramétrica:** Generación de formas usando ecuaciones
- **List comprehension anidada:** Múltiples círculos
- **Matplotlib aspect ratio:** Mantener proporciones correctas
- **Subplots múltiples:** Comparación visual

---

## Sección 2: Detección de errores

Esta sección documenta **cuatro tipos de errores** encontrados durante la práctica con matplotlib y visualización de datos.

### Task 3: ModuleNotFoundError
**Error:** Error tipográfico en el nombre del módulo al importar matplotlib.

```python
import matplotlb.pyplot as plt  # Error: 'matplotlb' en vez de 'matplotlib'
```

**Mensaje de error:**
```
ModuleNotFoundError: No module named 'matplotlb'
```

**Causa:** Error tipográfico en el nombre del módulo. Se escribió 'matplotlb' en lugar de 'matplotlib'.

**Soluciones:**
1. Corregir el nombre del módulo a 'matplotlib'
2. Verificar que el módulo esté instalado: `pip install matplotlib`
3. Verificar el entorno virtual activo

**Ejecución:**
```bash
python3 Section_2/task_3.py
```

---

### Task 4: ValueError
**Error:** Intentar graficar arrays de diferentes longitudes en matplotlib.

```python
x = [1, 2, 3, 4, 5]  # 5 elementos
y = [1, 4, 9, 16]    # 4 elementos (Error: longitudes diferentes)
plt.plot(x, y)
```

**Mensaje de error:**
```
ValueError: x and y must have same first dimension, but have shapes (5,) and (4,)
```

**Causa:** Las listas x e y tienen diferentes longitudes. Matplotlib requiere que tengan la misma cantidad de elementos para emparejar puntos (x, y).

**Soluciones:**
1. Asegurar que x e y tengan la misma longitud desde el inicio
2. Usar list comprehension para generar datos (garantiza consistencia)
3. Recortar la lista más larga
4. Revisar la lógica de generación de datos

**Ejecución:**
```bash
python3 Section_2/task_4.py
```

---

### Task 5: NameError
**Error:** Usar una variable antes de definirla en un list comprehension.

```python
x = np.linspace(0, 2 * np.pi, 100)
y = [np.sin(xi) * amplitude for xi in x]  # Error: 'amplitude' no definida
```

**Mensaje de error:**
```
NameError: name 'amplitude' is not defined
```

**Causa:** La variable `amplitude` se usa en el list comprehension antes de ser definida.

**Soluciones:**
1. Definir la variable antes de usarla
2. Usar funciones con parámetros para evitar variables globales
3. Verificar el orden de las sentencias
4. Revisar el scope de las variables

**Ejecución:**
```bash
python3 Section_2/task_5.py
```

---

### Task 6: KeyError
**Error:** Intentar acceder a una clave que no existe en un diccionario de configuración.

```python
plot_config = {
    'color': '#FF6B6B',
    'linewidth': 2,
    'linestyle': '-'
}
marker = plot_config['marker']  # Error: 'marker' no existe
```

**Mensaje de error:**
```
KeyError: 'marker'
```

**Causa:** Se intenta acceder a la clave 'marker' que no existe en el diccionario `plot_config`.

**Soluciones:**
1. Agregar la clave faltante al diccionario
2. Usar `dict.get('key', default)` con valor por defecto
3. Verificar existencia con `if 'key' in dict` antes de acceder
4. Usar try-except para manejar el error

**Ejecución:**
```bash
python3 Section_2/task_6.py
```

---

## Ejecución del Laboratorio

### Requisitos:
```bash
pip install matplotlib numpy
```

### Ejecutar todas las tareas de la Sección 1:
```bash
cd Lab_8
python3 Section_1/task_1.py
python3 Section_1/task_2.py
```

### Ejecutar todas las tareas de la Sección 2:
```bash
python3 Section_2/task_3.py
python3 Section_2/task_4.py
python3 Section_2/task_5.py
python3 Section_2/task_6.py
```

---

## Conceptos clave aprendidos

### 1. List Comprehensions
- **Sintaxis:** `[expresion for item in iterable]`
- Forma concisa de crear listas
- Más eficiente que bucles tradicionales
- Ideal para transformación de datos
- Ejemplo: `y = [x**2 for x in range(10)]`

### 2. Matplotlib - Configuración Básica
- **Importación:** `import matplotlib.pyplot as plt`
- **Figure y Axes:** Estructura de gráficas
- **plot():** Función principal para líneas
- **show():** Mostrar la gráfica

### 3. Configuración de Ejes
- **Títulos:** `ax.set_title()`, `plt.title()`
- **Etiquetas:** `ax.set_xlabel()`, `ax.set_ylabel()`
- **Ticks:** `ax.set_xticks()`, `ax.set_yticks()`
- **Etiquetas de ticks:** `ax.set_xticklabels()`
- **Límites:** `ax.set_xlim()`, `ax.set_ylim()`

### 4. Personalización de Gráficas
- **Colores:** Códigos hexadecimales o nombres
- **Líneas:** `linewidth`, `linestyle`, `alpha`
- **Marcadores:** `marker`, `markersize`
- **Grid:** `ax.grid(True, alpha=0.3)`
- **Leyendas:** `ax.legend()`

### 5. Subplots
- **Creación:** `fig, axes = plt.subplots(nrows, ncols)`
- **Acceso:** `axes[i]` o `axes[i, j]`
- **Layout:** `plt.tight_layout()`

### 6. Geometría Paramétrica
- **Círculo:** x = r·cos(θ), y = r·sin(θ)
- **Ondas:** y = A·sin(ω·t)
- Generación eficiente con list comprehension

---

## Errores Comunes con Matplotlib

1. **Importación incorrecta del módulo**
   - Verificar ortografía
   - Verificar instalación

2. **Arrays de diferentes longitudes**
   - Usar list comprehension para consistencia
   - Verificar dimensiones antes de graficar

3. **Variables no definidas**
   - Definir variables antes de usarlas
   - Cuidado con el orden en list comprehensions

4. **Claves inexistentes en diccionarios**
   - Usar `dict.get()` con defaults
   - Verificar con `in` antes de acceder

5. **Gráficas no se muestran**
   - Llamar a `plt.show()` al final
   - Verificar que no haya errores previos

---

## Buenas prácticas

**Organización del código:**
- Separar generación de datos de visualización
- Usar funciones para reutilización
- Documentar con docstrings

**List comprehensions:**
- Usar para transformaciones simples
- No abusar de la complejidad
- Considerar legibilidad

**Matplotlib:**
- Usar interface orientada a objetos (fig, ax)
- Configurar todos los elementos visuales
- Incluir títulos y etiquetas siempre
- Usar colores y estilos consistentes

**Manejo de errores:**
- Verificar importaciones
- Validar dimensiones de datos
- Usar valores por defecto apropiados

---

## Recursos adicionales

- [Documentación oficial de Matplotlib](https://matplotlib.org/stable/index.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- Slides del curso: Matplotlib y Generadores

---



**Team 6**  
Noviembre 2025
