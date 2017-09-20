from Tkinter import *

rows = 0
cols = 0
canvas = None
board = None


def timerFired(canvas):
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

def update(node):
    global board
    print "hei"
    assumedVariables = node.assumedVariables
    assumedValues = node.assumedValues
    board = [[0 for i in range(len(cols))] for j in range(len(rows))]
    for variable, value in zip(assumedVariables, assumedValues):
        if variable[0]==0:
            x  = value
            y = rows-variable[1]-1
            for i in range(variable[3]):
                board[y][x+i]=1
        else:
            y  = rows-value-1
            x = variable[1]
            for i in range(variable[3]):
                board[y-i][x]=1
    root.update()
    redrawAll()

def redrawAll():
    canvas.delete(ALL)
    drawboard(canvas, board)


def drawboard(canvas, board):
    board = canvas.data["board"]
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, board, row, col)

def drawCell(canvas, board, row, col):
    margin = 5
    cellSize = 30
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill="white")
    if (board[row][col] > 0):
        canvas.create_rectangle(left, top, right, bottom, fill="blue")

def loadboard(canvas):
    global board
    board = [ [ 0 for i in range (cols)] for j in range (rows) ]
    canvas.data["board"] = board


def init(canvas):
    loadboard(canvas)
    redrawAll()


def run(numRows, numCols):
    global rows, cols, canvas
    rows = numRows
    cols = numCols
    print rows, cols
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=310, height=310)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)

    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
