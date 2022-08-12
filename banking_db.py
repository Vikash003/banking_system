from random import *

bankAccounts = {}
class SavingsAccount():
    def __init__(self):
        self.balance = 0
    def createAccount(self, name, initialDeposit):
        accNumber = randint(10000, 99999)
        self.name = name
        self.balance += initialDeposit
        bankAccounts[accNumber] = self
        return accNumber

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance - amount < 0:
            return False
        else:
            return True

run = 'y'
while run == 'y':
    option = 0
    while option not in [1, 2]:
        option = int(input("1.Create a new Savings Account\n2.open existing account\nEnter the option : "))
        if option not in [1, 2]:
            print("Option not available, Try Again!\n")

    if option == 1:
        account = SavingsAccount()
        print("\nNew Account Details :-")
        name = input("Enter your name : ")
        initialDeposit = int(input("Initial Deposit : "))
        accNumber = account.createAccount(name, initialDeposit)
        print("New Savings Account Created")
        print(f"Account Number : {accNumber}")

    if option == 2:
        accFound = False
        while not (accFound):
            print("\nExisting Account Details :-")
            name = input("Enter your name : ")
            accNumber = int(input("Enter Account Number : "))
            if accNumber in bankAccounts.keys():
                accFound = True
                print("Account Found")
                currAccount = bankAccounts[accNumber]
                accOption = 1
                while accOption != 0:
                    print("\nAccount Options :-\n0.Quit\t1.Withdraw\t2.Deposit\t3.Display Balance")
                    accOption = int(input("Enter the option : "))
                    if accOption == 1:
                        withAmount = int(input("Enter the amount to withdraw : "))
                        if currAccount.withdraw(withAmount):
                            print(f"rs {withAmount}/- is withdrawed")
                            print(f"Balance : {currAccount.balance}")
                        else:
                            print("Not enough Balance!")
                    if accOption == 2:
                        depAmount = int(input("Enter the amount to deposit : "))
                        currAccount.deposit(depAmount)
                        print(f"rs {depAmount}/- is deposited")
                        print(f"Balance : {currAccount.balance}")
                    if accOption == 3:
                        print(f"Available Balance : {currAccount.balance}")
            else:
                accFound = False
                print("Account not Found, Try Again!")

    run = input("\nContinue (y/n) : ")
