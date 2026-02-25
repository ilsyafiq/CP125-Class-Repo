def process_actions(catalog, actions):
    for action in actions:
        if action[0] == "BORROW":
            if action[1] in catalog and catalog[action[1]] > 0:
                catalog[action[1]] -= 1
        elif action[0] == "RETURN":
            if action[1] in catalog:
                catalog[action[1]] += 1
        
    return catalog



catalog = {
    "978-A": 2,
    "978-B": 0,
    "978-C": 1,
}
actions = [
    ("BORROW", "978-A"),
    ("BORROW", "978-A"),
    ("BORROW", "978-B"),
    ("RETURN", "978-B"),
    ("BORROW", "978-Z"),
]
result = process_actions(catalog, actions)
print(result)
