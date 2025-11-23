# Laboratorio 2: Special Methods (__init__, __str__, etc.)

## Información del Laboratorio

- **Curso**: Advanced Python
- **Institución**: CINVESTAV Guadalajara
- **Team**: 6
- **Integrantes**: 
  - Alejandro Campos Martínez
  - Agustín Jaime Navarro
- **Tema**: Special Methods (Dunder Methods) en Python
- **Fecha de Entrega**: Noviembre 12, 2025

---

## Objetivos

El objetivo de este laboratorio es comprender y aplicar los special methods (métodos especiales o "dunder methods") en Python para crear clases personalizadas que se integren naturalmente con la sintaxis del lenguaje. Específicamente:

1. Implementar una clase `AIModel` con múltiples special methods
2. Comprender el propósito y uso de cada special method
3. Crear objetos que se comporten como tipos built-in de Python
4. Demostrar operaciones aritméticas, comparaciones y comportamiento callable
5. Implementar limpieza de recursos con `__del__`

---

## Desarrollo

### Estructura del Proyecto

```
lab2_special_methods/
│
├── aimodel.py              # Implementación completa de AIModel
└── REPORT.md              # Este reporte
```

---

## Conceptos Fundamentales

### ¿Qué son los Special Methods?

Los special methods (también llamados "dunder methods" por sus dobles guiones bajos) son métodos predefinidos en Python que permiten que los objetos personalizados se comporten como tipos built-in. Comienzan y terminan con doble guión bajo (`__`).

**¿Por qué son importantes?**

- Hacen que las clases sean más intuitivas y pythonicas
- Se integran con la sintaxis nativa de Python
- Permiten sobrecarga de operadores
- Facilitan el uso de objetos en contextos específicos

---

## Implementación de la Clase AIModel

### Special Methods Implementados

La clase `AIModel` implementa los siguientes special methods:

| Special Method | Propósito | Sintaxis Habilitada |
|----------------|-----------|---------------------|
| `__init__` | Inicialización | `model = AIModel("GPT", 90)` |
| `__str__` | Representación amigable | `print(model)` |
| `__repr__` | Representación oficial | `repr(model)` |
| `__add__` | Operador suma | `model1 + model2` |
| `__lt__` | Menor que | `model1 < model2` |
| `__le__` | Menor o igual | `model1 <= model2` |
| `__gt__` | Mayor que | `model1 > model2` |
| `__ge__` | Mayor o igual | `model1 >= model2` |
| `__eq__` | Igualdad | `model1 == model2` |
| `__ne__` | Desigualdad | `model1 != model2` |
| `__call__` | Objeto callable | `model("input text")` |
| `__bool__` | Evaluación booleana | `if model:` |
| `__del__` | Destructor | `del model` |

---

### 1. __init__: Inicialización

```python
def __init__(self, name, score, active=True):
    """Inicializa una nueva instancia de AIModel."""
    self.name = name
    self.score = score
    self.active = active
    print(f"[INIT] AIModel '{self.name}' initialized with score {self.score}")
```

**Propósito**: Personalizar el objeto recién creado después de que `__new__()` lo crea.

**Flujo de creación de objetos**:
1. `__new__()` crea la instancia
2. `__init__()` inicializa los atributos
3. La instancia se retorna al llamador

**Características**:
- Es el constructor más común en Python
- Siempre retorna `None`
- Se llama automáticamente al crear una instancia

---

### 2. __str__ y __repr__: Representaciones de String

```python
def __repr__(self):
    """Representación oficial (para debugging)."""
    return f"AIModel('{self.name}', {self.score}, active={self.active})"

def __str__(self):
    """Representación amigable (para usuarios)."""
    status = "active" if self.active else "inactive"
    return f"Model '{self.name}' with score {self.score} ({status})"
```

**Diferencias clave**:

| Aspecto | __repr__ | __str__ |
|---------|----------|---------|
| Propósito | Debugging, desarrollo | Usuarios finales |
| Formato | Código Python válido (ideal) | Legible y amigable |
| Prioridad | Si no hay __str__, se usa __repr__ | Preferido por print() |
| Ejemplo | `AIModel('GPT', 90, active=True)` | `Model 'GPT' with score 90 (active)` |

