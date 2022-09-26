print("PLAY PRICES PER TICKET")
print("1. Student $5.00")
print("2. Veteran $7.00")
print("3. Show Sponsor $2.00")
print("4. Retiree $5.00")
print("5. General Public $10.00")

category_number = int(input("Please enter the number of the category you fit for purchasing tickets: "))
user_tickets = int(input("How many tickets would you like to purchase? "))
total_price = 0

if category_number == 1:
    total_price = 5.00 * user_tickets
    print(f"Cost before any discounts were applied: ${total_price:.2f}")
elif category_number == 2:
    total_price = 7.00 * user_tickets
    print(f"Cost before any discounts were applied: ${total_price:.2f}")
elif category_number == 3:
    total_price = 2.00 * user_tickets
    print(f"Cost before any discounts were applied: ${total_price:.2f}")
elif category_number == 4:
    total_price = 6.00 * user_tickets
    print(f"Cost before any discounts were applied: ${total_price:.2f}")
elif category_number == 5:
    total_price = 10.00 * user_tickets
    print(f"Cost before any discounts were applied: ${total_price:.2f}")
else:
    print("Please enter a valid category number.")

if user_tickets >= 4 and user_tickets <= 8:
    discount = total_price * .10
    final_discounted_price = total_price - discount
    print(f"Your cost after all discounts were applied: ${final_discounted_price:.2f}")
elif user_tickets >= 9 and user_tickets < 15:
    discount = total_price * .15
    final_discounted_price = total_price - discount
    print(f"Your cost after all discounts were applied: ${final_discounted_price:.2f}")
elif user_tickets >= 15:
    discount = total_price * .20
    final_discounted_price = total_price - discount
    print(f"Your cost after all discounts were applied: ${final_discounted_price:.2f}")

price_per_ticket = final_discounted_price / user_tickets
print(f"Your price per ticket is: ${price_per_ticket:.2f}")