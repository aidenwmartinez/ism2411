# Exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50 ; an example to show how to enter variables without making them variables because you can enter them into the function

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final Price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 6

x = 100  # global variable

def double_it() :
    x = 999  # local variable - different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?


# Reflection Questions

# Reflection Question 1: In Exercise 5 (Debug First, Then Ask), what was the first bug you spotted? Did you find it from 
# the traceback, from a print() statement, from explaining the code out loud to the duck, or only after asking AI? 
# What does that tell you about your current debugging instincts?

# In excercise 5, the first bug I spotted was that the total variable was being overwritten with the current sale 
# value instead of being accumulated. I found this bug by explaining the code out loud to the duck. This tells me 
# that my debugging instincts are improving, as I am able to identify issues by reasoning through the code and its 
# logic.

# Reflection Question 2: Without looking at your code, explain in plain English what apply_discount(price, tier) 
# does, what its inputs are, and what it returns. Could a colleague use it without reading the body?

# The apply_discount function takes two inputs: price, which is a numerical value representing the original price 
# of an item, and tier, which is a string that indicates the discount tier (gold, silver, bronze, or none). 
# The function checks the tier and applies the corresponding discount to the price. It returns the discounted 
# price as a numerical value. A colleague could use this function without reading the body by understanding that 
# it calculates the final price after applying a discount based on the specified tier.

# Reflection Question 3: If you used AI on any part of today's lab, write the disclosure comment you would add to 
# the top of your file. Then reflect: did the AI use build your understanding, or did it shortcut it?

# I used AI to help me understand the accumulator pattern and how to properly iterate through a list without going 
# out of bounds. The AI provided explanations and examples that helped me grasp the concepts more quickly. However, 
# I also made sure to reason through the code and debug it myself, which reinforced my understanding. Overall, the 
# AI use built my understanding rather than shortcutting it, as it guided me to think critically about the code 
# and its logic.