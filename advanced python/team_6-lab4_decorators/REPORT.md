# Laboratorio 4: Decorators

## Información del Laboratorio

- **Curso**: Advanced Python
- **Institución**: CINVESTAV Guadalajara
- **Team**: 6
- **Integrantes**: 
  - Alejandro Campos Martínez
  - Agustín Jaime Navarro
- **Tema**: Decorators en Python
- **Fecha de Entrega**: Noviembre 11, 2025

---

## Objetivos

El objetivo de este laboratorio es comprender y aplicar el concepto de decoradores en Python, específicamente:

1. Crear un decorador de logging que registre llamadas a funciones
2. Implementar un decorador de control de acceso para funciones sensibles
3. Comprender el patrón de wrapper functions
4. Aplicar stacking de decoradores
5. Entender el uso de `*args` y `**kwargs` en decoradores

---

## Desarrollo

### Estructura del Proyecto

El laboratorio requería crear la siguiente jerarquía de archivos:

```
team_6-lab4_decorators/
│
├── lab1_logging_decorator.py      # Lab 1: Decorador de logging
├── lab2_access_control.py         # Lab 2: Control de acceso
├── main.py                         # Integración de ambos labs
└── REPORT.md                       # Este reporte
```

---

## Implementación

### Lab 1: Logging Decorator

El primer laboratorio requería crear un decorador llamado `logger` que imprima el nombre de la función y los argumentos con los que fue llamada.

```python
def logger(func):
    """
    Decorador que registra información sobre las llamadas a funciones.
    """
    def wrapper(*args, **kwargs):
        # Construir cadena de argumentos posicionales
        args_str = ', '.join([repr(arg) for arg in args])
        
        # Construir cadena de argumentos keyword
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        
        # Combinar ambos tipos de argumentos
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        # Imprimir información de logging
        print(f"[LOG] Calling function '{func.__name__}' with arguments: {all_args}")
        
        # Llamar a la función original
        result = func(*args, **kwargs)
        
        # Log del resultado
        print(f"[LOG] Function '{func.__name__}' returned: {repr(result)}")
        
        return result
    
    return wrapper
```

**Características del decorador:**

- Captura tanto argumentos posicionales (`*args`) como keyword (`**kwargs`)
- Registra el nombre de la función usando `func.__name__`
- Muestra los argumentos de forma legible usando `repr()`
- Registra también el valor de retorno
- Preserva la funcionalidad original de la función

**Aplicación a función matemática:**

```python
@logger
def add(a, b):
    return a + b

# Uso
result = add(5, 3)
# Output:
# [LOG] Calling function 'add' with arguments: 5, 3
# [LOG] Function 'add' returned: 8
```

---

### Lab 2: Access Control Decorator

El segundo laboratorio requería crear un decorador llamado `require_admin` que verifica si se pasa el argumento keyword `role="admin"`.

```python
def require_admin(func):
    """
    Decorador que verifica si el usuario tiene permisos de administrador.
    """
    def wrapper(*args, **kwargs):
        # Verificar si el argumento 'role' existe y es 'admin'
        user_role = kwargs.get('role', None)
        
        if user_role == 'admin':
            print(f"[ACCESS GRANTED] User with role '{user_role}' can access '{func.__name__}'")
            # Remover 'role' de kwargs antes de llamar la función
            kwargs_clean = {k: v for k, v in kwargs.items() if k != 'role'}
            return func(*args, **kwargs_clean)
        else:
            print(f"[ACCESS DENIED] User with role '{user_role}' cannot access '{func.__name__}'")
            print(f"[ACCESS DENIED] Admin privileges required for '{func.__name__}'")
            return None
    
    return wrapper
```

**Características del decorador:**

- Extrae el valor de `role` de los kwargs usando `kwargs.get()`
- Compara el rol con 'admin' para determinar el acceso
- Limpia kwargs antes de pasar a la función original (elimina 'role')
- Retorna None si el acceso es denegado
- Proporciona mensajes claros de acceso concedido o denegado

**Aplicación a función sensible:**

```python
@require_admin
def delete_user(username):
    return f"User '{username}' has been successfully deleted from the system."

# Uso sin permisos
result1 = delete_user('john_doe')
# Output:
# [ACCESS DENIED] User with role 'None' cannot access 'delete_user'
# [ACCESS DENIED] Admin privileges required for 'delete_user'
# result1 = None

# Uso con permisos
result2 = delete_user('john_doe', role='admin')
# Output:
# [ACCESS GRANTED] User with role 'admin' can access 'delete_user'
# result2 = "User 'john_doe' has been successfully deleted from the system."
```

---

## Pruebas y Resultados

### Ejecución del Lab 1

