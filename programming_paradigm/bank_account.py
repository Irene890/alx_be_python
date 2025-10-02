class BankAccount:
    def __init__ (self,initial_balance=0):
        self._account_balance = initial_balance
        
        
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited:${amount}")
        else:
            print(f"ERROR: Deposit must be positive.")

    def withdraw(self, amount):     
        if amount <= 0:
            print("Amount should higher that current balance.")
            return False
        if self._account_balance >= amount:
            self._account_balance -= amount
            print(f"Withdrew:${amount}")
            return True
        else:
            print(f"Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance}")



