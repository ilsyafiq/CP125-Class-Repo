def was_backward_detected(waypoints):
    for i in range (1, len(waypoints)):
        if waypoints[i][0] < waypoints[i-1][0] or waypoints[i][1] < waypoints[i-1][0]:
            return True
        
    return False

# Test
path = ((0, 0, 0), (1, 2, 3), (2, 4, 6))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