**Cuándo se llaman**:
- `__repr__`: Por `repr()`, en el REPL, en listas
- `__str__`: Por `str()`, `print()`, `format()`

---

### 3. Operadores Aritméticos: __add__

```python
def __add__(self, other):
    """Define el comportamiento de model1 + model2."""
    if not isinstance(other, AIModel):
        return NotImplemented
    return self.score + other.score
```

**Características**:
- Permite usar el operador `+` con objetos personalizados
- Retorna `NotImplemented` para tipos incompatibles
- En este caso, suma los scores de dos modelos

**Uso**:
```python
model1 = AIModel("GPT-4", 90)
model2 = AIModel("BERT", 85)
combined = model1 + model2  # 175
```

---

### 4. Operadores de Comparación

```python
def __lt__(self, other):
    """Define model1 < model2."""
    if not isinstance(other, AIModel):
        return NotImplemented
    return self.score < other.score

def __gt__(self, other):
    """Define model1 > model2."""
    if not isinstance(other, AIModel):
        return NotImplemented
    return self.score > other.score
```

**Operadores de comparación disponibles**:
- `__lt__`: Less than (`<`)
- `__le__`: Less than or equal (`<=`)
- `__gt__`: Greater than (`>`)
- `__ge__`: Greater than or equal (`>=`)
- `__eq__`: Equal (`==`)
- `__ne__`: Not equal (`!=`)

**Beneficio**: Permite ordenar objetos con `sorted()`:
```python
models = [model1, model2, model3]
sorted_models = sorted(models, reverse=True)
```

---

### 5. __call__: Objetos Callable

```python
def __call__(self, input_text):
    """Hace que el objeto se pueda llamar como una función."""
    if not self.active:
        return f"[ERROR] Model '{self.name}' is not active"
    return f"{self.name} processed: '{input_text}'"
```

**Propósito**: Permite que un objeto se comporte como una función.

**Uso**:
```python
model = AIModel("GPT-4", 90)
result = model("Translate this")  # En lugar de model.process("Translate this")
# Output: "GPT-4 processed: 'Translate this'"
```

**Aplicaciones prácticas**:
- Decoradores
- Factories
- Functors
- APIs más limpias

---

### 6. __bool__: Evaluación Booleana

```python
def __bool__(self):
    """Define el valor booleano del objeto."""
    return self.active
```

**Propósito**: Controla cómo se evalúa el objeto en contextos booleanos.

**Uso en condicionales**:
```python
model = AIModel("GPT-4", 90, active=True)
if model:
    print("Model is ready")  # Se ejecuta

inactive_model = AIModel("Old", 50, active=False)
if not inactive_model:
    print("Model is inactive")  # Se ejecuta
```

**Sin __bool__**: Python usaría `__len__()` o consideraría el objeto siempre True.

---

### 7. __del__: Destructor

```python
def __del__(self):
    """Llamado cuando el objeto está a punto de ser destruido."""
    print(f"[CLEANUP] Model '{self.name}' is being deleted")
```

**Características importantes**:
- Se llama cuando no quedan referencias al objeto
- Útil para limpieza de recursos (archivos, conexiones, etc.)
- **No se garantiza** el momento exacto de ejecución
- Depende del garbage collector de Python

**Uso**:
```python
model = AIModel("Temp", 50)
del model  # Dispara __del__
# Output: [CLEANUP] Model 'Temp' is being deleted
```
---

## Pruebas y Resultados

### Ejecución Principal

