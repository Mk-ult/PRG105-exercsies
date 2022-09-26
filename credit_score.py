credit_score = int(input("What is your credit score? "))

if credit_score >= 720:
    print("You have excellent credit.")
elif credit_score >= 690:
    print("You have good credit.")
elif credit_score >= 630:
    print("You have fair credit.")
else:
    print("You have bad credit.")

