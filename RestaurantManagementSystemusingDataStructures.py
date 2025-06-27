import numpy as np

# Menu using tuple
menu = (("Idli", 30), ("Dosa", 50), ("Puri", 40))

# Set of available tables
tables = {1, 2, 3}

# Empty orders list
orders = []

# Show menu
print("Menu:")
for item in menu:
    print(item[0], "-", item[1], "Rs")

# Take one order (simple)
t = int(input("Enter table number: "))
i = input("Enter item name: ")
q = int(input("Enter quantity: "))

# Check and add order
for m in menu:
    if m[0].lower() == i.lower():
        p = m[1]
        orders.append([t, i, q, p])
        print("Order added:", i, "x", q, "for Table", t)

# Generate bill for that table
print("\nBill for Table", t)
total = 0
for o in orders:
    if o[0] == t:
        a = o[2] * o[3]
        print(o[1], "x", o[2], "=", a, "Rs")
        total += a
print("Total =", total, "Rs")
