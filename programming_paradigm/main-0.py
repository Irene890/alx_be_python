import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        return (f"Deposited: ${amount:.0f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            return(f"Withdrew: ${amount:.0f}")
        else:
            return("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        return("Invalid command.")

if __name__ == "__main__":
    main()