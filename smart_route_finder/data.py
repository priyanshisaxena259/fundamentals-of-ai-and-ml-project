import heapq
from graph_data import graph, heuristic
from visualize import visualize_graph

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, 0, []))

    visited = set()

    while open_list:
        f, node, g, path = heapq.heappop(open_list)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        print(f"\nVisiting: {node}")
        print(f"g(n): {g}, h(n): {heuristic[node]}, f(n): {f}")

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]

                heapq.heappush(open_list, (f_new, neighbor, g_new, path))

    return None, None


print("Available cities:", list(graph.keys()))

start = input("Enter start city: ").strip()
goal = input("Enter destination city: ").strip()

if start not in graph or goal not in graph:
    print("Invalid city name!")
    exit()

path, cost = a_star(start, goal)

if path:
    print("Shortest Path:", " → ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found!")

visualize_graph(path)
