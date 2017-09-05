import static


def astar(start, goal, board):
    opened = set()
    closed = set()
    current = start
    opened.add(current)
    while opened:
        current = min(opened, key = lambda n: n.g + n.h)
        if isSolution(current,goal):
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            #reverse the list, quicker than .reverse()
            return path[::-1], len(closed)
        opened.remove(current)
        closed.add(current)
        for node in current.expand():
            if node in closed:
                #TODO update if lower values, children aswell
                continue
            if node in opened:
                newG = current.g + 1
                if node.g > newG:
                    node.g = newG
                    node.parent = current
            else:
                node.g = current.g +1
                node.h = heuristic(node, goal)
                node.parent = current
                opened.add(node)
    return [], len(closed)

def isSolution(node, goal):
    return node.positions[0]==goal

def heuristic(node, goal):
    h = 0
    h+=goal-node.positions[0]
    for i in range(node.positions[0]+static.lengths[0],len(node.board)):
        if node.board[static.constantPos[0]][i] != '.':
            h +=1
    return h

'''
board1 = [['.' for i in range(6)] for j in range (6)]

fixedPos1 = [2, 2]
positions1= [0, 2]
carSize1 = 2
board1[2][0], board1[2][1] = 0, 0
board1[2][2], board1[3][2] = 1, 1


def main():
    print(heuristic())


main()
'''
