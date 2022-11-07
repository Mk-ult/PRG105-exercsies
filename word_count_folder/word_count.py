# Create a program to read the words in the file and add them to a dictionary 
# along with a count of how many times each word appears in the file.
# Create a program to read the words in the file and add them to a dictionary along with a count of how many times each word appears in the file.
# 

def main():
    # Open the file
    in_file = open('tale_of_two_cities.txt', 'r')
    # Create a dictionary to hold the words and their counts
    word_count = {}
    # Read the file's contents
    for line in in_file:
        # Split the line into words
        words = line.split()
        # Add the words to the dictionary
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    # Close the file
    in_file.close()
    # Display the words and their counts
    for word in word_count:
        if word_count[word] <= 1:
            print(word, word_count[word])
        # print(word, word_count[word])

main()