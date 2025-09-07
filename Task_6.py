# The program to calculates and returns the unit price of the pizza.

import math

# Function to calculate price per square meter
def unit_price_per_sqm(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100 # Convert cm to meters
    area_sqm = math.pi * radius_m ** 2 # Area in square meter
    unit_price = price_eur / area_sqm
    return unit_price

# Main program
print("Enter details for Pizza 1:")
d1 = float(input("diameter (cm): "))
p1 = float(input("diameter (euros): "))

print("\nEnter details for Pizza 2:")
d2 = float(input("diameter (cm): "))
p2 = float(input("diameter (euros): "))

# Calculate unit price
unit_price1 = unit_price_per_sqm(d1, d2)
unit_price2 = unit_price_per_sqm(p1, p2)

print(f"\nPizza 1 unit price: {unit_price1:.2f} euros/sqm")
print(f"Pizza 2 unit price: {unit_price2:.2f} euros/sqm")

# Price comparison
if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money")
else:
    print("Both pizzas provide better value for money")

