total_monthly_income = float(input("How much is your total monthly income? "))
monthly_housing = float(input("How much do you spend on housing each month? "))
monthly_food = float(input("How much do you spend on food each month? "))
monthly_transportation = float(input("How much do you spend on transportation each month? "))
monthly_phonebill = float(input("How much do you spend on your phone bill each month? "))
monthly_utilities = float(input("How much do you spend on utilities each month? "))
monthly_clothing = float(input("How much do you spend on clothing each month? "))

print("\n")

total_housing = monthly_housing / total_monthly_income
print(f"Housing takes up {total_housing:.2%} of your monthly income")
total_food = monthly_food / total_monthly_income
print(f"Food takes up {total_food:.2%} of your monthly income")
total_transportation = monthly_transportation / total_monthly_income
print(f"Transportation takes up {total_transportation:.2%} of your monthly income")
total_phone = monthly_phonebill / total_monthly_income
print(f"Your phone bill takes up {total_phone:.2%} of your monthly income")
total_utilities = monthly_utilities / total_monthly_income
print(f"Utilities take up {total_utilities:.2%} of your monthly income")
total_clothing = monthly_clothing / total_monthly_income
print(f"Clothing takes up {total_clothing:.2%} of your monthly income")