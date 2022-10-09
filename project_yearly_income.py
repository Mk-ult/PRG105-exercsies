# Write a program that projects yearly income, amount saved towards retirement each year, and total retirement savings.
# Assume a 3% raise each year, and a 6% yearly return on investments.





user_age = int(input("How old are you currently? "))
user_retirement_age = int(input("At what age do you plan to retire? "))
years_left = user_retirement_age - user_age
yearly_income = int(input("What is your yearly income? "))
# yearly_income = yearly_income * 1.03
savings_percent = int(input("What percent of your income do you save? "))
total_savings = int(input("How much do you currently have saved? "))