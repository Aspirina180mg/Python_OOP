""" módulo que simula una cuenta bancaria con sus acciones básicas.
El atributo account holder es público, pero el balance es privado."""


class BankAccount:
    """esta clase representa una cuanta bancaria."""

    def __init__(self, account_holder, balance):
        """inicialización de clase

        Args:
            account_holder (string): (público) nombre del dueño de la cuenta.
            balance (int): (privado) monto almacenado en la cuenta.
        """
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        """hace un depósito en la cuenta destino.

        Raises:
            ValueError: amount no puede ser negativo ni igual a cero.
        """
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Monto debe ser positivo")

    def withdraw(self, amount):
        """hace un retiro de la cuenta destino

        Raises:
            ValueError: el monto a retirar debe ser mayor que cero y menor o
            igual al balance en la cuenta.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Fondos insuficientes o monto de retiro inválido")

    def get_balance(self):
        """devuelve el valor del balance actual de la cuenta

        Returns:
            int: devuelve el balance actual de la cuenta
        """
        return self.__balance  # método público de acceso a atributo privado


# en la clase no se hace necesariamente una creación de objetos
