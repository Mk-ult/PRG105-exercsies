# Design a class that holds the following personal data: name, address, age, and phone number.
# Write appropriate accessor and mutator methods (get and set methods).
# Write a program that creates three instances of the class.
# One instance should hold your information and the other two should hold your friends' or family members' information.
# Just add information, don't get it from the user
# Print the data from each object, make sure to format the output for clarity and ease of reading.

class Person:
    def __init__(self, name_in, address_in, age_in, phone_number_in):
        self.__name = name_in
        self.__address = address_in
        self.__age = age_in
        self.__phone_number = phone_number_in

    def set_name(self, name_in):
        self.__name = name_in

    def set_address(self, address_in):
        self.__address = address_in

    def set_age(self, age_in):
        self.__age = age_in

    def set_phone_number(self, phone_number_in):
        self.__phone_number = phone_number_in

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def __str__(self):
        return "Name: " + self.__name + "\nAddress: " + self.__address + "\nAge: " + self.__age + "\nPhone Number: " + self.__phone_number


def main():
    person1 = Person("Martin", "123 Main St.", "25", "123-456-7890")
    person2 = Person("John", "456 Main St.", "26", "123-456-7891")
    person3 = Person("Jane", "789 Main St.", "27", "123-456-7892")

    print(person1)
    print()
    print(person2)
    print()
    print(person3)


main()