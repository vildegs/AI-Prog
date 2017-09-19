from cellConstraint import Cell
from rowcolConstraint import RowCol
from GAC import gac
numcols = 0
numrows = 0


def readFile(filename):
    global numrows, numcols
    rows, cols , doc= [], [], []
    file = open(filename,'r')
    numcols, numrows = map(int, file.readline().split())
    counter = 0
    for line in file:
        num = map(int, line.split())
        if counter<numrows:
            rows.append(num)
        else:
            cols.append(num[::-1])
        doc.append(num)
        counter+=1
    file.close()
    return rows, cols

def initVariables(rows, cols):
    variables = []
    for i in range(len(rows)):
        for j in range (len(rows[i])):
            variables.append((0,i,j,rows[i][j]))
    for i in range(len(cols)):
        for j in range(len(cols[i])):
            variables.append((1,i,j,cols[i][j]))
    return variables

def initDomains(variables, rows, cols):
    domains = {}
    count = 0
    print rows
    print cols
    for i in range(len(rows)):
        for segNr in range(len(rows[i])):
            numSegments = len(rows[i])
            sumSegments = sum(rows[i])
            domains[variables[count]] = domain(segNr, rows[i], numcols)
            count +=1
    for i in range(len(cols)):
        for segNr in range(len(cols[i])):
            numSegments = len(cols[i])
            sumSegments = sum(cols[i])
            domains[variables[count]] = domain(segNr, cols[i], numrows)
            count +=1
    return domains

def domain(segNr, segments, max):
    length = segments[segNr]
    before = segments[:segNr]
    after = segments[segNr+1:]
    beforelim = sum(before)+len(before)
    afterlim = max -length-sum(after)-len(after)+1
    dom = [i for i in range(beforelim, afterlim)]
    return dom

def initConstraints(variables):
    constraints = []
    for i in range (numrows):
        affectedVar = []
        for variable in variables:

            if variable[0] == 0 and variable[1]==i:
                affectedVar.append(variable)
        constraints.append(RowCol(0,i, affectedVar))
    for i in range(numcols):
        affectedVar = []
        for variable in variables:

            if variable[0] == 1 and variable[1]==i:
                affectedVar.append(variable)
        constraints.append(RowCol(1,i, affectedVar))


    for i in range(numrows):
        for j in range(numcols):
            affectedVar = []
            affectedVar = filter(lambda var: (var[0]==0 and var[1]==i) or (var[0]==1 and var[1]==j), variables)
            #print i, j, affectedVar
            constraints.append(Cell(j,i,affectedVar))

    return constraints

def printDomains(domains):
    for key in domains.keys():
        print (key, domains[key])

def main():
    rows,cols = readFile("example.txt")
    variables = initVariables(rows, cols)
    rowVar = filter(lambda var: var[0]==0, variables)
    colVar = filter (lambda var: var[0]==1, variables)
    domains= initDomains(variables, rows, cols)
    constraints = initConstraints(variables)
    #printDomains(domains)
    path, expanded = gac(variables, domains,constraints)
    #printDomains(path[len(path)-1].domains)
    if path:
        print "Solution"
        printDomains(path.domains)
        #showSolution(path[len(path)-1], rows, cols)
    else:
        print "Could not find solution"


def showSolution(sol, rows, cols):
    board = [['.' for i in range(len(cols))] for j in range(len(rows))]

    print len(cols)
    print len(rows)
    print "y:",len(board)
    print "x: ",len(board[0])
    for variable in sol.domains:
        if variable[0]==0:
            #print sol.domains[variable][0]
            x  = sol.domains[variable][0]
            y = len(rows)-variable[1]-1
            for i in range(variable[3]):
                board[y][x+i]='x'
        else:
            #print sol.domains[variable]
            y  = len(rows)-sol.domains[variable][0]-1
            #print y
            x = variable[1]
            #print "x" ,x
            print variable[3]
            for i in range(variable[3]):
                print "y", y-i
                print "x", x
                print(board[8][7])
                board[y-i][x]='x'
                print "y", y-i
                print "x", x



    for i in range(len(board)):
        for j in range(len(board[i])):
            print board[i][j],
        print " "


main()
