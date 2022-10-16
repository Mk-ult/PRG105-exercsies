#  Write a program that gathers contact information from people
# The program should ask the user how many entries they are going to make
# Then it should ask for the name, address, and phone number for each entry
# You will be writing this information to a text file.
# Separate each value with a comma, and make sure to include the new line character.

def main():
    entries = int(input("Enter the number of entries you are going to make: "))

    address_book = open("address_book.txt", "w")

    for count in range(1, entries + 1):
        name = input("What is the name of the person? ")
        phone_number = input("What is their phone number? ")
        email_address = input("What is their email address? ")
        print()
        address_book.write(f'{name}, {phone_number}, {email_address}\n')

    address_book.close()


main()
