programName = "Future Value Calculator"
developerName = "Tai Tran"
date = "November 2, 2026"
print(f"Program: {programName}\n"
      f"Developer name: {developerName}\n"
      f"Date: {date}\n"
      f"\n")

monthly_investment = float(input("Enter monthly investment: "))
yearly_interest_rate = float(input("Enter yearly interest rate(%): "))
monthly_interest_rate = (yearly_interest_rate / 100) / 12
years = int(input("Enter number of years the investment will be made: "))
months = years * 12

future_value = 0
principle = 0 

for i in range(months):
    principle = future_value + monthly_investment
    monthly_interest_amount = principle * monthly_interest_rate
    future_value = principle + monthly_interest_amount

future_value = round(future_value, 2)
print("\nThe future value of the total investment:", future_value)