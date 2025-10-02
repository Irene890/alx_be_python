class BankAccount:
    def __init__ (self,initial_balance=0):
        self._account_balance = initial_balance
        
        
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited:${amount:.0f}"
        else:
            return f"ERROR: Deposit must be positive."

    def withdraw(self, amount):     
        if amount <= 0:
            return "Amount should higher that current balance."
            
        if self._account_balance >= amount:
            self._account_balance -= amount
            return f"Withdrew:${amount:.0f}"
            
        else:
            return f"Insufficient funds."
            
        
    def display_balance(self):
        print( f"Current Balance: ${self._account_balance}")



