graph = {"A":[("B",9),("C",4)],
         "B":[("C",2),("D",7),("E",3)],
         "C":[("D",1),("E",6)],
         "D":[("E",4),("F",8)],
         "E":[("F",2)],
         "F":[("D",8),("E",2)]}
start = "A"
goal = "F"
queue = [(0, start, [start])]

while queue:

    queue.sort()

    cost, node, path = queue.pop(0)

    if node == goal:
        print(" -> ".join(path))
        print("Total Cost =", cost)
        break

    for neighbor, edge_cost in graph[node]:

        new_cost = cost + edge_cost
        new_path = path + [neighbor]

        queue.append((new_cost, neighbor, new_path))