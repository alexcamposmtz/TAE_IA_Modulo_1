# Lab 7: Programación Orientada a Objetos II-IV

**Curso:** Talento Altamente Especializado – Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Cristian Torres González  
**Equipo:** Team 6
- Alejandro Campos Martínez

**Fecha de asignación:** 31/10/2025  
**Fecha de entrega:** 10/11/2025

---

## Descripción del Laboratorio

Este laboratorio cubre conceptos avanzados de **Programación Orientada a Objetos (POO)** en Python, incluyendo:
- Herencia simple y múltiple
- Polimorfismo
- Composición
- Métodos especiales (dunder methods)
- Detección y corrección de errores

---

## Estructura del Laboratorio

```
Lab_7/
├── README.md
├── Section_1/
│   ├── task_1.py    # Herencia
│   ├── task_2.py    # Herencia Múltiple
│   ├── task_3.py    # Polimorfismo
│   ├── task_4.py    # Composición
│   └── task_5.py    # Métodos Especiales
└── Section_2/
    ├── task_6.py    # AttributeError
    ├── task_7.py    # TypeError
    └── task_8.py    # IndexError
```

---

## Sección 1: Práctica de Programación

### Task 1: Herencia
Implementación de herencia simple con las clases `Employee` y `Manager`.

**Características:**
- Clase base `Employee` con atributos `name` y `salary`
- Método `show_info()` para mostrar información del empleado
- Clase derivada `Manager` que hereda de `Employee`
- Atributo adicional `department` en `Manager`
- Sobrescritura del método `show_info()` para incluir el departamento

**Ejemplo de salida:**
```
======================================================================
TASK 1: HERENCIA - EMPLOYEE Y MANAGER
======================================================================

--- Creando empleado ---
Nombre: Juan Perez
Salario: $25,000.00

--- Creando gerente ---
Nombre: Maria Rodriguez
Salario: $45,000.00
Departamento: Ventas
```

---

### Task 2: Herencia Múltiple
Implementación de herencia múltiple con las clases `Accountant`, `Technician` y `Boss`.

**Características:**
- Clase `Accountant` con método `generate_report()`
- Clase `Technician` con método `repair_machine()`
- Clase `Boss` que hereda de ambas clases
- Demostración del uso de métodos heredados de múltiples clases padre

**Ejemplo de salida:**
```
======================================================================
TASK 2: HERENCIA MULTIPLE - ACCOUNTANT, TECHNICIAN, BOSS
======================================================================

--- Creando jefe con herencia multiple ---
Jefe: Roberto Sanchez
Capacidades: Contabilidad y Tecnicas

--- Probando metodo heredado de Accountant ---
Generating financial report

--- Probando metodo heredado de Technician ---
Repairing machine
```

---

### Task 3: Polimorfismo
Implementación de polimorfismo con diferentes tipos de empleados y cálculo de pagos.

**Características:**
- Función `calculate_payment(worker)` que funciona con diferentes tipos
- Clase `FullTimeEmployee` con salario mensual fijo
- Clase `HourlyEmployee` con pago por horas trabajadas
- Clase `FreelanceEmployee` con pago por proyectos
- Cada clase tiene su propia implementación del método `payment()`


**Conceptos demostrados:**
- **Polimorfismo:** Mismo método, diferentes comportamientos
- **Duck typing:** "Si camina como pato y hace cuac como pato, es un pato"
- **Interfaces implícitas:** No se requiere herencia para el polimorfismo en Python

---

### Task 4: Composición
Implementación de composición con las clases `Engine` y `Car`.

**Características:**
- Clase `Engine` con método `start()` y atributos del motor
- Clase `Car` que contiene un objeto `Engine` como atributo
- Relación "has-a" (Car HAS-A Engine)
- Método `start_car()` que utiliza el motor interno para arrancar

**Ejecución:**
```bash
python3 Section_1/task_4.py
```

**Ejemplo de salida:**
```
--- Creando automovil 1 con motor V8 ---
Automovil: Ford Mustang
Motor: V8
Potencia: 450 HP

--- Arrancando automovil 1 ---
Arrancando Ford Mustang...
Engine started
```

**Conceptos demostrados:**
- **Composición vs. Herencia:** "has-a" vs. "is-a"
- **Diseño modular:** Separación de responsabilidades
- **Reutilización:** El mismo motor puede usarse en diferentes coches

---

### Task 5: Métodos Especiales
Implementación de métodos especiales (dunder methods) con la clase `Book`.

**Características:**
- Clase `Book` con atributos `title` y `num_pages`
- Método `__str__()` para representación legible del objeto
- Método `__len__()` para obtener el número de páginas con `len()`
- Método `__repr__()` para representación técnica del objeto

**Ejecución:**
```bash
python3 Section_1/task_5.py
```

**Ejemplo de salida:**
```
Usando print() que internamente llama a __str__():
Book: Cien Anos de Soledad, Pages: 417

Usando len() que internamente llama a __len__():
El libro tiene 417 paginas

Libro mas largo:
  Book: Don Quijote de la Mancha, Pages: 863
```

