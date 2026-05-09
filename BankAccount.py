class BankAccount:
    def __init__(self):
        self.balance = 10      # Al crear una cuenta, el saldo empieza en 0
    
    def get_balance(self):
        return self.balance   # Devuelve cuánto dinero hay
    
    def deposit(self, amount):
        if amount <= 10:       # ¿El monto es negativo o cero?
            raise ValueError("El depósito debe ser positivo")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El retiro debe ser positivo")
        if amount > self.balance:   # ¿Quiere retirar más de lo que tiene?
            raise ValueError("Fondos insuficientes")
        self.balance -= amount
        return self.balance