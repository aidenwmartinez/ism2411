# Exercise 1: Build the list

inventory =["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3: Slicing

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Modify the List

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5: Tuple Comparison

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed.")
    print("This is useful for coordinates because it keeps them the same.")

print(coords)

# Exercise 6: Average of a List of Sales

sales = [100, 250, 75, 480, 200]

print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))

#Exercise 7: Accumulator Pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:" , prices)
print("Discounted:", discounted)

# Exercise 8: Filter the Above Threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))


# Reflection
#
# 1. The most surprising thing was how easy it is to
# change a list in Python. I thought it would be harder
# to add and remove items, but it only takes one command.
#
# 2. In a business class, Python lists could help me
# keep track of sales from different days. Instead of
# adding everything manually in Excel, I could use
# Python to find the total and average much faster.
