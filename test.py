

'''
def printBoard(board):
    for row in board:
        for element in row:
            print element,
        print ("\n")


def main ():
    readFile = readFromFile()
    state = createState(readFile)
    printBoard(state)
    print(constantPos)
    print(currentPos)
    print(lengths)
    print(orientations)

    opened = [state]
    closed = []
    while len(opened) != 0:
        cur = opened.pop()
        closed.append(cur)
        printBoard(cur)
        if isSolution(cur):
            break
        newStates = possStates(cur)
        for possState in range newStates:
            opened.append(possState)

def expand(state):
    states = []

    for i in range (numCars):
        position = currentPos[i]
        fixedPos = constantPos[i]
        orientation = orientations[i]
        carSize = lengths[i]

        #move horisontal
        if orientation == 0:
            if canMove(board,0,carSize,position,fixedPos):
                states.append(move())
            elif canMove(board,1,carSize,position,fixedPos):
                states.append(move)
        #move vertical
        else:
            if canMove(board,2,carSize,position,fixedPos):
                states.append()
            elif canMove(board,3,carSize,position,fixedPos):
                print("Hello")

def move(board, direction, carSize, position, fixedPos, carNum):
    #left
    if direction ==0:
        board[position-1][fixedPos] = carNum
        board[position+carSize][fixedPos] = '.'
    #right
    elif direction ==1:
        board[position+carSize][fixedPos] = carNum
        board[position][fixedPos] = '.'
    #up
    elif direction ==2:
        board[position-1][fixedPos] =carNum
        board[position+carSize-1][fixedPos] = '.'
    #down
    elif direction ==3:
        board[position+carSize][fixedPos] = carNum
        board[position-1][fixedPos] = '.'

    return board

def canMove(board, direction, carSize, position, fixedPos):
    #left
    if direction ==0 and position>0 :
        return board[fixedPos][position-1]=='.'
    #right
    elif direction ==1 and position+carSize<5:
        return board[fixedPos][position+carSize]=='.'
    #up
    elif direction ==2 and position>0 :
        return  board[position-1][fixedPos]=='.'
    #down
    elif direction ==3 and position < 5 :
        return  board[position+carSize][fixedPos]=='.'
    else:
        return False

def test():
    readFile = readFromFile()
    state = createState(readFile)
    state[1][0] = 6
    state[2][0] = 6
    printBoard(state)
    #print(canMove(state, 0,2,4,1 ))
    #print(canMove(state, 1,2,4,1 ))
    print(canMove(state, 2,2,1,0 ))
    print(canMove(state, 3,2,1,0 ))
    move(state, 2, 2, 1, 0, 6)
    printBoard(state)


test ()

def isSolution(state):
    return
'''

#The way I chose to compute the latter, is to get the distance of the red car from the exit, and then add 1 for every vehicle in the way, since it has to be moved at least once in order to clear the way. When I replace the lower bound calculation with a constant 0, I get a regular BFS behavior.
'''
def printState(state):
    board = [["." for i in range (6)] for i in range (6)]
    for i in range (len(state)):
        x=state[i][1]
        y=state[i][2]
        for j in range (state[i][3]):
            if state[i][0]==0:
                board[y][x+j]=i
            else:
                board[y+j][x]=i
    printBoard(board)



def astar():
    #contains
    closedSet =
    #contains the nodes found but not yet expanded
    openSet =

def heuristic():
    #TODO define heuristic function
    return 0

def moves (state):
    return posMoves

#main()
'''
