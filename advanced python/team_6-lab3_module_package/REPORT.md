# Laboratorio 3: Modules and Packages

## Información del Laboratorio

- **Curso**: Advanced Python
- **Institución**: CINVESTAV Guadalajara
- **Team**: 6
- **Integrantes**: 
  - Alejandro Campos Martínez
  - Agustín Jaime Navarro
- **Tema**: Módulos y Gestión de Paquetes en Python
- **Fecha de Entrega**: Noviembre 10, 2025

---

## Objetivos

El objetivo de este laboratorio es comprender y aplicar los conceptos de módulos y paquetes en Python, específicamente:

1. Crear un módulo personalizado para procesamiento de texto
2. Crear un paquete con submódulos para inferencia de modelos
3. Integrar módulos y paquetes en un programa principal
4. Demostrar diferentes métodos de importación

---

## Desarrollo

### Estructura del Proyecto

El laboratorio requería crear la siguiente jerarquía de directorios:

```
team_6-lab3_module_package/
│
├── main.py                    # Programa principal
├── text_utils.py              # Parte 1: Módulo de procesamiento de texto
│
└── ai_models/                 # Parte 2: Paquete para inferencia de modelo
    ├── __init__.py            # Inicializador del paquete
    └── mock_model.py          # Módulo de predicción
```

---

## Implementación

### Parte 1: Módulo de Procesamiento de Texto (text_utils.py)

Se creó un módulo simple con una función para limpiar texto.

```python
def clean_text(text):
    """
    Limpia y normaliza el texto convirtiéndolo a minúsculas.
    
    Args:
        text (str): El texto a procesar
        
    Returns:
        str: El texto convertido a minúsculas
    """
    return text.lower()
```

**Características del módulo:**

- Función simple y enfocada en una tarea específica
- Documentación clara con docstring
- Incluye ejemplos de uso en la documentación
- Bloque de prueba con `if __name__ == "__main__"` para testing independiente

**Justificación del diseño:**

La función `clean_text()` es intencionalmente simple para este laboratorio, pero en un proyecto podría extenderse para:
- Remover puntuación
- Eliminar espacios extra
- Normalizar caracteres especiales
- Tokenización

---

### Parte 2: Paquete ai_models

#### 2.1 Archivo `__init__.py`

El archivo inicializador del paquete cumple varias funciones importantes:

```python
"""
Paquete ai_models: Contiene módulos para inferencia de modelos simulados.
"""

# Importar la función predict para facilitar su uso
from .mock_model import predict

# Definir exportaciones
__all__ = ['predict']

# Metadatos del paquete
__version__ = '1.0.0'
__author__ = 'Team 6'
```

**Funciones del `__init__.py`:**

1. **Inicialización del paquete**: Marca el directorio como un paquete Python
2. **Importaciones convenientes**: Permite usar `from ai_models import predict` directamente
3. **Control de exportaciones**: Define qué se exporta con `import *`
4. **Metadatos**: Información sobre versión y autores

---

#### 2.2 Módulo `mock_model.py`

Este módulo contiene la lógica de predicción de sentimiento:

```python
def predict(text):
    """
    Realiza una predicción de sentimiento simple basada en palabras clave.
    
    Args:
        text (str): El texto a analizar
        
    Returns:
        str: "positive" si "good" está en el texto, "negative" en caso contrario
    """
    text_lower = text.lower()
    
    if "good" in text_lower:
        return "positive"
    else:
        return "negative"
```

**Características del módulo:**

- Implementa un modelo de sentimiento simulado muy básico
- Convierte el texto a minúsculas para búsqueda case-insensitive
- Retorna valores claros y consistentes
- Incluye documentación y ejemplos

---

### Parte 3: Programa Principal (main.py)

El programa principal integra ambas partes del laboratorio:

```python
import text_utils
from ai_models import predict

def main():
    test_texts = [
        "This is a GOOD day for learning Python!",
        "MODULES and PACKAGES are IMPORTANT concepts",
        # ... más casos de prueba
    ]
    
    for text in test_texts:
        cleaned = text_utils.clean_text(text)
        sentiment = predict(cleaned)
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}")
```

**Flujo del programa:**

