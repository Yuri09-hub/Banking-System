class customer:
    def __init__(self, name, address, document, type):
        self.name = name
        self.address = address
        self.document = document
        self.type = type

    def print_customer(self):
        print(f"Name: {self.name}")
        print(f"Address:{self.address}")
        print(f"{self.type}_ID:{self.document}")


class Account(customer):
    def __init__(self, Number_account, balance, name, address, document, type):
        super().__init__(name, address, document, type)
        self.Number_account = Number_account
        self.balance = balance
        self.name = name
        self.address = address
        self.document = document
        self.type = type

    def deposit(self, value):
        if value <= 0:
            print(f"You cannot deposit negative values")
        else:
            self.balance += value

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            print(f"Not enough money")

    def print_balance(self):
        print(f"Name: {self.name}")
        print(f"Balance:{self.balance}")
