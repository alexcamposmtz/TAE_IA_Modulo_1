# Lab 6: Programación Orientada a Objetos I

**Curso:** Talento Altamente Especializado – Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:** Cristian Torres González  
**Equipo:** Team 6
- Alejandro Campos Martínez


**Fecha de asignación:** 20/10/2025  
**Fecha de entrega:** 27/10/2025

---

## Descripción del Laboratorio

Este laboratorio introduce los conceptos fundamentales de **Programación Orientada a Objetos (POO)** en Python, incluyendo:
- Creación de clases y objetos
- Constructores (`__init__`)
- Métodos de instancia, métodos de clase y métodos estáticos
- Atributos de clase y atributos de instancia

---

## Estructura del Laboratorio

```
Lab6/
├── README.md
├── section_1/
│   ├── task_1.py    # Clase Car
│   ├── task_2.py    # Clase Person
│   └── task_3.py    # Clase BankAccount
└── section_2/
    ├── task_4.py    # SyntaxError
    ├── task_5.py    # TypeError
    ├── task_6.py    # AttributeError
    └── task_7.py    # NameError
```

---

## Sección 1: Práctica de Programación

### Task 1: Clase Car
Implementación de una clase `Car` con los atributos:
- `brand` (marca)
- `model` (modelo)
- `color` (color)

Incluye el método `show_info()` que muestra la información completa del coche.

**Ejecución:**
```bash
python3 section_1/task_1.py
```

**Ejemplo de salida:**
```
======================================================================
TASK 1: CLASE CAR - INFORMACIÓN DE COCHES
======================================================================

--- Creando primer coche ---
Automóvil: Toyota Corolla
Color: Rojo

--- Creando segundo coche ---
Automóvil: Honda Civic
Color: Azul
```

### Task 2: Clase Person
Implementación de una clase `Person` con constructor que recibe:
- `name` (nombre)
- `age` (edad)
- `city` (ciudad)

Incluye el método `greet()` que muestra un saludo personalizado.

**Ejecución:**
```bash
python3 section_1/task_2.py
```

**Ejemplo de salida:**
```
--- Creando primera persona ---
Hola, mi nombre es Ana, tengo 25 años y vivo en México.

--- Creando segunda persona ---
Hola, mi nombre es Carlos, tengo 30 años y vivo en Guadalajara.
```

### Task 3: Clase BankAccount
Implementación de una clase `BankAccount` que demuestra los **tres tipos de métodos** en Python:

1. **Atributo de clase:** `bank = "Central Bank"`
2. **Método de instancia:** `show_balance()` - muestra el saldo del cliente
3. **Método de clase:** `show_bank()` - muestra el nombre del banco
4. **Método estático:** `convert_currency(value)` - convierte dólares a pesos

**Ejecución:**
```bash
python3 section_1/task_3.py
```

**Conceptos demostrados:**
- **Método de instancia:** Trabaja con datos específicos del objeto (`self`)
- **Método de clase:** Trabaja con atributos de la clase (`cls`, `@classmethod`)
- **Método estático:** Función independiente que no accede a la clase ni al objeto (`@staticmethod`)

---

## Sección 2: Detección de Errores

Esta sección documenta **cuatro tipos de errores** encontrados durante la práctica de POO, siguiendo el formato establecido en laboratorios anteriores.

### Task 4: SyntaxError
**Error:** Falta el símbolo `:` al final de la definición de un método.

```python
def show_info(self)  # ← Error: falta ':'
```

**Mensaje de error:**
```
SyntaxError: expected ':'
```

**Causa:** En Python, todas las definiciones (`def`, `class`, `if`, `for`, etc.) deben terminar con dos puntos.

**Solución:** Agregar `:` al final de la línea.

**Ejecución:**
```bash
python3 section_2/task_4.py
```

---

### Task 5: TypeError
**Error:** Falta pasar argumentos requeridos al crear un objeto.

```python
person = Person("Ana", 25)  # ← Error: falta 'city'
```

**Mensaje de error:**
```
TypeError: Person.__init__() missing 1 required positional argument: 'city'
```

