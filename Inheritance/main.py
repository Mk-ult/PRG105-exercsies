# You will create two classes, a parent class and a child class, in one file. You will import that file into a separate file holding your program code.
# Write an Employee class that keeps data attributes for the following pieces of information: Employee Name and Employee Number
# write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class should keep data attributes for the following information: Shift Number (an integer, such as 1, 2, or 3) and Hourly Pay Rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2.
# Write the appropriate accessor and mutator methods (get and set) for each class.
# Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts the user to enter data for each of the object’s data attributes
# Store the data in the object and then use the object’s accessor methods to retrieve it and display it on the screen.

import classes


def main():
    print("Please enter the following information:")
    name = input("Enter name: ")
    number = input("Enter ID number: ")
    shift = input("Enter shift (1=day, 2=night, 0=unassigned): ")
    pay = input("Hourly Pay Rate: ")
    print()
    
    worker = classes.ProductionWorker(name, number, shift, pay)
    
    print(f"Employee: {worker.get_name()}")
    print(f"ID Number: {worker.get_number()}")
    print(f"Shift: {worker.get_shift()}")
    print(f"Hourly Pay Rate: {worker.get_pay()}")


main()