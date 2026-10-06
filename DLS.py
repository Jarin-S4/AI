tree = {"A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G","H"],
    "E": ["I"],
    "F": ["J"],
    "G": [],
    "H":[],
    "I":[],
    "J":[]}

def dls(tree, node, goal, depth):
    print(node, end=" ")

    if node == goal:
        return True

    if depth == 0:
        return False

    for neighbor in tree[node]:
        if dls(tree, neighbor, goal, depth - 1):
            return True

    return False

dls(tree,"A","F",2)