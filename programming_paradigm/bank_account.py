class BankAccount:

    def __init__(self, initial_balance=0):
        # Store balance as a whole int
        self._account_balance = int(initial_balance)

    def deposit(self, amount: int):
        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount: int):
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.0f}")


