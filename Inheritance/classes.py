# ou will create two classes, a parent class and a child class, in one file. You will import that file into a separate file holding your program code.
# Write an Employee class that keeps data attributes for the following pieces of information: Employee Name and Employee Number
# write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class should keep data attributes for the following information: Shift Number (an integer, such as 1, 2, or 3) and Hourly Pay Rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2.
# Write the appropriate accessor and mutator methods (get and set) for each class.
# Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts the user to enter data for each of the object’s data attributes
# Store the data in the object and then use the object’s accessor methods to retrieve it and display it on the screen.

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number
    
    def __str__():
        return f"Name: {self.__name} Number: {self.__number}"
    
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__pay = pay

    def set_shift(self, shift):
        self.__shift = shift
        
        if shift == "1":
            shift = "Day"
        elif shift == "2":
            shift = "Night"
        else:
            shift = "Unassigned"

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay
    
    def __str__():
        return f"Name: {self.__name} Number: {self.__number} Shift: {self.__shift} Pay: {self.__pay}"
    
