# you will create a simple trivia game for two players
# Starting with player 1, each player gets a turn at answering 5 trivia questions.
# (There should be a total of 10 questions.)
# When a question is displayed, 4 possible answers are also displayed.
# Only one of the answers is correct, and if the player selects the correct answer, he or she earns a point. 
# After answers have been selected for all the questions, the program displays the number of points earned by each
# player and declares the player with the highest number of points the winner.
# To create this program, write a Question class to hold the data for the trivia question.
# The Question class should also have an appropriate __init__ method, accessors, and mutators.
# The program should have a list or a dictionary containing 10 Question Objects, one for each trivia question.
# Make up your own trivia question on the subject or subjects of your choice for the objects.

import question


def main():

    print("Welcome to Trivia Game! There are 10 questions.")
    print("There are 2 players taking turns after each question.")
    print("Player 1 will go first.")
    print()

# define variables for player 1 score and player 2 score
# initialise both to zero
    tries = 10
    player1 = 0
    player2 = 0

    questions = get10questions()

    for questionCount in range(tries):
        if questionCount % 2 == 0:
            player = 'first'
        else:
            player = 'second'

        print("This question is for the", player, "player")

        # show the next question
        current = questions[questionCount]
        print(current)

        # get the user input
        player_answer = int(input("Please enter your answer, given options 1 to 4: "))
        while player_answer < 1 or player_answer > 4:
            print("This is not a valid entry. Please enter either 1, 2, 3 or 4.")
            player_answer = int(input("Please enter your answer, given options 1 to 4: "))

        print('\n')

        # check if the answer is correct
        if current.right_answer(player_answer):
            if player == "first":
                player1 += 1
            else:
                player2 += 1

    # display scores
    print('Player 1 has a total score of', player1, 'points')
    print('Player 2 has a total score of', player2, 'points')

    # declare the winner
    if player1 > player2:
        print('Congrats! The winner is Player 1')
    elif player2 > player1:
        print('Congrats! The winner is Player 2')
    else:
        print('There is a tie. No winner declared.')


def get10questions():

    questions = []

    # create 10 questions
    q1 = question.Question("Question 1: What is the only food that cannot go bad?", "Honey", "Peanut Butter",
                           "Dark Chocolate", "Canned Tuna", 1)
    questions.append(q1)

    q2 = question.Question("Question 2: What is the most visited tourist attraction in the world?", "Statue of Liberty",
                           "Eiffel Tower", "Great Wall of China", "Colosseum", 2)
    questions.append(q2)

    q3 = question.Question("Question 3: What’s the heaviest organ in the human body?", "Brain", "Heart", "Skin",
                           "Liver", 4)
    questions.append(q3)

    q4 = question.Question("Question 4: On average, how many seeds are located on the outside of a strawberry?",
                           "500", "100", "200", "300", 3)
    questions.append(q4)

    q5 = question.Question("Question 5: Which fast food restaurant has the largest number of retail locations in the "
                           "world?", "Chipotle", "Subway", "Mcdonald's", "Wendy's", 2)
    questions.append(q5)

    q6 = question.Question("Question 6: What is the oldest soft drink in the United States?",
                           "Mt. Dew", "Pepsi", "Coca Cola", "Dr. Pepper", 4)
    questions.append(q6)

    q7 = question.Question("Question 7: What river passes through New Orleans, Louisiana?",
                           "Mississippi River", "Colorado River", "Orleans River", "Fox River", 1)
    questions.append(q7)

    q8 = question.Question("Question 8: In what country do more than half of people believe in elves?",
                           "Norway", "Russia", "Iceland", "Holland", 3)
    questions.append(q8)

    q9 = question.Question("Question 9: Which pop star burnt down her home gym with candles?", "Kim Kardashian",
                           "Britney Spears", "Lady Gaga", "Arianna Grande", 2)
    questions.append(q9)

    q10 = question.Question("Question 10: What is the highest-grossing video game franchise to date?",
                            "Call of Duty", "Mario", "Street Fighter", "Pokemon", 4)
    questions.append(q10)

    return questions


main()