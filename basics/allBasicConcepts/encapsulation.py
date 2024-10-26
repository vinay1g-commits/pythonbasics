"""
Data Hiding: Encapsulation allows you to hide the internal state of an
object and only expose what is necessary. This is often done using access
modifiers (like private, protected, and public).

Public and Private Attributes: In Python, attributes that are intended
to be private can be prefixed with an underscore (e.g., _attribute).
This is a convention to indicate that they should not be accessed directly
outside the class.

Getter and Setter Methods: Encapsulation often involves providing methods
to get and set the values of private attributes, allowing controlled access.
"""

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Private attribute (by convention)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance  # Getter method

# Usage
account = BankAccount(100)
account.deposit(50)         # Output: Deposited: 50
account.withdraw(30)        # Output: Withdrew: 30
print(account.get_balance())  # Output: 120
# print(account._balance)  # Not recommended, but technically possible
