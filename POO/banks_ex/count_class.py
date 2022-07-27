from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, nome, saldo):
        self.agencia = agencia
        self.numero = numero
        self.nome = nome
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass


class Conta_corrente(Conta):
    def __init__(self, agencia, numero, nome, saldo, limite=200):
        super().__init__(agencia, numero, nome, saldo)
        self.__limite = limite
        self.__saldo = saldo


def sacar(self, valor):
    if valor > self.__saldo + self.__limite:
        print('Saldo insuficiente')
    else:
        self.__saldo -= valor
        print('Saque realizado')
    self.exibir_saldo()


def exibir_saldo(self):
    print(f'{self.nome}, o seu saldo é de {self.__saldo}')


class Conta_poupanca(Conta):
    def __init__(self, agencia, numero, nome, saldo):
        super().__init__(agencia, numero, nome, saldo)
        self.__saldo = saldo

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente')
        else:
            self.__saldo -= valor
            print('Saque realizado')
        self.exibir_saldo()

    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de {self.__saldo}')



#
# from abc import ABC, abstractmethod
#
#
# class Count(ABC):
#     def __init__(self, name, agency, number, owner, balance=0):
#         self.name = name
#         self.agency = agency
#         self.number = number
#         self.owner = owner
#         self.__balance = balance
#
#     def deposit(self, value):
#         self.__balance += value
#
#     @abstractmethod
#     def withdraw(self, value):
#         pass
#
#     def show_balance(self):
#         pass
#         print(f'{self.name}, your balance is {self.__balance:.2f}')
#
#
# class Checking_Account(Count):
#     def __init__(self, name, agency, number, owner, balance, limit=200):
#         super().__init__(name, agency, number, owner, balance)
#         self.__limit = limit
#         self.balance = balance
#
#     def withdraw(self, value):
#         if value > self.__balance + self.__limit:
#             print('the balance is not enough')
#         else:
#             self.__balance -= value
#             print('withdraw done')
#
#
# class Savings_Account(Count):
#     def __init__(self, name, agency, number, owner, balance):
#         super().__init__(name, agency, number, owner, balance)
#         self.balance = balance
#
#     def withdraw(self, value):
#         if value > self.__balance:
#             print('the balance is not enough')
#         else:
#             self.__balance -= value
#             print('withdraw done')
#
#
# c1 = Savings_Account('cairo', 1234, 2, 'cairo', 1000)
# c1.withdraw(200)

