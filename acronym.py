# Get phrase from user
# Split the phrase into a list, use 1st letter of each word to create an acronym
# Display acronym using all capital letters

def main():
    print("This program accepts a phrase and returns the acronym")
    user_phrase = input("Please enter a phrase to convert: ")
    user_phrase = user_phrase.upper()

    # Split phrase into a list
    user_list = user_phrase.split()
    new_list = ""
    for word in user_list:
        new_list += word[0]
    print(f"The acronym is: {new_list}")


main()