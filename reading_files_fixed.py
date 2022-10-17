def main():
    sales_file = open("sales_totals.txt", "r")
    total = 0
    count = 0
    for line in sales_file:
        sales_amt = float(line.rstrip('\n'))
        print(format(sales_amt, "10,.2f"))
        total += sales_amt
        count += 1
    print("Total: " + format(total, "27,.2f"))
    print("Number of entries: " + format(count, "15,.0f"))
    print("Average: " + format((total/count), "25,.2f"))

main()