**Conceptos demostrados:**
- **Métodos mágicos:** Personalización del comportamiento de objetos
- **Integración con Python:** Usar funciones built-in como `print()` y `len()`
- **Convenios:** `__str__()` para usuarios, `__repr__()` para desarrolladores

---

## Sección 2: Detección de Errores

Esta sección documenta **tres tipos de errores** encontrados durante la práctica de POO avanzada, siguiendo el formato establecido en laboratorios anteriores.

### Task 6: AttributeError
**Error:** Intentar acceder a un atributo que no existe en un objeto.

```python
def show_info(self):
    print(f"Grado: {self.grade}")  # ← Error: self.grade no existe
```

**Mensaje de error:**
```
AttributeError: 'Student' object has no attribute 'grade'
```

**Causa:** El atributo `grade` no fue definido en el constructor `__init__` de la clase.

**Soluciones:**
1. Agregar el atributo en el constructor
2. Usar valores por defecto para atributos opcionales
3. Validar existencia con `hasattr()` antes de acceder

**Ejecución:**
```bash
python3 Section_2/task_6.py
```

---

### Task 7: TypeError
**Error:** Intentar realizar operaciones matemáticas con tipos de datos incompatibles.

```python
final_price = product.apply_discount("20")  # ← Error: string en vez de número
```

**Mensaje de error:**
```
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

**Causa:** Se pasó un string `"20"` cuando se esperaba un número para realizar la división.

**Soluciones:**
1. Pasar el argumento con el tipo correcto (número)
2. Convertir el tipo dentro del método usando `float()` o `int()`
3. Validar y manejar errores con `try-except`


### Task 8: IndexError
**Error:** Intentar acceder a un índice que está fuera del rango de una lista.

```python
for i in range(len(self.students) + 1):  # ← Error: +1 genera índice extra
    print(f"{i + 1}. {self.students[i]}")
```

**Mensaje de error:**
```
IndexError: list index out of range
```

**Causa:** El bucle genera un índice adicional (3) para una lista de 3 elementos (índices 0, 1, 2).

**Soluciones:**
1. Usar `range(len(self.students))` sin el `+1`
2. Iterar directamente sobre elementos con `enumerate()`
3. Validar índices antes de acceder a la lista

**Ejecución:**
```bash
python3 Section_2/task_8.py
```

## Conceptos Clave Aprendidos

### 1. Herencia simple
- **Clase base (padre):** Define atributos y métodos comunes
- **Clase derivada (hija):** Hereda y puede extender/modificar comportamiento
- **`super()`:** Llama métodos de la clase padre
- **Method overriding:** Sobrescribir métodos heredados

### 2. Herencia múltiple
- Una clase puede heredar de múltiples clases padre
- **Method Resolution Order (MRO):** Orden de búsqueda de métodos
- Usar `ClassName.__mro__` para ver el orden de resolución
- Cuidado con el "problema del diamante"

### 3. Polimorfismo
- **Mismo nombre de método, diferentes implementaciones**
- Duck typing: "Si se ve como un pato y hace cuac como un pato, es un pato"
- No requiere herencia en Python
- Permite código más flexible y reutilizable

### 4. Composición
- **"Has-a" relationship:** Un objeto contiene otro objeto
- Alternativa a la herencia
- Mayor flexibilidad y menor acoplamiento
- **Principio:** "Favor composition over inheritance"

### 5. Métodos especiales (Dunder Methods)
- **`__init__()`:** Constructor del objeto
- **`__str__()`:** Representación legible para usuarios
- **`__repr__()`:** Representación técnica para desarrolladores
- **`__len__()`:** Define comportamiento de `len()`
- Muchos otros: `__add__`, `__eq__`, `__getitem__`, etc.

---

## Errores comunes presentados en POO avanzada

1. **Olvidar llamar `super().__init__()`** en clases derivadas
2. **Confundir composición con herencia** (usar una cuando se necesita la otra)
3. **No inicializar atributos** antes de usarlos
4. **Errores de tipo** al pasar argumentos a métodos
5. **Acceder a índices fuera de rango** en listas

---

## Notas Importantes

**Herencia vs. Composición:**  
- Usa herencia para relaciones "is-a" (un Manager ES UN Employee)
- Usa composición para relaciones "has-a" (un Car TIENE UN Engine)

**Polimorfismo:**  
- No requiere herencia en Python (duck typing)
- Facilita el diseño de interfaces flexibles

**Métodos Especiales:**  
- Hacen que objetos personalizados se comporten como tipos nativos
- Mejoran la integración con el ecosistema de Python

**Buenas Prácticas:**  
- Documentar clases y métodos con docstrings
- Inicializar todos los atributos en `__init__()`
- Preferir composición sobre herencia cuando sea posible
- Validar tipos de entrada en métodos críticos

---

## Recursos Adicionales

- [Documentación oficial de Python - Clases](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- Slides del curso: OOP II, III y IV

---

**Team 6**  
Noviembre 2025
