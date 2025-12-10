# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    round_trip = one_way_km * 2                  # Total distance
    total_fuel = round_trip / km_per_liter       # Total fuel needed = total distance / fuel usage per 1 km
    total_cost = total_fuel * price_per_liter    
    if total_cost <= budget:
        return True
    else:
        return False

# Test your code here
print("Testing Road Trip Budgeter...")
print(is_budget_sufficient(100, 10, 2.0, 40))
