# ATM class for managing account objects

from account import *


class Bank:
    def __init__(
        self, name, address, hours,
    ):

        self.bankAccounts = {}
        self.nextaccountNumber = 0
        self.name = name
        self.address = address
        self.hours = hours

    def createBankAccount(self, clientName, amount, accountType, password):

        creating = True
        while creating:

            print()
            print("***Creating New Bank Account***")
            print("Select Account Type: ")
            print("For a Business Account: press 'b'.")
            print("For a Checking Account: press 'c'.")
            print("For a Savingss Account: press 's'.")

            action = input("Select Account Type: ")
            action = action[0].lower()

            try:
                if action == "b":
                    newAccount = BusinessAccount(
                        clientName, amount, accountType, password
                    )
                    newAccountNumber = self.nextaccountNumber
                    self.bankAccounts[newAccountNumber] = newAccount
                    # Increment account number to prepare for a new account to be created
                    self.nextaccountNumber = self.nextaccountNumber + 1
                    return newAccountNumber
                    break

                if action == "c":
                    newAccount = CheckingAccount(
                        clientName, amount, accountType, password
                    )
                    newAccountNumber = self.nextaccountNumber
                    self.bankAccounts[newAccountNumber] = newAccount
                    # Increment account number to prepare for a new account to be created
                    self.nextaccountNumber = self.nextaccountNumber + 1
                    return newAccountNumber
                    break

                if action == "s":
                    newAccount = SavingsAccount(
                        clientName, amount, accountType, password
                    )
                    newAccountNumber = self.nextaccountNumber
                    self.bankAccounts[newAccountNumber] = newAccount
                    # Increment account number to prepare for a new account to be created
                    self.nextaccountNumber = self.nextaccountNumber + 1
                    return newAccountNumber
                    break

            except AbortProcess as error:
                print(error)

    def openAccount(self):
        print("***Open Bank Account***")
        userName = input("What is the name of the account holder?")
        startingBalance = int(input("What is the starting balance of the account?"))
        accountType = input("What type of account is it: ")
        setPassword = input("Please set a password: ")
        userAccountNumber = self.createBankAccount(
            userName, startingBalance, accountType, setPassword
        )
        print("Your new Account Number is: ", userAccountNumber)

    def closeBankAccount(self):
        print("***Close Bank Account***")
        account = self.getUserAccount()
        self.validatePassword(account)
        accountBalance = account.getbalance()
        print("You had a balance of", accountBalance, "which is being returned to you.")
        del account
        print("Your Bank Account has been deleted.")

    def validateAccountNumber(self):
        try:
            accountNumber = int(input("What is your account number: "))
        except ValueError:
            raise AbortProcess("Account Number must be an integer.")
        if accountNumber not in self.bankAccounts:
            raise AbortProcess("There is no account number: " + str(accountNumber))
        return accountNumber

    def validatePassword(self, userAccount):
        password = input("Please enter your password: ")
        userAccount.checkPasswordCorrect(password)

    def getUserAccount(self):
        accountNumber = self.validateAccountNumber()
        userAccount = self.bankAccounts[accountNumber]
        self.validatePassword(userAccount)
        return userAccount

    def deposit(self):
        print("***Making a deposit***")
        user = self.getUserAccount()
        depositamount = input("How much would you like to deposit: ")
        balance = user.deposit(depositamount)
        print("Deposited: ", depositamount)
        print("Your new balance is: ", balance)

    def withdraw(self):
        print("***Making a withdrawal***")
        user = self.getUserAccount()
        withdrawalamount = input("How much would you like to deposit: ")
        balance = user.withdraw(withdrawalamount)
        print("Deposited: ", withdrawalamount)
        print("Your new balance is: ", balance)

    def balance(self):
        print("***Get your balance***")
        user = self.getUserAccount()
        balance = user.getBalance()
        print("Your current balance is: ", balance)

    def showInfo(self):
        print("**Account Information: ")
        user = self.getUserAccount()
        print(user)

    def bankInfo(self):
        print("Bank: ", self.name)
        print("Address: ", self.address)
        print("Opening Hours: ", self.hours)

    def adminPermission(self):
        for account in self.bankAccounts:
            print(account)

    # def createBankAccount(self, clientName, amount, password):
    #     newAccount = Account(clientName, amount, password)
    #     newAccountNumber = self.nextaccountNumber
    #     self.bankAccounts[newAccountNumber] = newAccount
    #     # Increment account number to prepare for a new account to be created
    #     self.nextaccountNumber = self.nextaccountNumber + 1
    #     return newAccountNumber
