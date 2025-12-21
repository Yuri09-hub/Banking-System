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
    def __init__(self, number_account, customer, balance):
        self.customer = customer
        self.balance = balance
        self.number_account = number_account

    def deposit(self, value):
        if value <= 0:
            print(f"You cannot deposit negative or zero values")
        else:
            self.balance += value

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            print(f"Not enough money")

    def print_balance(self):
        print(f'Name:{self.customer.name}')
        print(f"Balance:{self.balance}")