```
================================================================================
Lab 2: Special Methods - AIModel Implementation
================================================================================

Test 1: __init__ - Object Initialization
--------------------------------------------------------------------------------
[INIT] AIModel 'GPT-4' initialized with score 90
[INIT] AIModel 'BERT' initialized with score 85
[INIT] AIModel 'Inactive-Model' initialized with score 70

Test 2: __str__ - User-friendly representation
--------------------------------------------------------------------------------
model1: Model 'GPT-4' with score 90 (active)
model2: Model 'BERT' with score 85 (active)
model3: Model 'Inactive-Model' with score 70 (inactive)

Test 3: __repr__ - Official representation (for debugging)
--------------------------------------------------------------------------------
repr(model1): AIModel('GPT-4', 90, active=True)
repr(model2): AIModel('BERT', 85, active=True)

Test 5: Comparison operators
--------------------------------------------------------------------------------
model1 > model2: True
model1 < model2: False
model1 == model2: False

Test 7: __call__ - Callable behavior
--------------------------------------------------------------------------------
GPT-4 processed: 'Translate this text to Spanish'
BERT processed: 'Classify this sentiment'
[ERROR] Model 'Inactive-Model' is not active
```

---

## Análisis de Errores y Soluciones

### Error 1: NotImplemented vs NotImplementedError

**Problema inicial**:
```python
def __add__(self, other):
    if not isinstance(other, AIModel):
        raise NotImplementedError()  # Incorrecto
```

**Solución correcta**:
```python
def __add__(self, other):
    if not isinstance(other, AIModel):
        return NotImplemented  # Correcto
```

**Explicación**:
- `NotImplemented` es un valor especial (singleton)
- `NotImplementedError` es una excepción
- Retornar `NotImplemented` permite que Python pruebe el método reverso
- Si ambos retornan `NotImplemented`, entonces Python lanza `TypeError`

---

### Error 2: __del__ no se llama inmediatamente

**Problema observado**:
```python
del model
print("Deleted")
# A veces no se imprime el mensaje de __del__ antes de "Deleted"
```

**Causa**:
El garbage collector de Python no garantiza el momento exacto de llamar `__del__`.

**Solución**:
Usar context managers para recursos críticos:
```python
class AIModel:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Limpieza garantizada
        print(f"Cleanup for {self.name}")

# Uso
with AIModel("GPT", 90) as model:
    model("Process this")
# Limpieza garantizada al salir del with
```

---

### Error 3: __str__ vs __repr__ confusión

**Problema**:
Al principio usábamos el mismo formato para ambos.

**Solución**:
Seguir las mejores prácticas:
- `__repr__`: Formato que puede recrear el objeto
- `__str__`: Formato legible para usuarios

```python
# Buena práctica
def __repr__(self):
    return f"AIModel('{self.name}', {self.score}, active={self.active})"

def __str__(self):
    return f"Model '{self.name}' with score {self.score}"
```

---

## Mejores Prácticas Aplicadas

### 1. Usar __repr__ para debugging

`__repr__` debe retornar una cadena que idealmente sea código Python válido:

```python
# En el REPL:
>>> model = AIModel("GPT", 90)
>>> model
AIModel('GPT', 90, active=True)  # Puedes copiar y pegar esto para recrear el objeto
```

---

### 2. Retornar NotImplemented apropiadamente

Para operadores binarios, siempre retornar `NotImplemented` para tipos incompatibles:

```python
def __add__(self, other):
    if not isinstance(other, AIModel):
        return NotImplemented  # Permite que Python pruebe other.__radd__(self)
    return self.score + other.score
```

---

### 3. Implementar operadores de comparación relacionados

Si implementas `__lt__`, considera implementar también:
- `__le__` (menor o igual)
- `__gt__` (mayor que)
- `__ge__` (mayor o igual)
- `__eq__` (igual)

O usa `functools.total_ordering`:
```python
from functools import total_ordering

@total_ordering
class AIModel:
    def __eq__(self, other):
        return self.score == other.score
    
    def __lt__(self, other):
        return self.score < other.score
    # Los demás se generan automáticamente
```

---

### 4. __bool__ para objetos con estado

Si un objeto tiene un concepto natural de "verdadero" o "falso", implementa `__bool__`:

```python
def __bool__(self):
    return self.active  # Un modelo inactivo es "falsy"
```

---

### 5. Evitar lógica compleja en __del__

`__del__` no es confiable para limpieza crítica. Usa context managers:

```python
# No recomendado
def __del__(self):
    self.save_to_database()  # Puede fallar o no ejecutarse

# Recomendado
def __enter__(self):
    return self

def __exit__(self, *args):
    self.save_to_database()  # Garantizado con 'with'
```

---

## Tabla de Special Methods Implementados

### Métodos de Inicialización y Representación

| Method | Propósito | Llamado por | 
|--------|-----------|-------------|
| `__init__` | Inicializa la instancia | `MyClass()` |
| `__del__` | Destructor | `del obj` o garbage collector |
| `__repr__` | Representación oficial | `repr(obj)` |
| `__str__` | Representación informal | `str(obj)`, `print(obj)` |

### Operadores Aritméticos

| Method | Operador | Ejemplo |
|--------|----------|---------|
| `__add__` | + | `a + b` |

### Operadores de Comparación

| Method | Operador | Ejemplo |
|--------|----------|---------|
| `__lt__` | < | `a < b` |
| `__le__` | <= | `a <= b` |
| `__gt__` | > | `a > b` |
| `__ge__` | >= | `a >= b` |
| `__eq__` | == | `a == b` |
| `__ne__` | != | `a != b` |

### Métodos Especiales

| Method | Propósito | Ejemplo ||
|--------|-----------|---------|
| `__call__` | Objeto callable | `obj()` |
| `__bool__` | Valor booleano | `bool(obj)`, `if obj` |

---

## Aplicaciones Prácticas

Los special methods implementados en este laboratorio tienen aplicaciones directas en el desarrollo profesional de Python:

### 1. APIs más Intuitivas

El uso de `__call__` permite crear objetos que se comportan como funciones, haciendo las APIs más limpias:

```python
model = AIModel("GPT-4", 90)
result = model("Procesar texto")  # Más limpio que model.process("Procesar texto")
```

### 2. Comparación y Ordenamiento

Los operadores de comparación permiten ordenar objetos personalizados de manera natural:

```python
models = [model1, model2, model3]
sorted_models = sorted(models)  # Ordena automáticamente por score
best_model = max(models)  # Encuentra el modelo con mayor score
```

### 3. Validación con __bool__

Usar objetos directamente en condicionales hace el código más pythonico:

```python
if model:
    # El modelo está activo, proceder
    result = model("input")
else:
    print("Modelo inactivo")
```

### 4. Debugging con __repr__

Una buena implementación de `__repr__` facilita el debugging:

```python
>>> model
AIModel('GPT-4', 90, active=True)  # Fácil de leer y copiar para recrear
```

---

## Conclusiones

### Aprendizajes Técnicos

La implementación de special methods en la clase AIModel reveló cómo Python permite que objetos personalizados se integren naturalmente con la sintaxis del lenguaje. Al implementar `__add__`, descubrimos que la sintaxis simple `model1 + model2` se traduce internamente en `model1.__add__(model2)`, demostrando el mecanismo de sobrecarga de operadores de Python.

La distinción entre `__str__` y `__repr__` enseñó una filosofía importante de diseño en Python: separar la representación para usuarios finales (legible y amigable) de la representación para desarrolladores (inequívoca y reproducible). Esta dualidad facilita tanto la experiencia del usuario como el proceso de debugging.

El método `__call__` demostró la flexibilidad de Python al permitir que objetos se comporten como funciones. Esta característica hace posible crear APIs más limpias donde `model("texto")` es más intuitivo que `model.process("texto")`, reduciendo la verbosidad del código.

La implementación de operadores de comparación (`__lt__`, `__gt__`, `__eq__`, etc.) permitió que los objetos AIModel funcionen perfectamente con funciones built-in como `sorted()`, `min()` y `max()`, demostrando cómo los special methods integran tipos personalizados en el ecosistema de Python.

El método `__bool__` mostró cómo Python permite que los objetos definan su propia "verdad contextual". Un modelo inactivo retorna `False`, permitiendo validaciones pythonicas como `if model:` en lugar de `if model.is_active():`.

