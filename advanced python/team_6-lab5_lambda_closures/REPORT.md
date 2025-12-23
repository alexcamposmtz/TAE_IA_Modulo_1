# Laboratorio 5: Lambda Expressions y Closures

## Información del Laboratorio

**Equipo:** Team 6  
**Integrantes:**
  - Alejandro Campos Martínez
  - Agustín Jaime Navarro

**Curso:** Advanced Python
**Tema** Lambda Expressions y Closures
**Institución:** CINVESTAV Guadalajara  
**Fecha:** Noviembre 2025

---

## 1. Introducción

Este laboratorio explora dos conceptos fundamentales de la programación funcional en Python: las **expresiones lambda** y los **closures**. El objetivo principal es implementar un closure llamado `adder` que retorna una expresión lambda para realizar operaciones de suma, demostrando cómo estas técnicas permiten crear funciones más flexibles y expresivas.

### Objetivos Específicos

1. Comprender y aplicar el concepto de expresiones lambda en Python
2. Implementar closures que capturen variables de su scope externo
3. Combinar lambdas y closures para crear funciones especializadas
4. Validar el funcionamiento mediante dos pruebas distintas

---

## 2. Marco Teórico

### 2.1 Expresiones Lambda

Las **expresiones lambda** son funciones anónimas de una sola línea que se definen con la palabra clave `lambda`. Su sintaxis básica es:

```python
lambda argumentos: expresión
```

**Características principales:**
- **Anónimas:** No requieren un nombre (no usan `def`)
- **Una sola expresión:** Solo pueden contener una expresión, no múltiples statements
- **Retorno automático:** El resultado de la expresión se retorna automáticamente
- **Uso común:** Ideales como argumentos para funciones como `map()`, `filter()`, y `sorted()`

**Limitaciones:**
- No pueden contener múltiples líneas de código
- No soportan statements como asignaciones o loops
- Menos legibles que funciones nombradas para lógica compleja
- No pueden incluir docstrings

### 2.2 Closures

Un **closure** es una función que tiene acceso a variables de su scope externo, incluso después de que la función externa haya terminado su ejecución. Esto es posible porque la función interna "captura" las variables del scope externo.

**Componentes de un closure:**
1. Una función externa que define variables locales
2. Una función interna que usa esas variables
3. La función externa retorna la función interna (no su resultado)

**Características:**
- **Encapsulación de estado:** Mantienen estado sin usar variables globales
- **Variables libres:** Las variables capturadas se llaman "free variables"
- **Persistencia:** El estado persiste entre llamadas
- **Uso de `nonlocal`:** Permite modificar variables del scope externo

### 2.3 Combinación Lambda + Closure

Cuando un closure retorna una lambda, se crea una función especializada que:
- Captura el contexto del closure
- Ejecuta una operación simple definida por la lambda
- Permite crear múltiples funciones especializadas desde una fábrica común

---

## 3. Desarrollo del Laboratorio

### 3.1 Implementación del Closure `adder`

```python
def adder(x):
    """
    Closure que captura un valor y retorna una lambda expression
    para sumar ese valor con otro valor dado.
    
    Args:
        x: Primer valor a sumar (será capturado por el closure)
        
    Returns:
        Lambda function que toma un segundo valor y retorna la suma
    """
    # La lambda captura la variable 'x' del scope externo (closure)
    # y la suma con el parámetro 'y' que recibe
    return lambda y: x + y
```

**Análisis técnico:**
- `x` es la variable capturada (free variable)
- La lambda retornada tiene acceso a `x` incluso después de que `adder()` termine
- Cada llamada a `adder()` crea un nuevo closure con su propio valor de `x`
- La lambda es la función interna que ejecuta la operación de suma

### 3.2 Test 1: Suma de Dos Valores del Usuario

**Objetivo:** Solicitar dos valores enteros al usuario y sumarlos usando el closure.

