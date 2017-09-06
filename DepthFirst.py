

def dfs(root, goal, visited = None, stack = None):
    if visited == None and stack == None:
        visited, stack = set(), [root]
    while stack:
        current = stack.pop()
        if isSolution(current, goal):
            print("Solution found!")
            path = []
            while current.parent:
                path.append
                current = current.parent
            path.append(current)
            return path[::-1], len(visited)
        children = current.expand()
        pos = tuple(current.positions)
        visited.add(pos)
        for node in children:
            pos = tuple(node.positions)
            if pos not in visited:
                dfs(node, goal, visited, stack+[node])
        #if pos not in visited:
        #    visited.add(pos)
        #    queue.extend(current.expand())
    return [], len(visited)


def isSolution(node, goal):
    return node.positions[0] == goal
