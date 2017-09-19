

def bfs(root,goal):
    print("BFS")
    visited, opened = set(), [root]
    path = []
    while opened:
        print(len(visited))
        current = opened.pop(0)
        if isSolution(current, goal):
            path = []
            while current.parent:
                path.append(current.positions)
                current = current.parent
            path.append(current.positions)
            return path[::-1], len(visited)
        pos = tuple(current.positions)
        if pos not in visited:
            visited.add(pos)
            print("Riktig",len(current.expand()))
            opened.extend(current.expand())
    return path, len(visited)

def isSolution(node, goal):
    return node.positions[0] == goal
