# task_7.py
# Seccion 2. Deteccion de Errores
# Alejandro Campos Martinez
# Team 6

"""
Se documenta un error de tipo (TypeError)
encontrado durante la practica con operaciones de NumPy.
"""

import numpy as np

print("=" * 70)
print("TASK 7: TypeError - Error de Tipo en Operaciones")
print("=" * 70)

# CODIGO CON ERROR:
"""
import numpy as np

# Crear array de NumPy
arr_np = np.array([1, 2, 3, 4, 5])
print(f"Array NumPy: {arr_np}")

# Crear lista de Python
list_py = [10, 20, 30, 40, 50]
print(f"Lista Python: {list_py}")

# Intentar sumar arrays de NumPy y Python (Error: tipos incompatibles)
result = arr_np + list_py
print(f"Resultado: {result}")
"""

# Error presentado:
"""
xandro@cresep-desktop:~/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9$ /usr/bin/python3 /home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_7.py
======================================================================
TASK 7: TypeError - Error de Tipo en Operaciones
======================================================================
Array NumPy: [1 2 3 4 5]
Lista Python: [10, 20, 30, 40, 50]
Resultado: [11 22 33 44 55]
Explicacion del error:
----------------------------------------------------------------------
Tipo de error: TypeError
Causa: Operaciones con tipos de datos incompatibles
Mensaje: TypeError: unsupported operand type(s) for...

Casos comunes de TypeError en NumPy:
1. Operaciones entre arrays y tipos no numericos
2. Funciones que esperan arrays pero reciben otros tipos
3. Operaciones matematicas con strings o None
4. Intentar indexar con tipos incorrectos

Soluciones:
1. Asegurar que todos los operandos sean arrays de NumPy
2. Convertir tipos con np.array() antes de operar
3. Verificar tipos con type() y isinstance()
4. Usar validacion de tipos en funciones
----------------------------------------------------------------------

Ejemplo de TypeError Real
----------------------------------------------------------------------
Array NumPy: [1 2 3 4 5]

TypeError capturado:
  ufunc 'add' did not contain a loop with signature matching types (dtype('int64'), dtype('<U5')) -> None

No se puede sumar un array numerico con un string

----------------------------------------------------------------------

Solucion 1: Convertir a tipos compatibles
----------------------------------------------------------------------
Array NumPy: [1 2 3 4 5], tipo: <class 'numpy.ndarray'>
Lista Python: [10, 20, 30, 40, 50], tipo: <class 'list'>

Convirtiendo lista a array:
list_as_array = np.array(list_py)
result = arr_np + list_as_array
Resultado: [11 22 33 44 55]

----------------------------------------------------------------------

Solucion 2: Validar tipos antes de operar
----------------------------------------------------------------------
Probando operaciones seguras:

[1,2,3] + [4,5,6] = [5 7 9]
[1,2,3] × 10 = [10 20 30]

Intentando operar con string:
Error: arr2 no es numerico (dtype: <U5)

----------------------------------------------------------------------

Solucion 3: Especificar dtype correcto
----------------------------------------------------------------------
Array int32: [1 2 3], dtype: int32
Array float64: [1.5 2.5 3.5], dtype: float64

Suma: [2.5 4.5 6.5]
Dtype resultante: float64 (promocionado a float)

Conversion explicita:
arr_int.astype(np.float64) = [1. 2. 3.]
Dtype: float64

======================================================================
CASO ESPECIAL: TypeError en Indexacion
======================================================================

Array: [0 1 2 3 4 5 6 7 8 9]
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/Module1_Team_6/Lab_9/Section_2/task_7.py", line 213, in <module>
    value = arr[2.5]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
"""

# Causa: Intentar operaciones con tipos incompatibles

print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: TypeError")
print("Causa: Operaciones con tipos de datos incompatibles")
print("Mensaje: TypeError: unsupported operand type(s) for...")
print()
print("Casos comunes de TypeError en NumPy:")
print("1. Operaciones entre arrays y tipos no numericos")
print("2. Funciones que esperan arrays pero reciben otros tipos")
print("3. Operaciones matematicas con strings o None")
print("4. Intentar indexar con tipos incorrectos")
print()
print("Soluciones:")
print("1. Asegurar que todos los operandos sean arrays de NumPy")
print("2. Convertir tipos con np.array() antes de operar")
print("3. Verificar tipos con type() y isinstance()")
print("4. Usar validacion de tipos en funciones")

print("-" * 70)

