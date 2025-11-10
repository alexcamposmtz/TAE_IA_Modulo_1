# task_6.py
# Sección 2. Detección de Errores
# Alejandro Campos Martínez
# Team 6

"""
Se documenta un error de atributo (AttributeError)
encontrado durante la práctica.
"""

print("=" * 70)
print("TASK 6: AttributeError - Error de Atributo")
print("=" * 70)

# CODIGO CON ERROR:
"""
class BankAccount:
    bank = "Central Bank"
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def show_balance(self):
        print(f"Saldo: ${self.balance:.2f}")

account = BankAccount("Juan", 1000)
account.show_balance()

# Intentar acceder a un atributo que no existe
print(account.account_number)  # Este atributo no fue definido
"""

# Error presentado:
"""
Traceback (most recent call last):
  File "/home/xandro/Certificacion/IA/Modulo_1/Labs/TAE_IA_Modulo_1/Lab_6/section_2/task_6.py", line 18
    print(account.account_number)
          ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'BankAccount' object has no attribute 'account_number'
"""

# Causa: Intentar acceder a un atributo que no existe en el objeto


print("Explicacion del error:")
print("-" * 70)
print("Tipo de error: AttributeError")
print("Causa: Intentar acceder a 'account_number' que no fue definido")
print("Mensaje: AttributeError: 'BankAccount' object has no attribute 'account_number'")
print("Este error ocurre cuando:")
print("- Accedemos a un atributo que no existe")
print("- Escribimos mal el nombre de un atributo (typo)")
print("- Olvidamos inicializar un atributo en __init__()")
print("Soluciones:")
print("1. Verificar que el atributo esté definido en __init__()")
print("2. Revisar la ortografía del nombre del atributo")
print("3. Usar hasattr() para verificar si existe antes de acceder")

print("-" * 70)

# CODIGO CORREGIDO - Opción 1: Definir el atributo en __init__
print("Solución 1 - Agregar el atributo faltante en __init__:")

class BankAccount:
    """Clase que representa una cuenta bancaria"""
    
    bank = "Central Bank"
    
    def __init__(self, owner, balance, account_number=None):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number if account_number else "N/A"
    
    def show_balance(self):
        print(f"Titular: {self.owner}")
        print(f"Número de cuenta: {self.account_number}")
        print(f"Saldo: ${self.balance:.2f}")

account1 = BankAccount("Juan", 1000, "123456")
account1.show_balance()
print(f"Número de cuenta: {account1.account_number}")  # ← Ahora funciona

# CODIGO CORREGIDO - Opción 2: Usar hasattr() para verificar
print("Solución 2 - Verificar existencia del atributo con hasattr():")

class BankAccountSafe:
    """Clase BankAccount con verificación de atributos"""
    
    bank = "Central Bank"
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def get_account_info(self):
        print(f"Titular: {self.owner}")
        print(f"Saldo: ${self.balance:.2f}")
        
        # Verificar si existe el atributo antes de acceder
        if hasattr(self, 'account_number'):
            print(f"Número de cuenta: {self.account_number}")
        else:
            print("Número de cuenta: No asignado")

account2 = BankAccountSafe("María", 2000)
account2.get_account_info()

# Agregar el atributo dinámicamente
account2.account_number = "789012"
print("Después de agregar account_number:")
account2.get_account_info()

# CODIGO CORREGIDO - Opción 3: Usar getattr() con valor por defecto
print("Solución 3 - Usar getattr() con valor por defecto:")

class BankAccountFlexible:
    """Clase BankAccount flexible"""
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account3 = BankAccountFlexible("Carlos", 1500)

# getattr(objeto, 'atributo', valor_por_defecto)
account_num = getattr(account3, 'account_number', 'Sin asignar')
print(f"Número de cuenta: {account_num}")