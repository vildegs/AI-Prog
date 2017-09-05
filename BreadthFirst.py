def main():
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

    while current.parent != None:

        current= current.parent
        path.append(current.board)

    for i in range(len(path)-1,-1,-1):
        printBoard(path[i])
    print("Path length: ",len(path))
    print("Visited nodes: ", len(visited))
    #visualisation(root,path)
