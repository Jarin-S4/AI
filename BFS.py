tree={"A":["B","C"],
"B":["D","E"],
"C":["F","G"],
"D":[],
"E":[],
"F":[],
"G":[]}

def bfs(tree, root):
    visited = set()
    queue = []

    queue.append(root)

    while queue:
        child = queue.pop(0)

        if child not in visited:
            print(child, end=" ")
            visited.add(child)

            for neighbor in tree[child]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(tree,"A")