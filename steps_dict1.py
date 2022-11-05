# You will be tracking the number of steps someone takes each day for a week.
# Using a loop, ask them to enter the date and the number of steps.
# At the end of the program, you will display the total number of steps taken,
# the day with the most steps, and the day with the least steps.
# Print multiple days if they are tied.
# Store the steps entered in a dictionary using the day names as a key.


def main():
    days_and_steps = {}
    total = 0
    maximum = 0
    minimum = 5000000
    print("Enter the number of steps you took each day for the week.")

    for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
        steps = int(input("Enter the number of steps you took on " + day + ": "))
        days_and_steps[day] = steps
        total += steps
        if steps > maximum:
            maximum = steps
        if steps < minimum:
            minimum = steps

    average = total / 7
    print(f"You walked a total of {total:,.0f} steps during the week.")
    print(f"That was an average of {int(average)} ")
    print(f"The Maximum steps you took were {maximum} on: ")
    for d in days_and_steps:
        if days_and_steps[d] == maximum:
            print(d)
    print(f"The Minimum steps you took were {minimum} on: ")
    for d in days_and_steps:
        if days_and_steps[d] == minimum:
            print(d)


main()