

def astar(start, goal, board):
    opened = set()
    closed = set()
    current = start
    opened.add(current)
    while opened:
        current = min(opened, key = lambda n: n.g + n.h)
        if isGoal(current):
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            #reverse the list, quicker than .reverse()
            return path[::-1]
        opened.remove(current)
        closed.append(current)
        for node in expand(current, board):
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
    return []




def heuristic():
    h = 0
    h+=4-positions1[0]
    for i in range(positions1[0]+carSize1-1):
        if board1[fixedPos1[0]][positions1[0]+carSize1+i] != '.':
            h +=1
    return h

board1 = [['.' for i in range(6)] for j in range (6)]

fixedPos1 = [2, 2]
positions1= [0, 2]
carSize1 = 2
board1[2][0], board1[2][1] = 0, 0
board1[2][2], board1[3][2] = 1, 1


def main():
    print(heuristic())


main()
