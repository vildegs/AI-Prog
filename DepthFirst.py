

def dfs(root, goal):
    visited, stack = set(), [root]
    while stack:
        current = stack.pop(0)
        if isSolution(current, goal):
            print("Solution found!")
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1], len(visited)
        children = current.expand()
        #for i in children:
        #    print(i.positions,)
        pos = tuple(current.positions)
        if pos not in visited:
            visited.add(pos)
            stack = children[::-1] + stack
    return [], len(visited)


def isSolution(node, goal):
    return node.positions[0] == goal
