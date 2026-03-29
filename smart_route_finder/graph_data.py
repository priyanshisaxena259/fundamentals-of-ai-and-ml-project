# Graph (city connections with cost)
graph = {
    'Delhi': [('Bhopal', 10), ('Jaipur', 8)],
    'Bhopal': [('Indore', 5), ('Nagpur', 7)],
    'Jaipur': [('Indore', 6), ('Nagpur', 9)],
    'Indore': [('Mumbai', 4)],
    'Nagpur': [('Mumbai', 3), ('Jaipur', 9)],
    'Mumbai': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'Delhi': 15,
    'Bhopal': 10,
    'Jaipur': 12,
    'Indore': 5,
    'Nagpur': 6,
    'Mumbai': 0
}