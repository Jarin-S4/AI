tree={"A":["B","C"],
"B":["D","E"],
"C":["F","G"],
"D":[],
"E":[],
"F":[],
"G":[]}

def dfs(tree, root):
    visited = set()
    stack = []

    stack.append(root)

    while stack:
        child = stack.pop()

        if child not in visited:
            print(child, end=" ")
            visited.add(child)

            for neighbor in reversed(tree[child]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
dfs(tree,"A")