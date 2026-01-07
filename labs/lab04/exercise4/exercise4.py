import math

def calc_average(lap_times_half):
    return sum(lap_times_half) / len(lap_times_half)

def analyze_performance(lap_times):
    divider = math.ceil(len(lap_times)/2)
    first_half = lap_times[:divider]
    second_half = lap_times[divider:]

    if calc_average(second_half) > calc_average(first_half):
        return True
    else:
        return False



# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
