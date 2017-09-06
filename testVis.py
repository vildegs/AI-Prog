import visualisation
import static
from copy import deepcopy

path = [[['.' for i in range(6)] for j in range (6)] for k in range(2)]

def readFromFile():
    numCars = 0
    readFile = []
    #file = open("expert-2.txt",'r')
    #file = open("hard-3.txt",'r')
    #file = open("medium-1.txt", 'r')
    file = open ("easy-3.txt", 'r')
    for line in file:
        numCars +=1
        cur =[]
        for i in line.split(','):
            cur.append(int(i))
        readFile.append(cur)
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

def main():
    board, positions, constantPos, orientations, lengths, numCars = createState(readFromFile())
    static.setVariables(constantPos,orientations ,lengths , numCars)
    newpositions = deepcopy(positions)
    newpositions[0]=1
    vis = visualisation.Visualisation([positions, newpositions])


main()
