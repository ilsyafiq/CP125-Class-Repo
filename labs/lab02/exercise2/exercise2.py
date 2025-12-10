# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    total_tent_cost = math.ceil((participants / tent_capacity)) * tent_price
    total_meal_price = participants * meal_price
    total_budget = total_tent_cost + total_meal_price
    return total_budget

# Test your code here
print("Testing Camping Logistics...")