1. Importa el módulo `text_utils`
2. Importa la función `predict` del paquete `ai_models`
3. Procesa una lista de textos de prueba
4. Para cada texto:
   - Limpia el texto con `clean_text()`
   - Predice el sentimiento con `predict()`
   - Muestra los resultados

---

## Pruebas y Resultados

### Ejecución del Programa

```
============================================================
Lab 3: Modules and Packages Demonstration
============================================================

Testing Module and Package Integration:
------------------------------------------------------------

Test Case 1:
Original text: 'This is a GOOD day for learning Python!'
Cleaned text:  'this is a good day for learning python!'
Sentiment:     positive

Test Case 2:
Original text: 'MODULES and PACKAGES are IMPORTANT concepts'
Cleaned text:  'modules and packages are important concepts'
Sentiment:     negative

Test Case 3:
Original text: 'I love programming with Python'
Cleaned text:  'i love programming with python'
Sentiment:     negative

Test Case 4:
Original text: 'This is a bad example'
Cleaned text:  'this is a bad example'
Sentiment:     negative

Test Case 5:
Original text: 'Good morning, everyone!'
Cleaned text:  'good morning, everyone!'
Sentiment:     positive
```

### Análisis de Resultados

**Casos positivos (contienen "good"):**
- Test Case 1: "GOOD day" → detectado correctamente
- Test Case 5: "Good morning" → detectado correctamente

**Casos negativos (no contienen "good"):**
- Test Cases 2, 3, 4 → clasificados correctamente como negativos

El sistema funciona según lo esperado para este laboratorio.

---

## Métodos de Importación

El laboratorio demuestra cuatro métodos diferentes de importar módulos:

### Método 1: Import Module

```python
import text_utils
result = text_utils.clean_text("TEXT")
```

**Ventajas:** Namespace claro, evita conflictos de nombres

### Método 2: From Package Import Function

```python
from ai_models import predict
result = predict("text")
```

**Ventajas:** Acceso directo a la función, código más conciso

### Método 3: Import Package

```python
import ai_models
result = ai_models.predict("text")
```

**Ventajas:** Acceso a todo el paquete, namespace explícito

### Método 4: From Package Import Module

```python
from ai_models import mock_model
result = mock_model.predict("text")
```

**Ventajas:** Acceso al módulo completo

---

## Errores Encontrados y Soluciones

### Error 1: ModuleNotFoundError

**Problema:**
Al principio, intenté ejecutar `main.py` desde un directorio diferente y obtuve:
```
ModuleNotFoundError: No module named 'text_utils'
```

**Causa:**
Python busca módulos en el directorio actual y en `sys.path`. Si el script no se ejecuta desde el directorio correcto, no encuentra los módulos.

**Solución:**
Ejecutar el script desde el directorio `team_6-lab3_module_package`:


---

### Error 2: Namespace Pollution con `import *`

**Problema:**
Usar `from module import *` puede causar conflictos de nombres.

**Solución aplicada:**
En `__init__.py`, definimos explícitamente qué exportar:
```python
__all__ = ['predict']
```

Esto controla qué se importa cuando alguien hace `from ai_models import *`.

---

## Conceptos Clave Aplicados

### 1. Módulos vs Paquetes

| Aspecto | Módulo | Paquete |
|---------|--------|---------|
| Definición | Archivo .py individual | Directorio con `__init__.py` |
| Contenido | Funciones, clases, variables | Múltiples módulos |
| Propósito | Organizar código relacionado | Organizar múltiples módulos |
| Ejemplo | `text_utils.py` | `ai_models/` |

---

### 2. El archivo `__init__.py`

**Funciones principales:**

1. **Marca de paquete**: Indica que el directorio es un paquete Python
2. **Inicialización**: Código que se ejecuta al importar el paquete
3. **Control de namespace**: Define la API pública del paquete
4. **Importaciones convenientes**: Expone funciones de submódulos

**Ejemplo práctico:**

Sin `__init__.py`:
```python
from ai_models.mock_model import predict
```

Con `__init__.py` configurado:
```python
from ai_models import predict  # Más limpio
```

---

### 3. El patrón `if __name__ == "__main__"`

Este patrón permite que un módulo sea:
1. **Ejecutable**: Como script independiente
2. **Importable**: Sin ejecutar el código de prueba

