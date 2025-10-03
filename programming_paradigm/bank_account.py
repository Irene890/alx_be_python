# class BankAccount:
#     def __init__ (self,initial_balance=0):
#         self._account_balance = initial_balance
        
        
#     def deposit(self, amount):
#         if amount > 0:
#             self._account_balance += amount
#             print(f"Deposited:${amount:.0f}")
#         else:
#             print("ERROR: Deposit must be positive.")

#     def withdraw(self, amount):     
#         if amount <= 0:
#             print("ERROR: Withdrawal amount must be positive.")
#             return False
        
#         elif amount <= self._account_balance:
#             self._account_balance -= amount
#             print(f"Withdrew:${amount:.0f}")
#             return True
#         else:
#             print("Insufficient funds.")
#             return False

#     def display_balance(self):
#         print( f"Current Balance: ${self._account_balance}")

# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.0f}")
            return True
        else:
            print("ERROR: Deposit must be positive.")
            return False

    def withdraw(self, amount):
        if amount <= 0:
            print("ERROR: Withdrawal amount must be positive.")
            return False
        elif amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.0f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.0f}")