```
======================================================================
Lab 4: Decorators - Lab 1: Logging Decorator
======================================================================

Test 1: Función add(5, 3)
----------------------------------------------------------------------
[LOG] Calling function 'add' with arguments: 5, 3
[LOG] Function 'add' returned: 8
Resultado: 8

Test 2: Función multiply(4, 5)
----------------------------------------------------------------------
[LOG] Calling function 'multiply' with arguments: 4, 5
[LOG] Function 'multiply' returned: 20
Resultado: 20

Test 3: Función multiply(2, 3, z=4)
----------------------------------------------------------------------
[LOG] Calling function 'multiply' with arguments: 2, 3, z=4
[LOG] Function 'multiply' returned: 24
Resultado: 24
```

### Análisis de Resultados del Lab 1

El decorador `logger` funciona correctamente en todos los casos de prueba:

**Argumentos posicionales**: Captura y muestra correctamente `add(5, 3)`

**Argumentos mixtos**: Maneja adecuadamente la combinación de posicionales y keyword en `multiply(2, 3, z=4)`

**Valores de retorno**: Registra los resultados de cada función

---

### Ejecución del Lab 2

```
======================================================================
Lab 4: Decorators - Lab 2: Access Control Decorator
======================================================================

Test 1: delete_user('juan_bananas') - WITHOUT admin role
----------------------------------------------------------------------
[ACCESS DENIED] User with role 'None' cannot access 'delete_user'
[ACCESS DENIED] Admin privileges required for 'delete_user'
Result: None

Test 2: delete_user('juan_bananas', role='admin') - WITH admin role
----------------------------------------------------------------------
[ACCESS GRANTED] User with role 'admin' can access 'delete_user'
Result: User 'juan_bananas' has been successfully deleted from the system.

Test 3: delete_user('san_blas_crazy_woman', role='user') - WITH user role
----------------------------------------------------------------------
[ACCESS DENIED] User with role 'user' cannot access 'delete_user'
[ACCESS DENIED] Admin privileges required for 'delete_user'
Result: None
```

### Análisis de Resultados del Lab 2

El decorador `require_admin` implementa correctamente el control de acceso:

**Sin rol especificado**: Detecta `role='None'` y niega el acceso

**Con rol admin**: Otorga acceso y ejecuta la función normalmente

**Con rol no-admin**: Rechaza roles como 'user' que no sean 'admin'

---

## Conceptos Avanzados Implementados

### 1. Uso de *args y **kwargs

Los decoradores utilizan `*args` y `**kwargs` para capturar cualquier combinación de argumentos:

```python
def wrapper(*args, **kwargs):
    # *args captura argumentos posicionales como tupla
    # **kwargs captura argumentos keyword como diccionario
    result = func(*args, **kwargs)
    return result
```

**Ventaja**: Permite que el decorador funcione con cualquier función, independientemente de su firma.

---

### 2. Stacking de Decoradores

Se puede aplicar múltiples decoradores a una misma función:

```python
@timer
@require_admin
@logger
def backup_system(backup_name):
    return f"System backed up as '{backup_name}'"
```

**Orden de ejecución**: Los decoradores se aplican de abajo hacia arriba:
1. Primero se aplica `logger`
2. Luego `require_admin`
3. Finalmente `timer`

Pero se ejecutan de arriba hacia abajo cuando se llama la función.

---

### 3. Preservación de Metadata con functools.wraps

Para preservar el nombre y docstring de la función original:

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**Sin @wraps**: `add.__name__` retornaría 'wrapper'

**Con @wraps**: `add.__name__` retorna 'add' correctamente

---

### 4. Closure en Decoradores

Los decoradores son un ejemplo perfecto de closures:

```python
def logger(func):  # Función externa
    def wrapper(*args, **kwargs):  # Función interna
        # wrapper tiene acceso a 'func' (variable de scope externo)
        result = func(*args, **kwargs)
        return result
    return wrapper
```

La función `wrapper` mantiene una referencia a `func` incluso después de que `logger` haya terminado de ejecutarse.

---

## Errores Encontrados y Soluciones

### Error 1: TypeError con kwargs extras

**Problema:**
Al principio, el decorador `require_admin` pasaba el argumento `role` a la función decorada, causando:
```
TypeError: delete_user() got an unexpected keyword argument 'role'
```

**Causa:**
La función `delete_user()` no acepta el parámetro `role`, pero el decorador lo estaba pasando.

**Solución:**
Limpiar kwargs antes de pasar a la función original:
```python
kwargs_clean = {k: v for k, v in kwargs.items() if k != 'role'}
return func(*args, **kwargs_clean)
```

---

### Error 2: Pérdida de metadata de función

**Problema:**
Después de decorar, `add.__name__` retornaba 'wrapper' en lugar de 'add'.

