import static


def astar(start, goal):
    print("A*")
    opened = dict()
    closed = dict()
    #currentHash = start.getHash()
    opened[start[0]]=start[1]
    while opened:
        current = opened[min(opened, key = lambda n: opened[n].g + opened[n].h)]
        currentHash = current.getHash()
        if isSolution(current,goal):
            return constructPath(current), len(closed)
        opened.pop(currentHash)
        closed[currentHash]=current
        children = current.expand()
        for (key, node) in children:
            #nodeHash = node.getHash()
            if key in closed:
                #TODO update if lower values, children aswell
                print("Already expanded and closed")
            elif key in opened:
                newG = current.g + 1
                if node.g > newG:
                    node.g = newG
                    node.parent = current
            else:
                node.g = current.g +1
                node.h = heuristic(node, goal)
                node.parent = current
                opened[nodeHash]= node
    return [], len(closed)

def isSolution(node, goal):
    return node.positions[0]==goal

def constructPath(current):
    path = []
    while current.parent:
        path.append(current.positions)
        current = current.parent
    path.append(current.positions)
    #reverse the list, quicker than .reverse()
    return path[::-1]

def heuristic(node, goal):
    h = 0
    #Adds the number of moves from current position to the goal
    h+=goal-node.positions[0]
    #add the number of blocked spaces on way to goal
    for i in range(node.positions[0]+static.lengths[0],len(node.board)):
        if node.board[static.constantPos[0]][i] != '.':
            h +=1

    return h
