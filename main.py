from system import *
from verification import *
from datetime import datetime

date = datetime.today()

while True:
    print("\n===== BANKING SYSTEM =====\n")
    print("1 - Create account")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Transfer")
    print("5 - View balance")
    print("6 - View information for all registered accounts. ")
    print("0 - Log out")
    option = input("Choose an option: ")

    if option == "1":
        Name = str(input("Enter your full name: ")).lower().capitalize()
        while not Name_verication(Name):
            Name = str(input("Enter your full name: ")).lower().capitalize()

        document_type = str(input("Enter your document type(Passport/Identity Card): "))
        while not Document_type_verification(document_type):
            document_type = str(input("Enter your document type(Passport/Identity Card): "))
        if document_type == "Passport":
            digit = 8
        else:
            digit = 14

        Document = str(input(f"Enter your {document_type} number({digit} digits): ")).strip()
        while not Document_verification(Document, document_type):
            Document = str(input(f"Enter your {document_type} number: ")).strip()

        Province = str(input("Enter your Province: ")).strip()
        while not alpha_verification(Province):
            Province = str(input("Enter your Province: ")).strip()

        municipality = str(input("Enter your Street: ")).strip()
        while not whitespace_verification(municipality):
            street = str(input("Enter your  municipality: ")).strip()

        Customer = customer(Name, Province,  municipality, document_type, Document)
        Creat = Bank.creat_account(Customer)
        print("Account created successfully!")
        Creat.print_balance()

    elif option == '2':
        number = int(input("Account number: "))
        value = float(input("Deposit amount: "))

        account = Bank.search_account(number)
        if account:
            if account.deposit(value):
                print("Deposit successful")
        else:
            print("Account not found")

    elif option == '3':
        number = int(input("Account number: "))
        value = float(input("Withdraw amount: "))

        account = Bank.search_account(number)
        if account:
            if account.withdraw(value):
                print("Withdraw successful")
        else:
            print("Account not found")

    elif option == "4":
        acc1_number = int(input("Origin account: "))
        acc2_number = int(input("Destination account: "))
        value = float(input("Amount: "))

        acc1 = Bank.search_account(acc1_number)
        acc2 = Bank.search_account(acc2_number)

        if acc1 and acc2:
            if acc1.withdraw(value):
                acc2.deposit(value)
                print("Transfer successful")
            else:
                print("Not enough money")
        else:
            print("One or both accounts not found")

    elif option == "5":
        number = int(input("Account number: "))
        account = Bank.search_account(number)

        if account:
            print("--------------------")
            print(f"Name: {account.customer.name}")
            account.print_balance()
            print("--------------------")

        else:
            print("Account not found")

    elif option == "6":
        if not Bank.list_of_Accounts:
            print("No accounts registered")
        else:
            bank = Bank("Bank of Unit Credit")
            bank.print_accounts()

    elif option == "0":
        print("Exiting system...")
        break

    else:
        print("Invalid option")
