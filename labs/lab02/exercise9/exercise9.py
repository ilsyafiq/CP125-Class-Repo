# Lab 02 Exercise 9: Level Up Calculator
# Write your code below:

def calculate_xp_required(current_level):
    XP_needed = current_level * 100
    return XP_needed

def can_level_up(xp_remaining, xp_required):
    if xp_remaining >= xp_required:
        return True
    else:
        return False

def simulate_leveling(total_xp):
    while can_level_up(total_xp, calculate_xp_required(level)):
        xp_remaining = total_xp
        while can_level_up(xp_remaining, calculate_xp_required(level)):
            xp_needed = calculate_xp_required(level)
            xp_remaining -= xp_needed
            level += 1
        return (level, xp_remaining)

# Test your code here
print("Testing Level Up Calculator...")
