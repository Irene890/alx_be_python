# define a function that performs basic arithmetic operations
# num1 (float), num2 (float), and operation (string)
# The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
# The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
# For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.

def perform_operation(num1,num2,operation):
    # num1 = float(input("Enter the first number: "))
    # num2 = float(input("Enter the second number: "))
    # operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return("Sorry, please type another number other than 0")
            else:
                return num1 / num2
        case _:
            print("I don't recognize that.")