La experiencia con `__del__` reveló las limitaciones del garbage collection en Python. Aunque parece un destructor tradicional, su naturaleza no determinista lo hace inadecuado para limpieza crítica de recursos, siendo los context managers la solución pythonica apropiada.

---

### Diseño y Arquitectura

Los special methods implementan el principio de "duck typing" de Python: no necesitamos heredar de ninguna clase especial para que nuestros objetos sean comparables u ordenables, solo necesitamos implementar los métodos correctos. Esto promueve composición sobre herencia.

El patrón de retornar `NotImplemented` en lugar de lanzar excepciones en operadores binarios permite que Python intente métodos alternativos, proporcionando un sistema de fallback robusto y comportamiento más intuitivo para el usuario.

La implementación de todos los operadores de comparación en lugar de solo uno o dos demuestra atención al detalle y proporciona una interfaz completa y consistente. Alternativamente, podríamos usar `functools.total_ordering` para reducir código repetitivo.

---

### Impacto en el Código

Los special methods transforman código imperativo verboso en código declarativo elegante:

**Sin special methods**:
```python
if model.is_active():
    result = model.process("text")
    combined = model.add_score(other_model)
    if model.compare_to(other_model) > 0:
        print("Better model")
```

**Con special methods**:
```python
if model:
    result = model("text")
    combined = model + other_model
    if model > other_model:
        print("Better model")
```

Esta transformación hace que el código sea más legible, mantenible y pythonico, reduciendo la barrera cognitiva para otros desarrolladores.

---

### Mejores Prácticas Aplicadas

1. **Retornar NotImplemented apropiadamente**: En operadores binarios, siempre retornar `NotImplemented` para tipos incompatibles, permitiendo que Python intente el método reverso
2. **Implementar __repr__ primero**: Si solo se implementa un método de representación, debe ser `__repr__` ya que también se usa cuando falta `__str__`
3. **Documentar el comportamiento**: Los special methods cambian fundamentalmente cómo se usa un objeto, por lo que requieren documentación clara
4. **Mantener consistencia**: Si se implementa `__eq__`, considerar implementar todos los operadores de comparación para una interfaz completa
5. **Evitar lógica compleja en __del__**: No es confiable para limpieza crítica, preferir context managers (`__enter__` y `__exit__`)

---

### Reflexión Final

Este laboratorio demostró que los special methods son mucho más que "azúcar sintáctico". Son el mecanismo fundamental que permite que Python sea un lenguaje expresivo y consistente, donde objetos personalizados pueden integrarse perfectamente con la sintaxis nativa del lenguaje. La implementación cuidadosa de estos métodos resulta en código más pythonico, mantenible y profesional.

---

## Referencias

- Python Official Documentation: [Data Model](https://docs.python.org/3/reference/datamodel.html)
- Python Official Documentation: [Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- PEP 207: [Rich Comparisons](https://www.python.org/dev/peps/pep-0207/)
- Fluent Python by Luciano Ramalho: Chapter 1 (The Python Data Model)
- Real Python: [Operator and Function Overloading](https://realpython.com/operator-function-overloading/)
- Slides del curso: AISpecial_methods.pdf

---

## Autor

**Team 6**
- Alejandro Campos Martínez
- Agustín Jaime Navarro

Advanced Python Course  
CINVESTAV Guadalajara  
Noviembre 2025

---

## Anexos

### Archivos Entregables

1. **aimodel.py** - Implementación completa de la clase AIModel con todos los special methods requeridos
2. **REPORT.md** - Este reporte completo

### Código Completo de AIModel

La implementación completa se encuentra en el archivo [aimodel.py](aimodel.py) e incluye:

- `__init__`: Inicialización de objetos
- `__str__`: Representación amigable para usuarios  
- `__repr__`: Representación oficial para debugging
- `__add__`: Operador de suma
- `__lt__, __le__, __gt__, __ge__, __eq__, __ne__`: Operadores de comparación completos
- `__call__`: Comportamiento callable
- `__bool__`: Evaluación booleana
- `__del__`: Destructor y limpieza


---

