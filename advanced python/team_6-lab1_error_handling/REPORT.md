# Laboratorio 1: Error Handling (Manejo de Excepciones)

## Información del Laboratorio

- **Curso**: Advanced Python
- **Institución**: CINVESTAV Guadalajara
- **Tema**: Manejo de Excepciones y Errores en Python
- **Fecha de Entrega**: Noviembre 7, 2025

---

## Objetivos

El objetivo de este laboratorio es extender el código de ejemplo proporcionado en clase para implementar un sistema robusto de manejo de excepciones que incluya:

1. Creación de excepciones personalizadas
2. Validación de entrada del usuario
3. Manejo de múltiples tipos de errores
4. Uso de bloques `finally` para cleanup
5. Implementación de buenas prácticas con `if __name__ == "__main__"`

---

## Desarrollo

### Requerimientos del Laboratorio

El laboratorio solicitaba las siguientes tareas:

- Crear una segunda excepción personalizada llamada `AgeTooLargeError` que se lance si la edad es mayor a 120

- Modificar la función `check_age()` para lanzar esta nueva excepción cuando sea necesario

- Agregar un bloque try-except para manejar `ValueError` si el usuario ingresa un valor no entero

- Envolver la lógica dentro de una función `main()`

- Agregar un bloque `finally` que imprima "Code processing finished!"

- Usar `if __name__ == "__main__"` para ejecutar la función `main()` solo cuando el script se ejecute directamente

---

## Implementación

### 1. Excepciones Personalizadas

Se crearon dos excepciones personalizadas siguiendo el patrón mostrado en clase:

```python
class AgeTooSmallError(Exception):
    """Exception raised when the input age is below the allowed threshold."""
    
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}"
        super().__init__(message)


class AgeTooLargeError(Exception):
    """Exception raised when the input age is above the maximum allowed threshold."""
    
    def __init__(self, age, threshold=120):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is above the maximum allowed threshold of {threshold}"
        super().__init__(message)
```

**Explicación:**
- Ambas excepciones heredan de la clase base `Exception`
- Cada una tiene atributos personalizados (`age` y `threshold`)
- Se utiliza `super().__init__(message)` para inicializar la excepción base con un mensaje descriptivo
- Los valores por defecto facilitan su uso

---

### 2. Función de Validación

La función `check_age()` fue modificada para validar tanto el límite inferior como superior:

```python
def check_age(age):
    """
    Checks if the age meets the minimum and maximum requirements.
    
    Args:
        age (int): The age to validate
        
    Raises:
        AgeTooSmallError: If age is below 18
        AgeTooLargeError: If age is above 120
        
    Returns:
        None: Prints "Access granted" if age is valid
    """
    if age < 18:
        raise AgeTooSmallError(age)
    if age > 120:
        raise AgeTooLargeError(age)
    print("Access granted")
```

**Explicación:**
- La función verifica primero si la edad es menor a 18
- Luego verifica si es mayor a 120
- Solo si pasa ambas validaciones, otorga acceso
- Incluye documentación clara usando docstrings

---

### 3. Función Principal con Manejo Completo de Excepciones

```python
def main():
    """
    Main entry point of the program.
    Handles user input and exception management.
    """
    try:
        # Get user input
        age_input = input("Please enter your age: ")
        
        # Try to convert input to integer
        try:
            age = int(age_input)
        except ValueError:
            raise ValueError(f"Invalid input: '{age_input}' is not a valid integer. Please enter a numeric age.")
        
        # Check if the age is valid
        check_age(age)
        print(f"Age {age} is valid and within acceptable range.")
        
    except AgeTooSmallError as err:
        print(f"Custom exception caught: {err}")
        print(f"   → You must be at least {err.threshold} years old to access this system.")
        
    except AgeTooLargeError as err:
        print(f"Custom exception caught: {err}")
        print(f"   → Maximum age allowed is {err.threshold} years.")
        
    except ValueError as err:
        print(f"ValueError caught: {err}")
        print(f"   → Please make sure to enter only numbers.")
        
    except Exception as err:
        print(f"Unexpected error occurred: {type(err).__name__}")
        print(f"   → Details: {err}")
        
    finally:
        print("\n" + "="*50)
        print("Code processing finished!")
        print("="*50)
```

