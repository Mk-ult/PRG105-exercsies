# you will use parallel arrays (lists) to make a secret code creator
# The first array (alpha array) will hold all upper and lower case letters, space, period, comma, and exclamation point.
# You will create a second array of the same size (code array) to hold your secret code characters
# Make sure you do not duplicate any characters. In other words, the letter 'm' might appear in both arrays, but no more
# than once in each array.
# You will ask the user for a secret phrase and encode each character by finding it in the alpha array and displaying
# the corresponding character from the code array.
# You will display the encoded message on-screen as a list and also write it to a file, one character per line.

def main():

    alpha_array = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                   'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                   'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', ' ', '.', ',', '!']
    coded_array = ['!', ' ', 'm', 'M', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H',
                   'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'n', 'N', '%', '$', '#', '@', '!', '(', ')', '*', '&', '^',
                   '=', '+', '-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'o', 'O']
    encoded_array = []

    secret_phrase = input("Enter a phrase to encode: ")

    for letter in secret_phrase:
        index_letter = alpha_array.index(letter)
        code_value = coded_array[index_letter]
        encoded_array.append(code_value)
    print(encoded_array)

    file = open("encoded.txt", "w")
    for letter in encoded_array:
        file.write(str(letter) + "\n")
    file.close()


main()
