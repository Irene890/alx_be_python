# Script calculates the user’s monthly savings based on inputted monthly income and expenses
# Script projects these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
interest = 0.05

monthlyincome =int(input('Enter your monthly income: '))
monthlyexpenses =int(input('Enter your total monthly expenses: '))
monthlysavings = monthlyincome - monthlyexpenses

projectedsavings = int(monthlysavings * 12 + (monthlysavings * 12 * 0.05))

print (f"Your monthly savings are ${monthlysavings}.")
print(f"Projected savings after one year, with interest, is: ${projectedsavings}.")