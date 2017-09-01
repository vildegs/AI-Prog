from copy import deepcopy
from test import readFromFile, createState
from visualisation import *

class Node:
    depth = None
    parent = None
    board = []
    positions = []
    prevBoard = []

    def __init__(self, parent, depth, board, positions, prevBoard):
        self.parent = parent
        self.depth = depth
        self.board = board
        self.positions = positions
        self.prevBoard = prevBoard

    def expand(self):
        if self.parent != None:
            prevBoard = self.parent.board
        else:
            prevBoard = []
        for i in range (numCars):
            #local
            position = self.positions[i]
            #global
            fixedPos = constantPos[i]
            orientation = orientations[i]
            carSize = lengths[i]


            for j in range(directions):
                if self.canMove(j, carSize, position, fixedPos, orientation):
                    newBoard, newPos = self.move(j,carSize,position,fixedPos,i)
                    self.createSuccessor(newBoard, newPos)

    def createSuccessor(self, newBoard, newPos):
        if (newBoard != self.prevBoard and newBoard not in visited):
            opened.append( Node(self,self.depth+1, newBoard, newPos, self.board))
            visited.append(newBoard)

    def move(self, direction, carSize, position, fixedPos, carNum):
        newBoard = deepcopy(self.board)
        newPos = deepcopy(self.positions)
        #left
        if direction ==0:
            newBoard[fixedPos][position-1] = carNum
            newBoard[fixedPos][position+carSize-1] = '.'
            newPos[carNum] -=1
        #right
        elif direction ==1:
            newBoard[fixedPos][position+carSize] = carNum
            newBoard[fixedPos][position] = '.'
            newPos[carNum] +=1
        #up
        elif direction ==2:
            newBoard[position-1][fixedPos] =carNum
            newBoard[position+carSize-1][fixedPos] = '.'
            newPos[carNum] -=1
        #down
        elif direction ==3:
            newBoard[position+carSize][fixedPos] = carNum
            newBoard[position][fixedPos] = '.'
            newPos[carNum] +=1

        return newBoard, newPos



    def canMove(self, direction, carSize, position, fixedPos, orientation):
        #left
        if orientation ==0:
            if direction ==0 and position>0 :
                return self.board[fixedPos][position-1]=='.'
            #right
            elif direction ==1 and position+carSize<6:
                return self.board[fixedPos][position+carSize]=='.'
            else:
                return False
        else:
            #up
            if direction ==2 and position>0 :
                return  self.board[position-1][fixedPos]=='.'
            #down
            elif direction ==3 and position+carSize < 6:
                return  self.board[position+carSize][fixedPos]=='.'
            else:
                return False

    def printBoard(self):
        for row in self.board:
            for element in row:
                print element,
            print ("\n")
        print("\n")

def printBoard(board):
    for row in board:
        for element in row:
            print element,
        print ("\n")
    print("\n")

example= []
numCars= None
lengths = []
orientations = []
carSize = []
constantPos = []
opened = []
closed = []
visited= []
directions = 4

def isSolution(node):
    return node.positions[0]==4

def main():
    '''example = [['.' for i in range (6)] for j in range (6)]
    example[0][2] = 1
    example[0][1]= 1
    example[3][3] =0
    example[4][3] =0
    example[2][3]= 0'''

    global numCars, constantPos, orientations, lengths, visited
    example, positions, constantPos, orientations, lengths, numCars = createState(readFromFile())
    visited.append(example)
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
    visualisation(root,path)



main()