# CODIGO CORREGIDO - Error real con strings
print("\nEjemplo de TypeError Real")
print("-" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array NumPy: {arr}")

try:
    # Intentar sumar array con string (Error)
    result = arr + "texto"
    print(f"Resultado: {result}")
except TypeError as e:
    print(f"\nTypeError capturado:")
    print(f"  {e}")
    print(f"\nNo se puede sumar un array numerico con un string")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 1: Convertir tipos
print("\nSolucion 1: Convertir a tipos compatibles")
print("-" * 70)

# Mezclar lista de Python con array de NumPy
arr_np = np.array([1, 2, 3, 4, 5])
list_py = [10, 20, 30, 40, 50]

print(f"Array NumPy: {arr_np}, tipo: {type(arr_np)}")
print(f"Lista Python: {list_py}, tipo: {type(list_py)}")

# Convertir lista a array antes de operar
list_as_array = np.array(list_py)
result = arr_np + list_as_array

print(f"\nConvirtiendo lista a array:")
print(f"list_as_array = np.array(list_py)")
print(f"result = arr_np + list_as_array")
print(f"Resultado: {result}")

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 2: Validacion de tipos
print("\nSolucion 2: Validar tipos antes de operar")
print("-" * 70)

def safe_array_operation(arr1, arr2, operation='add'):
    """
    Realiza operaciones entre arrays de forma segura.
    
    Parametros:
        arr1: Primer operando
        arr2: Segundo operando
        operation: Tipo de operacion ('add', 'subtract', 'multiply')
    
    Retorna:
        Resultado de la operacion o None si hay error
    """
    # Convertir a arrays si no lo son
    if not isinstance(arr1, np.ndarray):
        try:
            arr1 = np.array(arr1)
        except (ValueError, TypeError):
            print(f"Error: No se puede convertir arr1 a array")
            return None
    
    if not isinstance(arr2, np.ndarray):
        try:
            arr2 = np.array(arr2)
        except (ValueError, TypeError):
            print(f"Error: No se puede convertir arr2 a array")
            return None
    
    # Verificar que son numericos
    if not np.issubdtype(arr1.dtype, np.number):
        print(f"Error: arr1 no es numerico (dtype: {arr1.dtype})")
        return None
    
    if not np.issubdtype(arr2.dtype, np.number):
        print(f"Error: arr2 no es numerico (dtype: {arr2.dtype})")
        return None
    
    # Realizar operacion
    if operation == 'add':
        return arr1 + arr2
    elif operation == 'subtract':
        return arr1 - arr2
    elif operation == 'multiply':
        return arr1 * arr2
    else:
        print(f"Error: Operacion '{operation}' no reconocida")
        return None

# Probar con diferentes tipos
print("Probando operaciones seguras:\n")

# Caso 1: NumPy array + lista
result1 = safe_array_operation([1, 2, 3], [4, 5, 6], 'add')
print(f"[1,2,3] + [4,5,6] = {result1}")

# Caso 2: NumPy array + numeros
result2 = safe_array_operation([1, 2, 3], 10, 'multiply')
print(f"[1,2,3] × 10 = {result2}")

# Caso 3: Intentar con string (falla de forma controlada)
print(f"\nIntentando operar con string:")
result3 = safe_array_operation([1, 2, 3], "texto", 'add')

print("\n" + "-" * 70)

# CODIGO CORREGIDO - Solucion 3: Usar dtype apropiado
print("\nSolucion 3: Especificar dtype correcto")
print("-" * 70)

# Error comun: mezclar tipos numericos incompatibles
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.5, 2.5, 3.5], dtype=np.float64)

print(f"Array int32: {arr_int}, dtype: {arr_int.dtype}")
print(f"Array float64: {arr_float}, dtype: {arr_float.dtype}")

# NumPy automaticamente promociona al tipo mas general
result = arr_int + arr_float
print(f"\nSuma: {result}")
print(f"Dtype resultante: {result.dtype} (promocionado a float)")

# Conversion explicita
arr_int_as_float = arr_int.astype(np.float64)
print(f"\nConversion explicita:")
print(f"arr_int.astype(np.float64) = {arr_int_as_float}")
print(f"Dtype: {arr_int_as_float.dtype}")

# Ejemplo de error con indexacion
print("\n" + "=" * 70)
print("CASO ESPECIAL: TypeError en Indexacion")
print("=" * 70)

arr = np.arange(10)
print(f"\nArray: {arr}")

try:
    # Intentar indexar con float (Error)
    value = arr[2.5]
    print(f"arr[2.5] = {value}")
except TypeError as e:
    print(f"\nTypeError al indexar con float:")
    print(f"  {e}")
    print(f"\nSolucion: Usar indices enteros")
    value = arr[int(2.5)]
    print(f"  arr[int(2.5)] = arr[2] = {value}")

print("\nIndices validos: int, np.int32, np.int64")
print("Indices invalidos: float, string, None")
