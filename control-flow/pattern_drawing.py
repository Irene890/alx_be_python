# Utilize while loops and nested for loops to draw a simple text-based pattern.
# script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
# use a while loop to iterate through each row of the pattern
square_length = int(input("Enter the size of the pattern: "))
rows = 1

while rows <= square_length:
    for x in range(square_length):
        print("*",end="")
    print("")
    rows = rows +1
    

