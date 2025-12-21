import random
from datetime import datetime


class customer:
    def __init__(self, name, Province, document_type, document):
        self.name = name
        self.Province = Province
        self.document_type = document_type
        self.document = document
        self.data = datetime.today()

    def print_customer(self):
        print(f"Name: {self.name}")
        print(f"Address:{self.Province}")
        print(f"{self.document_type}_ID:{self.document}")
        print(f"Date: {self.data}")


class Account:
    def __init__(self, number_account, customer):
        self.customer = customer
        self.balance = 0.0
        self.number_account = number_account

    def deposit(self, value):
        try:
            value = float(value)
            self.balance += value
            return True
        except ValueError and value <= 0:
            print('Error: undefined values')
            return False

    def withdraw(self, value):
        try:
            value = float(value)
            self.balance -= value
            return True
        except value > self.balance:
            print('Not enough money')
            return False
        except ValueError and value <= 0:
            print('Error: undefined values')
            return False

    def print_balance(self):
        print(f'Number account: {self.number_account}')
        print(f"Balance:{self.balance}Kz")


class Bank:
    list_of_Accounts = []
    Existing_account_numbers = []

    def __init__(self, name):
        self.name = name

    @staticmethod
    def creat_account(customer):
        number_account = random.randint(10000000000000, 99999999999999)
        while number_account in Bank.Existing_account_numbers:
            number_account = random.randint(10000000000000, 99999999999999)
        Bank.Existing_account_numbers.append(number_account)
        account = Account(number_account, customer)
        Bank.list_of_Accounts.append(account)
        return account

    @staticmethod
    def search_account(number_account):
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

    def print_accounts(self):
        if not Bank.list_of_Accounts:
            print("No accounts registered")
            return

        print(f"===== {self.name} =====")
        for account in Bank.list_of_Accounts:
            account.customer.print_customer()
            print("--------------------")
            account.print_balance()
            print("--------------------")
