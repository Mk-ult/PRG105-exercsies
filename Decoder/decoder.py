# Copy the parallel arrays you used in the original program into your new program -- you will need to use the same parallel arrays in order to decode the message.
# Ask the user for the name of the file to import (the file you created in your previous assignment)
# Use try and except statements to ensure the file is there (Use a variable to store the file name, don't hard code it.)
# Use readlines to read the file into a list
# Step through the list (strip the \n!)
# Convert the coded message back into English and display the message on the screen (This can be concatenated to a string as you decode)



def main1():

    alpha_array = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                   'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                   'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', ' ', '.', ',', '!']
    coded_array = ['O', '/', 'm', 'M', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H',
                   'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'n', 'N', '%', '$', '#', '@', '!', '(', ')', '*', '&', '^',
                   '=', '+', '-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'o', ' ']
    decoded_array = []

    print("This program will decode a message for you.")
    file_name = input("What is the name of the file to decode? ")

    if file_name == "encoded.txt":
        file = open(file_name, "r")
        for line in file:
            line = line.strip("\n")
            index = coded_array.index(line)
            decoded_array.append(alpha_array[index])
        decoded_msg = "".join(decoded_array)
        print(decoded_msg)
        file.close()
    else:
        print("File not found.")


main1()