**Causa:**
El decorador reemplaza la función original con la función wrapper, perdiendo metadata.

**Solución:**
Usar `@wraps(func)` del módulo functools:
```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...
```

---

### Error 3: Representación confusa de argumentos

**Problema:**
Los strings se imprimían sin comillas, haciendo difícil distinguir tipos:
```
[LOG] Calling 'greet' with arguments: Alice
```

**Causa:**
Usar `str()` en lugar de `repr()` para convertir argumentos.

**Solución:**
Usar `repr()` para obtener representación con comillas:
```python
args_str = ', '.join([repr(arg) for arg in args])
```

Resultado:
```
[LOG] Calling 'greet' with arguments: 'Alice'
```

---

## Conceptos Clave Aplicados

### Decoradores vs Funciones Normales

| Aspecto | Función Normal | Decorador |
|---------|---------------|-----------|
| Propósito | Realizar una tarea específica | Modificar comportamiento de otras funciones |
| Input | Datos | Función |
| Output | Datos procesados | Función modificada |
| Uso | `result = func(data)` | `@decorator` |
| Ejemplo | `add(2, 3)` | `@logger` |

---

### Patrón Wrapper Function

El patrón fundamental de los decoradores es la wrapper function:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Código antes de la función
        result = func(*args, **kwargs)
        # Código después de la función
        return result
    return wrapper
```

**Componentes:**

1. **Función externa (decorator)**: Recibe la función a decorar
2. **Función interna (wrapper)**: Envuelve la función original
3. **Retorno**: La función externa retorna la wrapper

---

### Sintaxis del Decorador (@)

El símbolo `@` es azúcar sintáctico:

```python
@logger
def add(a, b):
    return a + b
```

Es equivalente a:

```python
def add(a, b):
    return a + b

add = logger(add)
```

---

## Aplicaciones Prácticas

### 1. Logging y Debugging

Los decoradores de logging son fundamentales para:
- Rastrear llamadas a funciones en producción
- Debugging de aplicaciones complejas
- Auditoría de operaciones
- Análisis de rendimiento

**Ejemplo real:**
```python
@logger
def process_payment(amount, user_id):
    # Lógica de pago
    pass
```

---

### 2. Control de Acceso y Seguridad

Los decoradores de autorización se usan ampliamente en:
- Frameworks web (Flask, Django)
- APIs RESTful
- Sistemas de administración
- Microservicios

**Ejemplo real en Flask:**
```python
@app.route('/admin/delete-user')
@require_admin
def delete_user_endpoint():
    # Solo accesible para admins
    pass
```

---

### 3. Medición de Performance

```python
@timer
def expensive_operation():
    # Operación costosa
    pass
```

Útil para:
- Identificar cuellos de botella
- Optimización de código
- Monitoreo de performance
- SLA compliance

---

### 4. Caching y Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Aplicaciones:
- Optimización de funciones costosas
- Reducción de llamadas a base de datos
- Cache de resultados de API

---

### 5. Rate Limiting

```python
@rate_limit(max_calls=100, time_window=3600)
def api_endpoint():
    # Máximo 100 llamadas por hora
    pass
```

---

## Mejores Prácticas Aplicadas

### 1. Uso de functools.wraps

Siempre preservar metadata de la función original:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**Beneficio**: Mantiene `__name__`, `__doc__`, y otros atributos.

---

### 2. Aceptar Argumentos Arbitrarios

Usar `*args` y `**kwargs` para flexibilidad:

```python
def wrapper(*args, **kwargs):
    # Funciona con cualquier firma de función
    return func(*args, **kwargs)
```

---

### 3. Retornar el Resultado Original

Siempre retornar el resultado de la función decorada:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # No olvidar retornar result
        return result
    return wrapper
```

---

### 4. Separación de Concerns

Cada decorador debe tener una responsabilidad única:

- `@logger`: Solo logging
- `@require_admin`: Solo autenticación
- `@timer`: Solo medición de tiempo

**Evitar**: Decoradores que hacen múltiples cosas no relacionadas.

---

### 5. Documentación Clara

Siempre documentar qué hace el decorador:

```python
def logger(func):
    """
    Decorador que registra información sobre las llamadas a funciones.
    
    Registra el nombre de la función, argumentos y valor de retorno.
    """
    ...
```

---

### 6. Manejo de Casos Edge

Considerar casos especiales:

```python
def require_admin(func):
    def wrapper(*args, **kwargs):
        user_role = kwargs.get('role', None)
        
        # Manejar caso donde role no existe
        if user_role is None:
            print("No role provided")
            return None
            
        # Manejar caso donde role es incorrecto
        if user_role != 'admin':
            print("Insufficient privileges")
            return None
            
        return func(*args, **kwargs)
    return wrapper
```

---

## Conclusiones

### Aprendizajes Técnicos