```python
def test_user_input():
    """
    Primera prueba: Solicita dos valores enteros al usuario
    y utiliza el closure adder para sumarlos.
    """
    print("=" * 50)
    print("TEST 1: User Input Sum")
    print("=" * 50)
    
    try:
        # Solicitar el primer valor al usuario
        input_str = input("Enter the first integer value: ")
        valor1 = int(input_str.strip())
        
        # Solicitar el segundo valor al usuario
        input_str = input("Enter the second integer value: ")
        valor2 = int(input_str.strip())
        
        # Crear el closure con el primer valor
        suma_funcion = adder(valor1)
        
        # Aplicar la lambda con el segundo valor
        resultado = suma_funcion(valor2)
        
        print(f"\nResult: {valor1} + {valor2} = {resultado}")
        print("Test 1 completed successfully!")
        
    except (ValueError, EOFError):
        print("Error: Please enter valid integer values.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

**Flujo de ejecución:**
1. Se solicita el primer valor al usuario y se convierte a entero
2. Se solicita el segundo valor al usuario y se convierte a entero
3. Se llama a `adder(valor1)` que retorna una lambda con `valor1` capturado
4. Se ejecuta la lambda pasándole `valor2` como argumento
5. La lambda suma `valor1 + valor2` y retorna el resultado

**Manejo de errores:**
- `ValueError`: Se captura cuando el usuario ingresa texto no numérico
- `EOFError`: Se captura cuando hay problemas con el input stream
- `Exception`: Captura cualquier otro error inesperado

### 3.3 Test 2: Suma con Lista de Elementos

**Objetivo:** Sumar un valor entero con cada elemento de una lista de 5 elementos.

```python
def test_list_sum():
    """
    Segunda prueba: Suma un valor entero con cada elemento
    de una lista usando el closure adder.
    """
    print("\n" + "=" * 50)
    print("TEST 2: Integer + List Elements")
    print("=" * 50)
    
    try:
        # Solicitar el valor entero base
        input_str = input("Enter an integer value to add to the list: ")
        valor_base = int(input_str.strip())
        
        # Crear una lista con 5 elementos
        lista_numeros = [10, 20, 30, 40, 50]
        print(f"\nList of numbers: {lista_numeros}")
        
        # Crear el closure con el valor base
        suma_funcion = adder(valor_base)
        
        # Aplicar la lambda a cada elemento de la lista usando map
        resultados = list(map(suma_funcion, lista_numeros))
        
        print(f"\nBase value: {valor_base}")
        print(f"Results after adding {valor_base} to each element:")
        
        # Mostrar los resultados detalladamente
        for i, (original, resultado) in enumerate(zip(lista_numeros, resultados)):
            print(f"  Position {i}: {valor_base} + {original} = {resultado}")
        
        print(f"\nFinal result list: {resultados}")
        print("Test 2 completed successfully!")
        
    except (ValueError, EOFError):
        print("Error: Please enter a valid integer value.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

**Flujo de ejecución:**
1. Se solicita un valor base al usuario
2. Se crea una lista predefinida con 5 elementos: `[10, 20, 30, 40, 50]`
3. Se crea el closure llamando a `adder(valor_base)`
4. Se utiliza `map()` para aplicar la lambda a cada elemento de la lista
5. Se convierte el resultado de `map()` a una lista
6. Se muestran los resultados detalladamente

**Uso de `map()`:**
```python
resultados = list(map(suma_funcion, lista_numeros))
```
- `map()` aplica la función `suma_funcion` a cada elemento de `lista_numeros`
- Es equivalente a: `[suma_funcion(x) for x in lista_numeros]`
- Demuestra el uso de funciones de orden superior en programación funcional

---

## 4. Ejecución y Resultados

### 4.1 Ejemplo de Ejecución - Test 1

```
==================================================
PRUEBA 1: Suma con Entrada del Usuario
==================================================
Ingrese el primer valor entero: 15
Ingrese el segundo valor entero: 25

Resultado: 15 + 25 = 40
Prueba 1 completada exitosamente!
```

**Análisis:**
- El usuario ingresa 15 y 25
- El closure captura el valor 15
- La lambda suma 15 + 25 = 40
- El resultado se muestra correctamente

### 4.2 Ejemplo de Ejecución - Test 2

```
==================================================
PRUEBA 2: Entero + Elementos de Lista
==================================================
Ingrese un valor entero para sumar a la lista: 10

Lista de numeros: [10, 20, 30, 40, 50]

Valor base: 10
Resultados despues de sumar 10 a cada elemento:
  Posicion 0: 10 + 10 = 20
  Posicion 1: 10 + 20 = 30
  Posicion 2: 10 + 30 = 40
  Posicion 3: 10 + 40 = 50
  Posicion 4: 10 + 50 = 60

Lista de resultados final: [20, 30, 40, 50, 60]
Prueba 2 completada exitosamente!
```

**Análisis:**
- El usuario ingresa el valor base 10
- El closure captura este valor
- La lambda se aplica a cada elemento de la lista mediante `map()`
- Cada elemento se incrementa en 10
- La lista resultante es `[20, 30, 40, 50, 60]`

### 4.3 Manejo de Errores

**Caso 1: Input no numérico**
```
Ingrese el primer valor entero: abc
Error: Por favor ingrese valores enteros validos.
```

**Caso 2: Input vacío**
```
Ingrese el primer valor entero: 
Error: Por favor ingrese valores enteros validos.
```

---

## 5. Ejemplos Adicionales Implementados

Además del laboratorio principal, se creó el archivo `lambda_closures_examples.py` que contiene ejemplos demostrativos de diferentes usos de lambdas y closures:


## 5. Dificultades Encontradas y Soluciones

### 5.1 Manejo de Input Stream

**Problema:** Al ejecutar el programa con input simulado mediante pipes o redirección, se generaban errores de `EOFError`.

**Solución:** Se agregó el manejo de `EOFError` en los bloques try-except:
```python
except (ValueError, EOFError):
    print("Error: Por favor ingrese valores enteros validos.")
```

### 5.2 Limpieza de Input

**Problema:** Los inputs del usuario podían contener espacios en blanco al inicio o final.

**Solución:** Se aplicó el método `.strip()` antes de convertir a entero:
```python
valor1 = int(input_str.strip())
```
---

## 6. Análisis de Conceptos de Ingeniería de Software

### 6.1 Principios Aplicados

**1. Single Responsibility Principle (SRP)**
- Cada función tiene una responsabilidad única
- `adder()`: Crear el closure
- `test_user_input()`: Manejar el test con input del usuario
- `test_list_sum()`: Manejar el test con lista
- `main()`: Orquestar la ejecución

**2. DRY (Don't Repeat Yourself)**
- El closure `adder()` se reutiliza en ambos tests
- No se repite la lógica de suma
- El código es mantenible y escalable

**3. Error Handling**
- Manejo robusto de excepciones
- Mensajes de error claros para el usuario
- El programa no falla abruptamente

### 6.2 Patrones de Diseño

**1. Factory Pattern**
- `adder()` actúa como una factory que produce funciones especializadas
- Cada llamada a `adder()` crea una nueva función con diferente estado

**2. Strategy Pattern**
- Las lambdas permiten cambiar el comportamiento sin modificar el código
- Se pueden crear diferentes estrategias de suma

### 6.3 Programación Funcional

**Conceptos aplicados:**
1. **Funciones de orden superior:** `adder()` retorna una función
2. **Inmutabilidad:** Las variables capturadas no se modifican
3. **Composición de funciones:** Lambda dentro de closure
4. **Funciones puras:** La lambda no tiene efectos secundarios

---

## 7. Ventajas y Desventajas

### 7.1 Ventajas de Lambda + Closures

**Ventajas:**
1. **Código conciso:** Menos líneas de código para operaciones simples
2. **Encapsulación:** El estado se mantiene privado dentro del closure
3. **Flexibilidad:** Fácil crear múltiples funciones especializadas
4. **Sin variables globales:** Evita contaminación del namespace global
5. **Programación funcional:** Facilita el uso de `map()`, `filter()`, etc.

**Casos de uso ideales:**
- Callbacks y event handlers
- Funciones de transformación simples
- Configuración dinámica de comportamiento
- Decoradores
- Factories de funciones

### 7.2 Desventajas

**Limitaciones:**
1. **Legibilidad:** Resulto confuso
2. **Debugging:** Más difícil de depurar que funciones nombradas
3. **Restricciones de lambda:** Solo una expresión, no statements

---

## 8. Conclusiones

### 8.1 Conclusiones Técnicas

1. **Closures y Lambdas son herramientas poderosas:** Permiten escribir código más expresivo y conciso al combinar funciones de orden superior con encapsulación de estado.

2. **Programación funcional en Python:** Este laboratorio demuestra cómo Python soporta paradigmas funcionales, facilitando operaciones como `map()`, `filter()`, y `sorted()` con lambdas.

3. **Encapsulación sin clases:** Los closures proporcionan una alternativa ligera a las clases para mantener estado, especialmente útil para operaciones simples.

4. **Flexibilidad en el diseño:** La capacidad de crear funciones especializadas dinámicamente permite diseños más flexibles y mantenibles.

### 8.2 Aprendizajes Clave

1. **Scope y Lifetime:** Comprendimos cómo las variables capturadas permanecen accesibles incluso después de que la función externa termine.

2. **Funciones de Orden Superior:** Experimentamos directamente con funciones que retornan otras funciones y cómo esto se aplica en programación real.

3. **Composición de Conceptos:** Vimos cómo lambda y closures se complementan para crear soluciones elegantes.

4. **Manejo de Errores:** Implementamos error handling robusto para inputs del usuario.

### 8.3 Aplicaciones Prácticas

Este conocimiento es aplicable en:
- **Desarrollo web:** Callbacks en frameworks asíncronos
- **Procesamiento de datos:** Transformaciones con pandas y numpy
- **APIs:** Configuración de endpoints dinámicos
- **Decoradores:** Crear decoradores personalizados
- **Testing:** Mocks y stubs con comportamiento configurable

### 8.4 Mejores Prácticas Identificadas

1. Usar lambdas solo para operaciones simples de una línea
2. Preferir funciones nombradas cuando la lógica es compleja
3. Documentar closures con docstrings claros
4. Evitar capturar demasiadas variables en un closure

### 9.5 Reflexión Final

Este laboratorio nos permitió profundizar en conceptos avanzados de Python que son fundamentales en la programación moderna. Las expresiones lambda y los closures no son solo características del lenguaje, sino herramientas que, cuando se usan apropiadamente, pueden hacer nuestro código más estructurado y sostenible. La clave está en entender cuándo y cómo aplicarlas para obtener los mejores resultados.

---

## 10. Referencias

1. Python Official Documentation - Lambda Expressions: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
2. Python Official Documentation - Closures: https://docs.python.org/3/faq/programming.html#what-are-closures
3. CINVESTAV Guadalajara - Advanced Python Course Materials
4. Slides: "Part 4 - Advanced Python Functionalities - Lambda Expressions and Closures"
5. Real Python - Python Lambda Functions: https://realpython.com/python-lambda/
6. Real Python - Python Closures: https://realpython.com/inner-functions-what-are-they-good-for/

---

**Fin del Reporte**
