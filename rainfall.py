# Import Data from file, turn file into a list
# Check to see if the data is valid, if not valid, indicate to user what the bad data is
# break apart list items into individual components by splitting strings
# split strings on a symbol
# Total and average the data, display formatted results on screen


def main():
    rainfall_list = open("rainfall-totals.txt", "r")
    lines = rainfall_list.readlines()
    rainfall_list.close()

    total = 0.0
    count = 0

    for line in lines:
        line = line.rstrip("\n")
        rain = line.split()
        rain_month = rain[0]
        rain_amt = rain[1].split('.')

        if rain_amt[0].isdigit() and rain_amt[1].isdigit():
            amount = float(rain_amt[0] + "." + rain_amt[1])
            total += float(amount)
            count += 1
        else:
            print(rain_month + " does not have valid data because")
            print(str(rain[1] + " is not a number"))

    print("the total rainfall for " + str(count) + " months is " + format(total, ',.2f'))
    print("the average rainfall was " + format((total/count), ',.2f'))


main()