

def dfs(root, goal):
    print("DFS")
    visited, stack = set(), [root]
    while stack:
        current = stack.pop(0)
        if isSolution(current, goal):
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1], len(visited)
        successors = current.expand()
        #attach to parent
        for successor in successors:
            successor.parent = current
        pos = tuple(current.positions)
        if pos not in visited:
            visited.add(pos)
            stack = successors + stack
    return [], len(visited)


def isSolution(node, goal):
    return node.positions[0] == goal
