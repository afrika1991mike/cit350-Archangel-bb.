# Input
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Display subtotal
print("\nSubtotal: $", round(subtotal, 2))

# Input sales tax rate
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Compute sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Compute total price
total_price = subtotal + sales_tax

# Display sales tax
print("Sales Tax: $", round(sales_tax, 2))

# Display total price
print("Total: $", round(total_price, 2))

# Enter payment amount and compute change
payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - total_price

# Display change
print("Change: $", round(change, 2))