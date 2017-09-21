

def bfs(root,goal):
    visited, opened = set(), [root]
    path = []
    while opened:
        current = opened.pop(0)
        if isSolution(current, goal):
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1], len(visited)
        pos = tuple(current.positions)
        if pos not in visited:
            visited.add(pos)
            successors = current.expand()
            #attach to parent
            for successor in successors:
                successor.parent = current
                opened.append(successor)
    return path, len(visited)

def isSolution(node, goal):
    return node.positions[0] == goal
