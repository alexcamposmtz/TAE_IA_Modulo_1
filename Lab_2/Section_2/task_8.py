# task_8_cronopios.py
# Alejandro Campos Martínez
# Explicación detallada de input() con ejemplos (tema: cronopios, famas y esperanzas)

"""
La función input() lee una línea desde el teclado y devuelve una cadena (str) sin el salto de línea.

Sintaxis:
    input(prompt=None) -> str

Parámetros:
- prompt (opcional): texto mostrado antes de leer.

Comportamiento:
- Bloquea la ejecución hasta que el usuario presione Enter.
- Siempre devuelve una cadena (tipo str).
- Para usar números, se debe convertir con int() o float().
- Puede lanzar:
    EOFError: si no hay entrada.
    KeyboardInterrupt: si el usuario interrumpe con Ctrl+C.

Buenas prácticas:
- Limpiar con .strip()
- Normalizar con .lower() o .upper()
- Validar y convertir con try/except
"""

# Ejemplo 1: Lectura simple
nombre = input("Registro de cronopios: escriba su nombre: ")
print("Cronopio registrado:", nombre)
print()

# Ejemplo 2: Conversión numérica
cajas_str = input("Famas: cantidad de cajas para archivar (entero): ")
try:
    cajas = int(cajas_str)
    print("Inventario:", cajas, "cajas asignadas a los famas.")
except ValueError:
    print("Entrada inválida: se esperaba un número entero.")
print()

# Ejemplo 3: Múltiples entradas
linea = input("Cronopios: anote tres objetos inútiles separados por comas: ")
objetos = [o.strip() for o in linea.split(",")]
if len(objetos) >= 3:
    print("Catálogo inútil:", objetos[0], ",", objetos[1], ",", objetos[2])
else:
    print("Formato inválido: se requieren al menos tres elementos.")
print()

# Ejemplo 4: Clasificador mínimo
tipo = input("Clasifique su temperamento (cronopio, fama, esperanza): ").strip().lower()
if tipo == "cronopio":
    print("Resultado: desorden jubiloso autorizado.")
elif tipo == "fama":
    print("Resultado: control y etiquetas alfabéticas.")
elif tipo == "esperanza":
    print("Resultado: calma y espera razonable.")
else:
    print("Resultado: indeterminado.")
print()

# Ejemplo 5: Valor por defecto simulado
alias = input("Alias de cronopio (Enter para 'anónimo'): ").strip()
alias = alias or "anónimo"
print("Alias confirmado:", alias)
print()

# Ejemplo 6: Bucle con validación
while True:
    print("Menú de famas: 1) Sumar  2) Restar  3) Salir")
    op = input("Opción (1-3): ").strip()
    if op in {"1", "2"}:
        a = input("a = ").strip()
        b = input("b = ").strip()
        try:
            a, b = float(a), float(b)
            res = a + b if op == "1" else a - b
            print("Resultado:", res)
        except ValueError:
            print("Error: números inválidos.")
    elif op == "3":
        print("Menú cerrado por un fama.")
        break
    else:
        print("Opción inválida.")
    print()

# Ejemplo 7: Manejo de EOF y Ctrl+C
try:
    prueba = input("Ensayo de robustez (Ctrl+D/Ctrl+Z = EOF, Ctrl+C = cancelar): ")
    print("Leído:", prueba)
except EOFError:
    print("EOF: sin entrada disponible.")
except KeyboardInterrupt:
    print("Interrumpido por el usuario.")
print()

# Ejemplo 8: map() con split
medidas = input("Esperanzas: ingrese tres medidas separadas por espacios: ").split()
try:
    x, y, z = map(float, medidas[:3])
    print("Suma de medidas:", x + y + z)
except Exception:
    print("Ingrese al menos tres números válidos.")
print()

print("==========================================================================================")
print("PUNTOS CLAVE:")
print("- input() bloquea hasta que el usuario presiona Enter y siempre devuelve una cadena.")
print("- Para usar números, convierta con int() o float().")
print("- .strip() y .lower() ayudan a limpiar y normalizar la entrada.")
print("- split() y map() permiten procesar varios valores a la vez.")
print("- Es posible manejar EOFError y KeyboardInterrupt para mayor control.")
print()

print("Referencia:")
print("Cortázar, J. (2013). Historias de cronopios y de famas. Alfaguara.")

