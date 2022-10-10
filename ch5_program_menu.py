def choice_a():
    return print(
        "Make this chicken with creamy sauce in a slow cooker. Add it to mashed potatoes, rice, or noodles, and you "
        "have a comforting meal that everyone will enjoy.")


def choice_b():
    return print(
        "Make this in a Crock Pot, but you can also bake it in the oven or make it on the stove top. You can slice"
        " it or shred it, depending on how you plan to serve it.")


def choice_c():
    return print(
        "Cook these in your Crock Pot, air fryer, or skillet. It doesn’t matter how you cook them because they always "
        "come out tasting great. Serve it with any vegetable or a salad, and you have a delicious meal.")


def choice_d():
    return print(
        "You can serve this as the main dish or a side dish. Or it can be the whole meal. Macaroni and cheese is "
        "considered one of the most popular foods in the U.S.")


def choice_e():
    return print("Classic choice, cant go wrong here. Add anything you want as a topping. Put pineapple on it or dip "
                 "it some mayonnaise")


def main_menu():
    print("Select one of the menu options below to find out more")
    print("A. Chicken and Gravy ")
    print("B. Garlic Tomato Roast Beef")
    print("C. Barbeque Pork chops")
    print("D. Classic baked Mac and Cheese")
    user_choice = input("Enter the letter of your choice: ")

    if user_choice == "A" or user_choice == "a":
        choice_a()
    elif user_choice == "B" or user_choice == "b":
        choice_b()
    elif user_choice == "C" or user_choice == "c":
        choice_c()
    elif user_choice == "D" or user_choice == "d":
        choice_d()
    elif user_choice == "E" or user_choice == "e":
        choice_e()
    else:
        print("Invalid choice, try again")
        main_menu()


main_menu()