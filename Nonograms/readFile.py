
numcols = 0
numrows = 0
def readFile(filename):
    global numrows, numcols
    doc = []
    file = open(filename,'r')
    numcols, numrows = map(int, file.readline().split())
    for line in file:
        num = map(int, line.split())

        doc.append(num)
    file.close()
    return doc

def initVariables(doc):
    variables = []
    for i in range(len(doc)):
        if 
        for j in range(len(doc[i])):
            variables.append((i,j))
    return variables

def initDomains(variables, doc):
    domains = {}
    count = 0
    for i in range(len(doc)):
        for j in range(len(doc[i])):
            numSegments = len(doc[i])
            sumSegments = sum(doc[i])
            domains[variables[count]] = domain(j, doc[i], sumSegments, numSegments, i)
            count +=1
    return domains

def domain(index, segments, sumSegments, numSegments, id):
    if id < numrows:
        length = numcols
    else:
        length = numrows
    #first
    '''if index == 0:
        dom = [i for i in range(length-numSegments-sumSegments)]
    #last
    elif index == numSegments-1:
        dom = [i for i in range(sumSegments+numSegments-segments[index]-1,length-segments[index]+1)]
    #other
else:'''
    left = segments[:index]
    right = segments[index+1:]
    leftlim = sum(left)+len(left)
    rightlim = length-(sum(right)+len(right))-segments[index]+1
    dom = [i for i in range(leftlim, rightlim)]
    return dom

def initConstraints():


def main():
    print(readFile("easyExample.txt"))
    doc = readFile("easyExample.txt")
    #print(initDomains(numrows, numcols))
    variables = initVariables(doc)
    domains= initDomains(variables, doc)
    print(domains)
    for i in range(len(domains)):
        print (variables[i],)
        print(domains[variables[i]])

main()
