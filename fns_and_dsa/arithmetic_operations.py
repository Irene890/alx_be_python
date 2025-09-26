# define a function that performs basic arithmetic operations
# num1 (float), num2 (float), and operation (string)
# The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
# The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
# For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.

def perform_operation(num1,num2,operation):
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    operation = input("Enter operation 'add', 'subtract', 'multiply', or 'divide': ").lower()
    
    match operation:
        case "add":
            result = num1 + num2
            print(f"Result: {result}")
        case "subtract":
            result = num1 - num2
            print(f"Result: {result}")
        case "multiply":
            result = num1 * num2
            print(f"Result: {result}")
        case "divide":
            if num2 == 0:
                print("Sorry, please type another number other than 0")
            else:
                result = num1 / num2
                print(f"Result: {result}")
        case _:
            print("I don't recognize that.")
