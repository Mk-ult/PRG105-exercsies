# create a program  that will have the user enter the total sales amount for the day at a coffee shop
# The program should ask the user for the total amount of sales and include the day in the request
# At the end of data entry, tell the user the total sales for the week, and the average sales per day. 
# You must create a list of the days of the week for the user to step through, see the example output

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]

for day in days_of_week:
    day += float(input("What were the total sales for"))