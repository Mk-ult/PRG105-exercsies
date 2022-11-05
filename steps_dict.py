# You will be tracking the number of steps someone takes each day for a week. Using a loop, ask them to enter the date and the number of steps. 
# At the end of the program, you will display the total number of steps taken, the day with the most steps, and the day with the least steps. 
# Print multiple days if they are tied.
# Store the steps entered in a dictionary using the day names as a key.

print("Enter the number of steps you took each day for the past week.")

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_and_steps = {}
max = 0
min = 100000000
total = 0


for day in days:
    user_steps = input(f"How many steps did you take on {day}? ")
    total += int(user_steps)
    for step in user_steps:
        days_and_steps[day] = user_steps
        if int(user_steps) > max:
            max = int(user_steps)
        if int(user_steps) < min:
            min = int(user_steps)
        
print(days_and_steps)
print(f"You walked a total of {total} steps during the week.")
average = total / len(days)
print(f"That was an average of {int(average)} ")
print(f"The Maximum steps you took were {max} on {day}")
print(f"The Minimum steps you took were {min} on {day}")
    