**Características importantes:**

1. **Try anidado para ValueError**: Se usa un try-except interno específicamente para la conversión a entero
2. **Múltiples bloques except**: Cada tipo de excepción tiene su propio manejador con mensajes específicos
3. **Bloque finally**: Se ejecuta siempre, independientemente de si ocurrió una excepción o no
4. **Manejo genérico**: Un `except Exception` final captura cualquier error inesperado

---

### 4. Guard del Módulo

```python
if __name__ == "__main__":
    """
    This ensures that main() only runs when the script is executed directly,
    not when the file is imported as a module.
    This is a best practice for writing reusable and testable Python code.
    """
    print("="*50)
    print("Lab 1: Age Validation System")
    print("="*50)
    print()
    main()
```

**Propósito:**
- Permite que el módulo sea importado sin ejecutar automáticamente `main()`
- Es una buena práctica para código reutilizable
- Facilita las pruebas unitarias

---

## Pruebas y Resultados

### Caso 1: Edad Menor a 18 (AgeTooSmallError)

**Input:** `16`

**Output:**
```
==================================================
Lab 1: Age Validation System
==================================================

Please enter your age: ERROR: Custom exception caught: Age 16 is below the allowed threshold of 18
       You must be at least 18 years old to access this system.

==================================================
Code processing finished!
==================================================
```

**Análisis:** La excepción personalizada `AgeTooSmallError` fue lanzada correctamente y el mensaje es claro para el usuario.

---

### Caso 2: Edad Mayor a 120 (AgeTooLargeError)

**Input:** `150`

**Output:**
```
==================================================
Lab 1: Age Validation System
==================================================

Please enter your age: ERROR: Custom exception caught: Age 150 is above the maximum allowed threshold of 120
       Maximum age allowed is 120 years.

==================================================
Code processing finished!
==================================================
```

**Análisis:** La nueva excepción `AgeTooLargeError` funciona correctamente y proporciona feedback útil.

---

### Caso 3: Entrada No Numérica (ValueError)

**Input:** `abc`

**Output:**
```
==================================================
Lab 1: Age Validation System
==================================================

Please enter your age: ERROR: ValueError caught: Invalid input: 'abc' is not a valid integer. Please enter a numeric age.
       Please make sure to enter only numbers.

==================================================
Code processing finished!
==================================================
```

**Análisis:** El manejo de `ValueError` captura correctamente las entradas no numéricas y muestra la entrada inválida.

---

### Caso 4: Edad Válida (Caso Exitoso)

**Input:** `25`

**Output:**
```
==================================================
Lab 1: Age Validation System
==================================================

Please enter your age: Access granted
Age 25 is valid and within acceptable range.

==================================================
Code processing finished!
==================================================
```

**Análisis:** Cuando la entrada es válida, el sistema funciona correctamente y muestra mensajes de confirmación.

---

## Errores Encontrados y Soluciones

### Error 1: Orden de Validación

**Problema inicial:** 
Al principio consideré validar primero si era mayor a 120 y luego menor a 18, pero esto no afectaba la lógica.

**Solución:** 
Mantuve el orden lógico: primero verificar el mínimo, luego el máximo. Es más intuitivo.

---

### Error 2: Manejo de ValueError

**Problema inicial:**
No estaba claro si debía manejar el `ValueError` directamente o lanzar uno personalizado.

**Solución:**
Decidí capturar el `ValueError` de `int()` y lanzar uno nuevo con un mensaje más descriptivo que incluya la entrada del usuario.

**Código:**
```python
try:
    age = int(age_input)
except ValueError:
    raise ValueError(f"Invalid input: '{age_input}' is not a valid integer...")
```

Esto permite mostrar al usuario exactamente qué ingresó mal.

---

### Error 3: Bloques Finally

**Problema inicial:**
Inicialmente solo imprimía el mensaje simple en el `finally`.

**Solución:**
Agregué separadores visuales para hacer más clara la salida:

```python
finally:
    print("\n" + "="*50)
    print("Code processing finished!")
    print("="*50)
```

---

## Conceptos Clave Aplicados

### 1. Try-Except-Finally

| Bloque | Propósito | Ejecución |
|--------|-----------|-----------|
| `try` | Código que puede generar excepciones | Siempre |
| `except` | Manejo de excepciones específicas | Solo si ocurre la excepción |
| `finally` | Código de limpieza | Siempre, incluso si hay excepciones |

