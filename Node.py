from copy import deepcopy
import static


class Node:
    g = 0
    h = 0
    parent = None
    board = []
    positions = []
    prevBoard = []

    def __init__(self, parent, board, positions, prevBoard):
        self.parent = parent
        self.board = board
        self.positions = positions
        self.prevBoard = prevBoard

    def getHash(self):
        return tuple(self.positions)

    def expand(self):
        children = []
        if self.parent != None:
            prevBoard = self.parent.board
        else:
            prevBoard = []
        for i in range (static.numCars):
            #local
            position = self.positions[i]
            #global
            fixedPos = static.constantPos[i]
            orientation = static.orientations[i]
            carSize = static.lengths[i]

            for j in range(static.directions):
                if self.canMove(j, carSize, position, fixedPos, orientation):
                    newBoard, newPos = self.move(j,carSize,position,fixedPos,i)
                    if newBoard != self.prevBoard:
                        children.append(self.createSuccessor(newBoard, newPos))
        return children


    def createSuccessor(self, newBoard, newPos):
        return Node(self, newBoard, newPos, self.board)

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

#TODO remove
    def printBoard(self):
        for row in self.board:
            for element in row:
                print element,
            print ("\n")
        print("\n")
