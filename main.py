from astar import astar
from breadthFirst import bfs
from depthFirst import dfs
import node
import static
import visualisation


def readFromFile(fileName):
    numCars = 0
    readFile = []
    file = open(fileName,'r')
    for line in file:
        numCars +=1
        cur =[]
        for i in line.split(','):
            cur.append(int(i))
        readFile.append(cur)
    file.close()
    return readFile

def createState(readFile):
    constantPos = []
    currentPos = []
    orientations= []
    lengths = []
    board = [["." for i in range (6)] for i in range (6)]
    for i in range (len(readFile)):

        orientation = readFile[i][0]
        x=readFile[i][1]
        y=readFile[i][2]
        length = readFile[i][3]

        if orientation == 0:
            constantPos.append(y)
            currentPos.append(x)
        else:
            constantPos.append(x)
            currentPos.append(y)
        for j in range (length):
            #horisontal
            if orientation==0:
                board[y][x+j]=i

            #vertical
            else:
                board[y+j][x]=i

        orientations.append(orientation)
        lengths.append(length)

    return board, currentPos, constantPos, orientations, lengths, len(lengths)


def printBoard(board):
    for row in board:
        for element in row:
            print element,
        print ("\n")
    print("\n")

fileNames = ["easy-3.txt","medium-1.txt","hard-3.txt","expert-2.txt"]
algorithms = [bfs, dfs, astar]
algorithmsToPrint=["bfs", "dfs", "astar"]

def main():

    print("\nRUSH HOUR GAME \n")
    print("Choose board: ")
    for i in range(len(fileNames)):
        print(str(i) + ": "+fileNames[i])

    index = input()
    print("\n")
    board, positions, constantPos, orientations, lengths, numCars = createState(readFromFile(fileNames[index]))
    static.setVariables(constantPos, orientations, lengths, numCars)
    root = node.Node(None, board, positions, [])
    print("Choose algorithm: ")
    for i in range(len(algorithms)):
        print(str(i) + ": "+ str(algorithmsToPrint[i]))

    index = input()
    print (index)
    path, expanded = algorithms[index](root, 4)

    path, expanded = astar(root,4)
    print("Path length: ",len(path)-1)
    print("Expanded nodes: ", expanded)
    vis = visualisation.Visualisation(path,len(path)-1, expanded)


main()