---

### 2. Jerarquía de Excepciones

```
Exception (Base)
├── ValueError
├── TypeError
├── AgeTooSmallError (Custom)
└── AgeTooLargeError (Custom)
```

---

### 3. Buenas Prácticas Implementadas

- **Excepciones específicas**: Crear excepciones personalizadas para casos de negocio específicos

- **Mensajes descriptivos**: Cada excepción tiene un mensaje claro y útil

- **Documentación**: Todas las funciones y clases tienen docstrings

- **Separación de concerns**: La validación está separada en su propia función

- **Guard de módulo**: Uso de `if __name__ == "__main__"`

- **Manejo defensivo**: Catch genérico para errores inesperados

---

## Conclusiones

### Aprendizajes Técnicos

1. **Excepciones Personalizadas**: Aprendí a crear excepciones que heredan de `Exception` y que pueden contener atributos y lógica personalizada. Esto hace el código más expresivo y mantenible.

2. **Bloques Try Anidados**: Descubrí que es útil anidar bloques try-except para manejar errores en diferentes niveles de granularidad. El try interno para `int()` me permite dar un mensaje más específico.

3. **Finally para Cleanup**: El bloque `finally` es crucial para garantizar que ciertas operaciones (como cerrar archivos o mostrar mensajes de finalización) se ejecuten sin importar qué pase.

4. **Guard Pattern**: El uso de `if __name__ == "__main__"` es fundamental para escribir código modular y testeable.

---

### Reflexiones sobre el Diseño

1. **Separación de Responsabilidades**: 
   - Las excepciones manejan casos específicos
   - `check_age()` solo valida edades
   - `main()` coordina la entrada/salida y el flujo

2. **Experiencia de Usuario**:
   Los mensajes de error están diseñados para ser:
   - Claros (indican qué salió mal)
   - Útiles (sugieren cómo corregir el problema)
   - Consistentes (mismo formato para todos los errores)

3. **Extensibilidad**:
   El código puede extenderse fácilmente para:
   - Agregar más validaciones
   - Crear nuevas excepciones personalizadas
   - Integrar con sistemas de logging

---

### Aplicaciones Prácticas

Este tipo de manejo de excepciones es fundamental en:

- **Validación de formularios web**: Verificar edades, correos, teléfonos
- **APIs REST**: Devolver códigos de error apropiados
- **Sistemas críticos**: Donde los errores deben manejarse sin que el sistema falle
- **Procesamiento de datos**: Validar entradas de archivos CSV, JSON, etc.

---

## Posibles Mejoras Futuras

1. **Logging**: Agregar un sistema de logs para registrar errores
   ```python
   import logging
   logging.error(f"Invalid age attempt: {age}")
   ```

2. **Configuración Externa**: Permitir configurar los límites desde un archivo
   ```python
   MIN_AGE = config.get('min_age', 18)
   MAX_AGE = config.get('max_age', 120)
   ```

3. **Pruebas Unitarias**: Crear tests usando `pytest` o `unittest`
   ```python
   def test_age_too_small():
       with pytest.raises(AgeTooSmallError):
           check_age(15)
   ```

4. **Internacionalización**: Soporte para múltiples idiomas en los mensajes

5. **Retry Logic**: Permitir múltiples intentos de entrada
   ```python
   for attempt in range(3):
       try:
           # ... input logic
           break
       except ValueError:
           if attempt == 2:
               raise
   ```

---

## Referencias

- Python Official Documentation: [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- PEP 8: [Style Guide for Python Code](https://pep8.org/)
- Real Python: [Python Exceptions](https://realpython.com/python-exceptions/)
- Slides del curso: AIException_Handling.pdf

---

## Autor

**Team [NÚMERO]**  
Advanced Python Course  
CINVESTAV Guadalajara  
Noviembre 2025

---

## Anexos

### Código Completo

Ver archivo: `lab1_error_handling.py`

### Estructura de Archivos Entregada

```
advanced_python/
└── team_[NÚMERO]-lab1_error_handling/
    ├── lab1_error_handling.py
    └── REPORT.md (este archivo)
```

---

**FIN DEL REPORTE**
