# Script calculates the user’s monthly savings based on inputted monthly income and expenses
# Script projects these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
interest = 0.05

monthly_income =int(input('Enter your monthly income: '))
monthly_expenses =int(input('Enter your total monthly expenses: '))
monthly_savings = monthly_income - monthly_expenses

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * interest))

print (f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")