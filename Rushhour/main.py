
from astarRushHour import RushHour
from breadthFirst import bfs
from depthFirst import dfs
from node import Node
import static
from visualisation import Visualisation


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
        #horisontal
        if orientation == 0:
            constantPos.append(y)
            currentPos.append(x)
        #vertical
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


fileNames = ["easy-3","medium-1","hard-3","expert-2"]
algorithmsToPrint=["bfs", "dfs", "astar"]

def main():

    print("\nRUSH HOUR GAME \n")
    print("Choose board: ")
    for i in range(len(fileNames)):
        print(str(i) + ": "+fileNames[i])
    index = input()
    print("\n")
    board, positions, constantPos, orientations, lengths, numCars = createState(readFromFile("inputFiles/"+fileNames[index]+".txt"))
    static.setVariables(constantPos, orientations, lengths, numCars)
    root = Node(board, positions, [])
    search = RushHour()
    astar = search.astar
    algorithms = [bfs, dfs, astar]
    print("Choose algorithm: ")
    for i in range(len(algorithms)):
        print(str(i) + ": "+ str(algorithmsToPrint[i]))
    index2 = input()
    print ""
    print "Algorithm: ",algorithmsToPrint[index2]
    print "Board: ", fileNames[index]
    print ""

    path, expanded = algorithms[index2](root, 4)
    print("Path length: ",len(path)-1)
    print("Expanded nodes: ", expanded)
    vis = Visualisation(path,len(path)-1, expanded)

main()
