# Create a program that asks a user to enter a whole number between 20 and 100
# Send that number to a function that will validate the number
# and if it is not a number between 20 and 100, use a while loop to keep asking the user for a valid number
# Return the number to the main function
# In addition, create three functions that determine if the number is divisible by two, by three, and by five
# Pass all of the results to a final function that displays output on the screen - identifying whether or not the number is divisible by two, three, and five.


def main():
    user_number = int(input("Enter a whole number between 20 and 100: "))
    good_number = validate(user_number)
    two = divisible_by_two(good_number)
    three = divisible_by_three(good_number)
    five = divisible_by_five(good_number)
    output(good_number, two, three, five)
    
    
def validate(number):
    while number < 20 or number > 100:
        print("That is not a valid number")
        number = int(input("Enter a whole number between 20 and 100: "))
    return number


def divisible_by_two(number):
    if number % 2 == 0:
        return " is divisible by two"
    else:
        return " is not divisible by two"
    
    
def divisible_by_three(number):
    if number % 3 == 0:
        return " is divisible by three"
    else:
        return " is not divisible by three"
    
    
def divisible_by_five(number):
    if number % 5 == 0:
        return " is divisible by five"
    else:
        return " is not divisible by five"
    
    
def output(number, two_result, three_result, five_result):
    print(str(number) + two_result)
    print(str(number) + three_result)
    print(str(number) + five_result)

main()