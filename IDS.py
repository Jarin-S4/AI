tree = {"A":["B", "C"],
    "B":["D", "E"],
    "C":["F","G"],
    "D":["H"],
    "E":["I"],
    "F":[],
    "G":["J"],
    "H":[],
    "I":[],
    "J":[]}
order = []
def dls(tree, node, goal, depth):

    order.append(node)

    if node == goal:
        return True

    if depth == 0:
        return False

    for neighbor in tree[node]:

        if dls(tree, neighbor, goal, depth - 1):
            return True

    return False


def ids(tree, start, goal):

    for depth in range(3):

        order.clear()

        if dls(tree, start, goal, depth):
            return depth


depth = ids(tree, "A", "G")

print(" -> ".join(order))