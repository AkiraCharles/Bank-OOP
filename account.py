# ABC for creating different types of accounts
from abc import ABC, abstractmethod

# Custom Exception
class AbortProcess(Exception):

    """This exception is raised to abort a bank transaction"""

    pass


class Account(ABC):
    def __init__(self, name, balance, type, password):

        self.name = name
        self.balance = self.validateAmount(balance)
        self.type = type
        self.password = password

    def validateAmount(self, amount):

        try:
            amount = int(amount)
        except ValueError:
            raise AbortProcess("Aount must be an integer")
        if amount < 0:
            raise AbortProcess("Amount must be a positive integer")
        return amount

    def checkPasswordCorrect(self, password):

        if self.password != self.password:
            raise AbortProcess("Password for this account is incorrect!")

    def depositFunds(self, depositAmount):

        depositAmount = self.validateAmount(depositAmount)
        self.balance = self.balance + depositAmount
        return self.balance

    def withdrawFunds(self, withdrawAmount):

        withdrawAmount = self.validateAmount(withdrawAmount)
        if withdrawAmount > self.balance:
            raise AbortProcess("Not enough funds in account to complete withdrawal")
        self.balance = self.balance - withdrawAmount
        return self.balance

    def getBalance(self):
        return self.balance

    def __str__(self):
        return ("Name: ") + str(self.name) + (", Balance: ") + ("$") + str(self.balance)


class BusinessAccount(Account):
    def __init__(self, name, balance, type, password):

        super().__init__(name, balance, type, password)


class SavingsAccount(Account):
    def __init__(self, name, balance, type, password):

        super().__init__(name, balance, type, password)


class CheckingAccount(Account):
    def __init__(self, name, balance, type, password):

        super().__init__(name, balance, type, password)

