def filter_query_times(times):
    
    if len(times) ==0:
        return []
    
    mean = sum(times)/len(times)
    variance = sum((x - mean) ** 2 for x in times) / len(times)
    std_dev = variance**0.5

    for time in times[:]:
        if time > mean + std_dev:
            times.remove(time)
    
    times.sort()
    return times


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
