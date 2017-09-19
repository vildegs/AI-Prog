
from constraint import Constraint

class Board(Constraint):

    rows = []
    cols = []
    board = []

    def __init__(self, variables, numRows, numCols):
        Constraint.__init__(self,variables)
        self.numRows = numRows
        self.numCols = numCols
        self.rows = [0 for i in range(numRows)]
        self.cols = [0 for i in range(numCols)]
        self.initBoard()

    def initBoard(self):
        for variable in self.variables:
            if variable[0]==0:
                self.rows[variable[1]]+=variable[3]
            else:
                self.cols[variable[1]]+=variable[3]

    def makeBoard(self, fixedVar, domains):
        self.board = [[0 for i in range (self.numCols)] for j in range(self.numRows)]
        for variable in fixedVar:
            length = variable[3]
            if variable[0]==0:
                row = variable[1]
                col = domains[variable][0]
                for i in range(length):
                    self.board[row][col+i]=1
            else:
                col = variable[1]
                row = domains[variable][0]
                for i in range(length):
                    self.board[row+i][col]=1



    def toString(self):
        print ""
        print "BoardConstraint"
        print "Variables: ",self.variables

    def isValid(self, variable, value, domains):
        fixedVar = filter(lambda var: len(domains[var])==1, domains)
        self.makeBoard(fixedVar,domains)

        length = variable[3]
        if variable[0]==0:
            row = variable[1]
            col = value
            for i in range(length):
                self.board[row][col+i]=1
        else:
            col = variable[1]
            row = value
            for i in range(length):
                self.board[row+i][col]=1

        for i in range(self.numRows):
            if (sum(self.board[i])>self.rows[i]):
                return False
        for i in range(self.numCols):
            cursum = 0
            for j in range (self.numRows):
                cursum +=self.board[j][i]
            if cursum>self.cols[i]:
                return False
        return True