La implementación de decoradores reveló conceptos fundamentales sobre la naturaleza de las funciones como objetos de primera clase en Python. Los decoradores funcionan porque Python permite pasar funciones como argumentos y retornar funciones como resultados, habilitando el patrón de envolver funcionalidad existente con comportamiento adicional sin modificar el código original.

El manejo de argumentos variables mediante `*args` y `**kwargs` demostró ser crucial para crear decoradores genéricos. Esta flexibilidad permite que un solo decorador funcione con funciones de cualquier aridad o firma, desde funciones sin argumentos hasta aquellas con múltiples parámetros posicionales y keyword. La capacidad de desempaquetar y reempaquetar argumentos de forma transparente es fundamental para mantener la compatibilidad con la función decorada.

El concepto de closure se manifiesta claramente en los decoradores, donde la función wrapper interna mantiene acceso a la variable `func` del scope externo incluso después de que la función decoradora haya terminado de ejecutarse. Este mecanismo permite que el wrapper "recuerde" qué función debe invocar, ilustrando cómo Python gestiona los scopes léxicos y la persistencia de referencias.

La preservación de metadata mediante `functools.wraps` evidenció la importancia de mantener la identidad de las funciones decoradas. Sin este mecanismo, herramientas de introspección y documentación perderían información valiosa sobre las funciones originales, afectando la depuración y la generación automática de documentación.

---

### Acerca del Diseño

El patrón decorador ejemplifica el principio de responsabilidad única al permitir que cada decorador encapsule una preocupación transversal específica. La separación entre logging, control de acceso y medición de tiempo en decoradores distintos facilita la composición modular de comportamientos sin acoplamiento innecesario entre funcionalidades ortogonales.

El stacking de decoradores ilustra el principio Open/Closed, permitiendo extender el comportamiento de funciones sin modificar su implementación. Las funciones originales permanecen cerradas a modificación mientras están abiertas a extensión mediante la aplicación de decoradores adicionales. Esta composición por capas permite construir pipelines de procesamiento complejos de manera declarativa.

La arquitectura de wrapper functions implementa efectivamente el patrón Proxy, donde el wrapper actúa como intermediario que controla el acceso a la función objetivo. Este patrón permite agregar verificaciones de precondiciones, logging, caching o cualquier otra lógica cross-cutting sin contaminar la lógica de negocio de la función decorada.

El uso de decoradores para control de acceso demuestra el patrón Template Method, donde la estructura general del flujo de control está definida en el decorador mientras que la lógica específica permanece en la función decorada. Esta inversión de control facilita la aplicación consistente de políticas de seguridad a través de múltiples endpoints o funciones.

---

### Aplicaciones Prácticas

Los decoradores son fundamentales en frameworks web modernos donde se utilizan para routing, autenticación, autorización, manejo de errores, validación de datos y transformación de respuestas. Frameworks como Flask y Django dependen extensivamente de decoradores para definir endpoints y aplicar middleware de forma declarativa.

En sistemas de observabilidad, los decoradores permiten instrumentar aplicaciones sin contaminar la lógica de negocio con código de telemetría. La capacidad de agregar logging, métricas y tracing mediante decoradores facilita el monitoreo de aplicaciones en producción mientras mantiene el código limpio y enfocado.

Para optimización de performance, decoradores como `lru_cache` de functools demuestran cómo la memoización puede aplicarse de forma no invasiva a funciones costosas, mejorando drásticamente el rendimiento sin modificar la implementación subyacente.

---

### Mejores Prácticas 

1. Siempre usar `@wraps` de functools para preservar metadata de funciones
2. Diseñar decoradores con responsabilidad única y bien definida
3. Usar `*args` y `**kwargs` para crear decoradores genéricos y reutilizables
4. Documentar claramente el comportamiento y los side effects de cada decorador
5. Considerar el orden de aplicación al stackear múltiples decoradores
6. Retornar siempre el resultado de la función decorada para mantener la cadena de ejecución
7. Manejar casos edge como argumentos faltantes o valores None apropiadamente

---

## Referencias

- Python Official Documentation: [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- Python Official Documentation: [functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
- PEP 318: [Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
- Real Python: [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
- Slides del curso: AI-Functools_lab_4.pdf

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

### Estructura Final de Archivos

```
team_6-lab4_decorators/
│
├── lab1_logging_decorator.py      # Decorador de logging
├── lab2_access_control.py         # Decorador de control de acceso
└── REPORT.md                       # Este reporte
```

### Archivos Entregables

1. `lab1_logging_decorator.py` - Lab 1: Logging Decorator
2. `lab2_access_control.py` - Lab 2: Access Control Decorator
3. `main.py` - Integración y demos avanzados
4. `REPORT.md` - Este reporte

---

