<<<<<<< HEAD
def bfs():
    global numCars, constantPos, orientations, lengths
    example, positions, constantPos, orientations, lengths, numCars = createState(readFromFile())
    root = Node(None, 0, example, positions, [])
    opened.append(root)
    print("ROOT")
    root.printBoard()
    while len(opened) != 0:
        current = opened.pop(0)
        if isSolution(current):
            print("Hurra")
            current.printBoard()
            break
        current.expand()
        closed.append(current)
        #current.printBoard()
    path = [current.board]
=======
>>>>>>> 3238d6b39adc3f86c3c2f7e38a86e511e5d42969


def bfs(root,goal):
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
            opened.extend(current.expand())

    return path, len(visited)

def isSolution(node, goal):
    return node.positions[0] == goal
