# Create a dictionary based on the language of your choice with the numbers from 1-10 paired with the numbers from 1-10 in English
# Create a quiz based on this dictionary
# Display the number in a foreign language and ask for the number in English. Score the test and give the user a letter grade.

def main():
    my_dict = {'Jeden': 'one', 'dwa': 'two', 'trzy': 'three', 'cztery': 'four', 'pięć': 'five', 'sześć': 'six', 'siedem': 'seven', 'osiem': 'eight', 'dziewięć': 'nine', 'dziesięć': 'ten'}
    score = 0
    
    print("Enter the number in English that corresponds to the number in Polish.")
    for key in my_dict:
        answer = input(f"What is the equivalent of {key} in English? ")
        if answer == my_dict[key]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    print(f"You scored {score} out of 10.")
    if score == 10:
        print("Perfect score! \n 'A+'")
    elif score >= 8:
        print("Great job! \n 'B+'")
    elif score >= 6:
        print("Good job! \n 'C'")
    elif score >= 4:
        print("You Failed! \n 'D'")
    else:
        print("You Failed! \n 'F'")
    
    
main()
    