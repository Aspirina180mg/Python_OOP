"""crea una cuenta bancaria con atributos y módulos desde bank_account
y le hace un depósito, mostrando finalmente el balance de la misma, demostrando
el encapsulamiento"""

from bank_account import BankAccount

# para mayor información sobre un módulo:
# import bank_account
# help(bank_account)

cuenta = BankAccount("Alice", 1000)
cuenta.deposit(234)
print(cuenta.get_balance())
# print(cuenta.__balance) # no funcionaría porque __balance es privado
