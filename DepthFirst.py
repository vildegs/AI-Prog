

def dfs(root, goal):
    visited, queue = set(), [root]
    path = []
    while queue:
        current = queue.pop()
        if isSolution(current, goal):
            path = []
            while current.parent:
                path.append
                current = current.parent
            path.append(current)
            return path[::-1], len(visited)
        if current not in visited:
            visited.add(current)
            queue.append(current.expand())

    return path, len(visited)


def isSolution(node, goal):
    return node.positions[0] == goal
