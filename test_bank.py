import pytest
from app import BankAccount  # Ajusta el nombre según el código real

class TestBankAccount:
    
    def setup_method(self):
        """Este método se ejecuta antes de cada prueba"""
        self.account = BankAccount()
    
    # Prueba 1: Saldo inicial
    def test_initial_balance(self):
        assert self.account.get_balance() == 0
    
    # Prueba 2: Depósito válido
    def test_deposit_valid(self):
        self.account.deposit(100)
        assert self.account.get_balance() == 100
    
    # Prueba 3: Depósito negativo
    def test_deposit_negative(self):
        with pytest.raises(ValueError, match="El depósito debe ser positivo"):
            self.account.deposit(50)
    
    # Prueba 4: Depósito cero
    def test_deposit_zero(self):
        with pytest.raises(ValueError, match="El depósito debe ser positivo"):
            self.account.deposit(0)
    
    # Prueba 5: Retiro válido
    def test_withdraw_valid(self):
        self.account.deposit(100)
        self.account.withdraw(30)
        assert self.account.get_balance() == 70
    
    # Prueba 6: Retiro con fondos insuficientes
    def test_withdraw_insufficient(self):
        self.account.deposit(100)
        with pytest.raises(ValueError, match="Fondos insuficientes"):
            self.account.withdraw(200)
    
    # Prueba 7: Retiro negativo
    def test_withdraw_negative(self):
        self.account.deposit(100)
        with pytest.raises(ValueError, match="El retiro debe ser positivo"):
            self.account.withdraw(-20)
    
    # Prueba 8: Múltiples operaciones
    def test_multiple_operations(self):
        self.account.deposit(50)
        self.account.deposit(30)
        self.account.withdraw(20)
        assert self.account.get_balance() == 60