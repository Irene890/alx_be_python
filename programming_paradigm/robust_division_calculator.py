#  Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

# safe_divide(numerator, denominator) that performs division, handling potential errors
# Division by Zero: Use a try-except block to catch ZeroDivisionError.
# Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
# Return appropriate messages for errors or the result for successful division.

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        num1 = num / den
    except ZeroDivisionError:
        return("Error: Cannot divide by Zero.")
    except ValueError:
        return("Error: Please enter numeric values only.")
    else:
        return(f"The result of the division is {num1:.1f}")
