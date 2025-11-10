# task_3.py
# Sección 1. Práctica de Programación
# Alejandro Campos Martínez
# Team 6

"""
Task 3: Crear una clase BankAccount con:
- Atributo de clase: bank = "Central Bank"
- Método de instancia: show_balance()
- Método de clase: show_bank()
- Método estático: convert_currency(value)
"""


class BankAccount:
    """
    Clase que representa una cuenta bancaria.
    
    Atributos de clase:
        bank (str): Nombre del banco (compartido por todas las cuentas)
    
    Atributos de instancia:
        owner (str): Nombre del titular de la cuenta
        balance (float): Saldo de la cuenta
    """
    
    # Atributo de clase
    bank = "Central Bank"
    
    def __init__(self, owner, balance=0.0):
        """
        Constructor de la clase BankAccount.
        
        Parámetros:
            owner (str): Nombre del titular de la cuenta
            balance (float): Saldo inicial de la cuenta. Valor por defecto: 0.0
        """
        self.owner = owner
        self.balance = balance
    
    def show_balance(self):
        """
        Método de instancia que muestra el saldo del cliente.
        
        Imprime el nombre del titular y su saldo actual.
        """
        print(f"Titular: {self.owner}")
        print(f"Saldo: ${self.balance:.2f}")
    
    @classmethod
    def show_bank(cls):
        """
        Método de clase que muestra el nombre del banco.
        
        Imprime el nombre del banco almacenado en el atributo de clase.
        """
        print(f"Banco: {cls.bank}")
    
    @staticmethod
    def convert_currency(value, exchange_rate=20.0):
        """
        Notas:
        Método estático que convierte dólares a pesos.
        
        Parámetros:
            value (float): Cantidad en dólares a convertir
            exchange_rate (float): Tipo de cambio. Valor por defecto: 20.0
        
        Retorna:
            float: Cantidad equivalente en pesos mexicanos
        """
        return value * exchange_rate


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 3: CLASE BANKACCOUNT - TRES TIPOS DE MÉTODOS")
    print("=" * 70)
    
    print("--- Creando cuenta bancaria ---")
    account = BankAccount("Juan Pérez", 5000.00)
    
    print("--- 1. Método de instancia: show_balance() ---")
    account.show_balance()
    
    print("--- 2. Método de clase: show_bank() ---")
    BankAccount.show_bank()
    
    print("--- 3. Método estático: convert_currency() ---")
    dolares = 100
    tipo_cambio = 20.0
    pesos = BankAccount.convert_currency(dolares, tipo_cambio)
    print(f"Conversión: ${dolares} USD = ${pesos:.2f} MXN")
    print(f"Tipo de cambio usado: {tipo_cambio}")
    
    print("--- Conversión adicional con tipo de cambio por defecto ---")
    dolares2 = 50
    pesos2 = BankAccount.convert_currency(dolares2)
    print(f"Conversión: ${dolares2} USD = ${pesos2:.2f} MXN")

