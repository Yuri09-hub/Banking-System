import random


class customer:
    def __init__(self, name, address, document, type):
        self.name = name
        self.address = address
        self.type = type
        self.document = document

    def print_customer(self):
        print(f"Name: {self.name}")
        print(f"Address:{self.address}")
        print(f"{self.type}_ID:{self.document}")


class Account:
    def __init__(self, number_account, customer):
        self.customer = customer
        self.balance = 0.0
        self.number_account = number_account

    def deposit(self, value):
        if value <= 0:
            print(f"You cannot deposit negative or zero values")
            return False
        else:
            self.balance += value
            return True

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            return True
        else:
            print(f"Not enough money")
            return False

    def print_balance(self):
        print(f'Name:{self.customer.name}')
        print(f"Balance:{self.balance}")


class Bank:
    list_of_Accounts = []

    def __init__(self, name):
        self.name = name

    def creat_account(self, customer):
        number_account = random.randint(10000000000000, 99999999999999)
        account = Account(number_account, customer)
        Bank.list_of_Accounts.append(account)

    def search_account(self, number_account):
        for account in Bank.list_of_Accounts:
            if account.number_account == number_account:
                return account
        return None

    def transfer_account(self, account1, account2, amount):
        account1 = self.search_account(account1.number_account)
        account2 = self.search_account(account2.number_account)
        if account1 and account2:
            if account1.withdraw(amount):
                account1.deposit(amount)
                print('Transfer successful')
            else:
                print('Transfer failed')
        else:
            print('Account not found')

    @staticmethod
    def print_accounts():
        for account in Bank.list_of_Accounts:
            print(f"Customer: {account.customer}")
            print(f"Account: {account.number_account}")
