

def readFile(filename):
    readFile = []
    file = open(filename,'r')
    numcols, numrows = map(int, file.readline().split())
    print(numcols)
    print(numrows)

    for line in file:
        readFile.append(line.strip() +",")
    file.close()
    return numrows, numcols
def initVariables(numrows, numcols):
    variables = []
    for i in range(numcols):
        for j in range(numrows):
            variables.append((i,j))
    return variables

def initDomains(numrows, numcols):
    domains = {}
    for i in range(numcols):

        for j in range(numrows):
            domains[(i,j)]=[0,1]
    return domains

def main():
    print(readFile("nono-cat.txt"))
    numrows, numcols = readFile("nono-cat.txt")
    print(initDomains(numrows, numcols))
    print(initVariables(numrows, numcols))
main()
