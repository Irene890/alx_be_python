#  prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division).
# script will then perform the selected operation using a Match Case statement and display the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
n = input("Choose the operation (+, -, *, /): ")

match n:
    case "+": 
        result = num1 + num2
        print(f"The result is {result}.")
    case "-": 
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print (f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _ :
        print("")
