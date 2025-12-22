# 🏦 Banking System – Python (Console Application)
A console-based banking system developed in Python using Object-Oriented Programming (OOP).
This project simulates the core functionalities of a real banking system, focusing on clean architecture, data validation, and scalability.

📌 Features

-Customer registration with validated personal data

-Unique bank account number generation

-Deposit and withdrawal operations

-Account-to-account transfer

-View balance of a specific account

-View information of all registered accounts

-Console-based interactive menu

🧠 System Design

The system follows Object-Oriented Programming principles, separating responsibilities into different modules:

Main Components:

Customer:

-Stores personal information

-Responsible for displaying customer data

Account:

-Manages balance

-Handles deposit and withdrawal operations

Bank:

-Creates and stores accounts

-Searches accounts

-Handles transfers

-Displays registered accounts

-Validation Module

-Validates user input (name, document type, document number, location)

📂 Project Structure

banking-system/

│

├── main.py

├── system.py

├── verification.py

└── README.md

🛂 Data Validation Strategy

The system validates all user input before creating accounts:

-Name: letters only (spaces allowed)

-Document Type: Passport or Identity Card

-Document Number:

-Passport → 8 alphanumeric characters

-Identity Card → 14 alphanumeric characters

-Province & Municipality: letters only

-Validation rules are implemented in a separate module (verification.py) to keep the system modular and maintainable.

🔐 Account Number Generation

-Account numbers are randomly generated

-The system guarantees uniqueness by storing and checking existing account numbers

-Duplicate account numbers are not allowed


📖 Menu Options

1 - Create account

2 - Deposit

3 - Withdraw

4 - Transfer

5 - View balance

6 - View information for all registered accounts

0 - Exit

