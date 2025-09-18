# Utilize while loops and nested for loops to draw a simple text-based pattern.
# script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
# use a while loop to iterate through each row of the pattern
square_length = int(input("Enter the size of the pattern: "))

while square_length:
    for x in range(1,square_length):
        print("*" * square_length,end="")
        print("")
    break

