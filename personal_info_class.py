# Design a class that holds the following personal data: name, address, age, and phone number.
# Write appropriate accessor and mutator methods (get and set methods).
# Write a program that creates three instances of the class.
# One instance should hold your information and the other two should hold your friends' or family members' information.
# Just add information, don't get it from the user
# Print the data from each object, make sure to format the output for clarity and ease of reading. 

class AddressBook:
    def __init__(self):
        self.name = "Martin"
        self.address = "123 Main St."
        self.age = "25 "
        self.phone_number = "123-456-7890"

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number
    
def main():
    test1 = AddressBook()
    print("Name:", test1.get_name())
    print("Address:", test1.get_address())
    print("Age:", test1.get_age())
    print("Phone Number:", test1.get_phone_number())
    test2 = AddressBook()
    test2.set_name("John")
    test2.set_address("456 Main St.")
    test2.set_age("26")
    test2.set_phone_number("123-456-7891")
    print("Name:", test2.get_name())
    print("Address:", test2.get_address())
    print("Age:", test2.get_age())
    print("Phone Number:", test2.get_phone_number())
    test3 = AddressBook()
    test3.set_name("Jane")
    test3.set_address("789 Main St.")
    test3.set_age("27")
    test3.set_phone_number("123-456-7892")
    print("Name:", test3.get_name())
    print("Address:", test3.get_address())
    print("Age:", test3.get_age())
    print("Phone Number:", test3.get_phone_number())

main()
    

if __name__ == "__main__":
    main()
    