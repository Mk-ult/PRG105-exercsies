# Write a program that will read numeric data from a text file line by line using a loop.
# Strip the newline and convert each value to a float, then display it.
# Use variables to count and total the entries.
# At the end, display the total, count and average of the values.

sales_total = open("sales_totals.txt", "r")
total = 0
count = 0

for line in sales_total:
    correct_line = float(line.strip())
    total += correct_line
    count += 1
    # print(correct_line)

# print(type(correct_line))
sales_total.close()
average = total / count
print(f"Total: {total:,.2f}")
print(f"Number of entries: {count}")
print(f"Average: {average:,.2f}")