**Causa:** El constructor `__init__` requiere 3 argumentos (`name`, `age`, `city`) pero solo se pasaron 2.

**Soluciones:**
1. Pasar todos los argumentos requeridos
2. Usar valores por defecto en el constructor
3. Usar `*args` o `**kwargs` para argumentos variables

**Ejecución:**
```bash
python3 section_2/task_5.py
```

---

### Task 6: AttributeError
**Error:** Intentar acceder a un atributo que no existe en el objeto.

```python
print(account.account_number)  # ← Error: atributo no definido
```

**Mensaje de error:**
```
AttributeError: 'BankAccount' object has no attribute 'account_number'
```

**Causa:** El atributo `account_number` no fue definido en el constructor `__init__`.

**Soluciones:**
1. Definir el atributo en `__init__`
2. Usar `hasattr()` para verificar existencia
3. Usar `getattr()` con valor por defecto

**Ejecución:**
```bash
python3 section_2/task_6.py
```

---

### Task 7: NameError (manifestado como AttributeError)
**Error:** Intentar usar un atributo sin haberlo inicializado.

```python
def show_info(self):
    print(f"Año: {self.year}")  # ← Error: 'year' no inicializado
```

**Mensaje de error:**
```
AttributeError: 'Car' object has no attribute 'year'
```

**Causa:** Se intenta usar `self.year` en un método pero nunca se inicializó en `__init__`.

**Soluciones:**
1. Agregar el atributo al constructor
2. Usar valor por defecto si es opcional
3. Verificar existencia con `hasattr()` antes de usar

**Ejecución:**
```bash
python3 section_2/task_7.py
```

---

## Ejecución del Laboratorio

### Ejecutar todas las tareas de la Sección 1:
```bash
cd Lab6
python3 section_1/task_1.py
python3 section_1/task_2.py
python3 section_1/task_3.py
```

### Ejecutar todas las tareas de la Sección 2:
```bash
python3 section_2/task_4.py
python3 section_2/task_5.py
python3 section_2/task_6.py
python3 section_2/task_7.py
```

### Ejecutar todo el laboratorio:
```bash
python3 verificar_lab.py
```

---

## Conceptos Clave Aprendidos

### 1. Programación Orientada a Objetos
- **Clase:** Plantilla para crear objetos
- **Objeto:** Instancia de una clase
- **Atributos:** Datos que pertenecen a un objeto
- **Métodos:** Funciones que pertenecen a una clase

### 2. Constructor `__init__`
- Se ejecuta automáticamente al crear un objeto
- Inicializa los atributos del objeto
- Recibe `self` como primer parámetro

### 3. El parámetro `self`
- Representa la instancia actual del objeto
- Se usa para acceder a atributos y métodos de la instancia
- Se pasa automáticamente (no es necesario incluirlo al llamar)

### 4. Tipos de Métodos
- **Método de instancia:** Accede a `self` (datos del objeto)
- **Método de clase (`@classmethod`):** Accede a `cls` (datos de la clase)
- **Método estático (`@staticmethod`):** No accede ni a `self` ni a `cls`

### 5. Atributos
- **Atributos de instancia:** Únicos para cada objeto (definidos con `self`)
- **Atributos de clase:** Compartidos por todos los objetos (definidos en la clase)

---

## Errores presentados en POO

1. **Olvidar `self`** en la definición de métodos
2. **Olvidar `self.`** al acceder a atributos
3. **No inicializar atributos** en `__init__`
4. **Pasar argumentos incorrectos** al constructor
5. **Olvidar los dos puntos** (`:`) en definiciones

---

## Notas

**Siempre inicializar todos los atributos en `__init__`**  
**Usar docstrings para documentar clases y métodos**  
**Nombrar clases con CamelCase:** `BankAccount`, `Person`  
**Nombrar métodos y atributos con snake_case:** `show_info`, `account_number`  
**Verificar tipos de argumentos cuando sea necesario**  
**Usar valores por defecto para atributos opcionales**

---

## Recursos Adicionales

- [Documentación oficial de Python - Clases](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Python OOP Tutorial](https://www.w3schools.com/python/python_classes.asp)

---


**Team 6**  
Octubre 2025
