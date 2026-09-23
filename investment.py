"""
Program: investment.py
8/27/26

Application that provides an investment report. User provides the details of the investment. Output will be calculations year by year and also some final summaries.

"""

# Input phase
startBalance = float(input("Please, enter the investment amount >> "))
years = int(input("Next, enter the number of years for the investment >> "))
rate = float(input("Finally, enter the interest rate as a % >> "))

# Processing phase
rate = rate / 100

# Create an accumulator variable for the total interest
totalInterest = 0.0

# Display the header for the table using tabular format
print()
print("%4s%18s%10s%16s" % ("Year", "Starting Balance", "Interest", "Ending Balance"))

# Compute and display the results for each year using a FOR LOOP
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest

# Output phase displaying the final totals
print("-" * 50)
print("Final Balance: $%0.2f" % endBalance)
print("Total Interest Earned: $%0.2f" % totalInterest)

input("\n\nPress ENTER to quit")