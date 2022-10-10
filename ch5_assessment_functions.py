PI_VALUE = 3.14


def from_main():
    print("This program will find the area of a shape for you")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Square")
    print("4. Circle")
    print("5. Quit")
    user_choice = int(input("Please enter the number of your selection: "))
    validate(user_choice)
    if user_choice == 1:
        rectangle()
    elif user_choice == 2:
        triangle()
    elif user_choice == 3:
        square()
    elif user_choice == 4:
        circle()
    elif user_choice == 5:
        print("Goodbye")
        quit_program()


def validate(number):
    while number < 1 or number > 5:
        print("That is not a valid number")
        print("1. Rectangle \n2. Triangle \n3. Square \n4. Circle \n5. Quit")
        number = int(input("Please enter the number of your selection: "))
    return number


def rectangle():
    width = float(input("Enter the width of the rectangle in cm: "))
    height = float(input("Enter the height of the rectangle in cm: "))
    area = height * width
    area1 = format(area, '.2f')
    print(f"The area of the rectangle is " + str(area1) + " square CM")


def triangle():
    base = float(input("Enter the base of the triangle in cm: "))
    height = float(input("Enter the height of the triangle in cm: "))
    area = 0.5 * height * base
    area1 = format(area, '.2f')
    print(f"The area of the triangle is " + str(area1) + " square CM")


def square():
    length_of_side = float(input("Enter the length of one side of the square in cm: "))
    area = length_of_side * length_of_side
    area1 = format(area, '.2f')
    print(f"The area of the square is " + str(area1) + " square CM")


def circle():
    radius = float(input("Enter the radius of the circle in cm: "))
    area = PI_VALUE * radius * radius
    area1 = format(area, '.2f')
    print(f"The area of the circle is " + str(area1) + " square CM")


def quit_program():
    print("Goodbye")
    quit()


from_main()