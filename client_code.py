# Main program for accessing ATM/Bank

from bank import *

Scotia = Bank("Scotiabank", "#1 Main Street, Waterloo", "Mon to Fri, 8am-5pm")

while True:
    print()
    print("To open a new account, press 'o'.")
    print("To close an account, press 'c'.")
    print("To make a deposit, press 'd'.")
    print("To make a withdrawal, press 'w'.")
    print("To view account balance, press 'b'.")
    print("To show account information, press 'a'.")
    print("For bank information, press 'i'.")
    print("To exit system, press 'q'.")

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]  # grab the first letter
    print()

    try:

        if action == "o":
            Scotia.openAccount()
        elif action == "c":
            Scotia.closeBankAccount()
        elif action == "d":
            Scotia.deposit()
        elif action == "w":
            Scotia.withdraw()
        elif action == "b":
            Scotia.balance()
        elif action == "a":
            Scotia.showInfo()
        elif action == "i":
            Scotia.bankInfo()
        elif action == "q":
            break
    except AbortProcess as error:
        print(error)

print("Done")



