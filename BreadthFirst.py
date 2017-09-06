

def bfs(root,goal):
    visited, opened = set(), [root]
    path = []
    while opened:
        print(len(visited))
        current = opened.pop(0)
        #print(current)
        #print(len(opened))
        #print("------------------")
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
            opened.extend(current.expand())

    return path, len(visited)

def isSolution(node, goal):
    return node.positions[0] == goal
