
# Basic ingredients for 1 loaf of bred
butter_basic_tablespoons = .25
sugar_basic_teaspoons = 2
salt_basic_teaspoons = .75
yeast_basic_package = 1.25
flour_basic_cups = 3.25
water_basic_cups = 1.25
# servings_base = 12


# Multiplies the basic ingredients of 1 loaf by the users desired amount and prints the total required.
user_loafs_wanted = int(input("Please enter the amount of loaves that you want: "))
total_butter = butter_basic_tablespoons * user_loafs_wanted
print(f"You will need {total_butter:,.1f} tablespoons of butter")
total_sugar = sugar_basic_teaspoons * user_loafs_wanted
print(f"You will need {total_sugar:,.1f} teaspoons of sugar")
total_salt = salt_basic_teaspoons * user_loafs_wanted
print(f"You will need {total_salt:,.1f} teaspoons of salt")
total_yeast = yeast_basic_package * user_loafs_wanted
print(f"You will need {total_yeast:,.1f} packages of yeast")
total_flour = flour_basic_cups * user_loafs_wanted
print(f"You will need {total_flour:,.1f} cups of flour")
total_water = water_basic_cups * user_loafs_wanted
print(f"You will need {total_water:,.1f} cups of water")