```python
def my_function():
    return "Hello"

if __name__ == "__main__":
    # Este código solo se ejecuta si el archivo se ejecuta directamente
    print(my_function())
```

**Ventajas:**
- Permite testing unitario dentro del módulo
- El código de prueba no se ejecuta al importar
- Facilita el desarrollo modular

---


## Conclusiones

### Aprendizajes Técnicos

Durante el desarrollo de este laboratorio, se consolidaron los siguientes conceptos fundamentales sobre la arquitectura modular de Python:
La implementación de módulos personalizados demostró cómo Python utiliza archivos individuales como unidades de código reutilizable. El módulo text_utils.py funcionó como un componente independiente que pudo ser importado y utilizado sin dependencias externas, ilustrando el principio de encapsulación a nivel de archivo.
La creación del paquete ai_models reveló la importancia del archivo __init__.py como mecanismo de inicialización. Este archivo no solo marca un directorio como paquete Python, sino que también permite controlar explícitamente qué componentes se exponen a través del namespace del paquete.

El manejo de importaciones mostró la flexibilidad del sistema de módulos de Python. Las importaciones absolutas (import text_utils) proporcionaron claridad en el origen del código, mientras que las importaciones relativas (from .mock_model import predict) demostraron ser más mantenibles dentro de la estructura del paquete.

La gestión de namespaces se evidenció como un aspecto crítico para evitar colisiones de nombres. El uso de importaciones específicas versus importaciones globales (import *) impacta directamente en la legibilidad del código y en la prevención de efectos secundarios inesperados.

---

### Acerca del Diseño

La arquitectura modular implementada en este laboratorio reflejó principios fundamentales de ingeniería de software aplicados al ecosistema Python.
El principio de responsabilidad única se manifestó en la separación clara entre procesamiento de texto (text_utils) y análisis de sentimiento (mock_model). Cada módulo mantiene una cohesión alta al enfocarse en una tarea específica, mientras que el acoplamiento entre módulos se mantiene bajo mediante interfaces bien definidas.
La estructura de paquetes establecida facilita la escalabilidad del proyecto. La jerarquía ai_models/ puede extenderse con submódulos adicionales sin modificar el código existente, demostrando el principio Open/Closed. Nuevos modelos de análisis podrían agregarse como módulos hermanos de mock_model.py sin romper la funcionalidad existente.

El patrón de testing implementado mediante if __name__ == "__main__" permitió validar cada componente de forma aislada. Esta separación entre código de producción y código de prueba representa una práctica esencial en el desarrollo de software mantenible, facilitando tanto el desarrollo iterativo como la detección temprana de errores.

---

### Aplicaciones Prácticas

Este tipo de organización es fundamental en:

- **Proyectos de Data Science**: Para organizar pipeline de datos, modelos y utilidades
- **Desarrollo Web**: Para separar rutas, modelos, vistas y lógica de negocio
- **Automatización**: Para crear herramientas reutilizables
- **Librerías**: Para distribuir código que otros pueden usar

---

### Mejores Prácticas 

1. Siempre usar docstrings descriptivos
2. Mantener módulos enfocados en una responsabilidad
3. Usar `__init__.py` para crear APIs limpias
4. Incluir código de testing con `if __name__ == "__main__"`
5. Seguir convenciones de nombres de Python (PEP 8)
6. Documentar no solo qué hace el código, sino por qué

---

## Referencias

- Python Official Documentation: [Modules](https://docs.python.org/3/tutorial/modules.html)
- Python Official Documentation: [Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- PEP 8: [Style Guide for Python Code](https://pep8.org/)
- Real Python: [Python Modules and Packages](https://realpython.com/python-modules-packages/)
- Slides del curso: AI-Modules-Packages.pdf

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
team_6-lab3_module_package/
│
├── main.py                    # Programa principal (integración)
├── text_utils.py              # Módulo de procesamiento de texto
│
└── ai_models/                 # Paquete de modelos AI
    ├── __init__.py            # Inicializador del paquete
    └── mock_model.py          # Módulo de predicción
```

### Archivos Entregables

1. `main.py` - Programa principal
2. `text_utils.py` - Módulo de utilidades
3. `ai_models/__init__.py` - Inicializador del paquete
4. `ai_models/mock_model.py` - Módulo de predicción
5. `REPORT.md` - Este reporte

---
