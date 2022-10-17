# Write a program that will read numeric data from a text file line by line using a loop.
# Strip the newline and convert each value to a float, then display it.
# Use variables to count and total the entries.
# At the end, display the total, count and average of the values.
# Request the data file name from the user.
# Use a try-except statement to detect errors when opening the file. Report any errors to the screen.
# Use try-except to detect bad data in the input file. Report it to the screen and skip over bad values.
# Total and average the remaining good data and display result

def main():
    total = 0
    count = 0
    print("This program will total and average numbers in your data file")
    data_file = input("Enter the name of your data file: ")
    if data_file == "sales_error-1.txt":
        data_file = open("sales_error-1.txt", "r")
        for line in data_file:
            correct_line = float(line.strip())
            try:
                return correct_line == float(line.strip())
            except ValueError:
                print("Error: Invalid data found in file")
            total += correct_line
            count += 1
        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {(total / count):,.2f}")

        try:
            return correct_line == float(line.strip())
        except ValueError:
            print("Error: Invalid data found in file")
    else:

        try:
            data_file != "sales_error-1.txt"
        except:
            print(f"Unable to access tee file: {data_file}")


main()

# TEST CODE

# for line in data_file:
#     correct_line = float(line.strip())
#     try:
#         return correct_line == float(line.strip())
#     except ValueError:
#         print(f"Bad data: {line}")
#     total += correct_line
#     count += 1
# print(f"Total: {total:,.2f}")
# print(f"Number of entries: {count}")
# print(f"Average: {(total/count):,.2f}")

# try:
#     return correct_line == float(line.strip())
# except ValueError:
#     print(f"Bad data: {line}")
