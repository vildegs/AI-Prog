from copy import deepcopy


class Node:
    variable = None
    g = 0
    h = 0
    parent = None
    assumed =[]
    domains = {}

    def __init__(self, domains, g = 0, parent =None,variable=None, assumedVariables= [], assumedValues=[]):
        self.g = g
        self.parent = parent
        self.domains = domains
        self.variable = variable
        self.assumedVariables = assumedVariables
        self.assumedValues = assumedValues
        self.children = []

    def updateChildren(self, g):
        self.g = g
        for child in children:
            if g + 1 < child.g:
                child.updateChildren(g+1)

    def toString(self):
        print "Variable: ", self.variable
        print "Parent: ", self.parent
        print "Domains: ", self.domains
        print "f-value",self.g + self.h
        for i in range (len(self.assumedVariables)):
            print self.assumedVariables[i], ": ", self.assumedValues[i]

    def getHash(self):
        return (tuple(self.assumedVariables),tuple(self.assumedValues))

    def chooseVariable(self):
        #print self.domains
        #print self.assumedVariables
        posVar = filter(lambda var: var not in self.assumedVariables, self.domains)
        variable = min(posVar, key = lambda var: len(self.domains[var]))
        #print posVar
        #print variable
        return variable

    def expand(self):
        from GAC import GACrerun
        successors = []
        '''for variable in self.domains:
            if variable not in self.assumedVariables:
                singleDomains = self.domains[variable]
                break
                '''
        varToAssume = self.chooseVariable()
        #print "To assume: ",varToAssume
        singleDomains = self.domains[varToAssume]
        #print "Single domains", singleDomains
        for i in range(len(singleDomains)):
            newDomains = deepcopy(self.domains)
            newDomains[varToAssume]=[singleDomains[i]]
            newAssumedVariables = deepcopy(self.assumedVariables)
            newAssumedVariables.append(varToAssume)
            newAssumedValues = deepcopy(self.assumedValues)
            newAssumedValues.append(i)
            successor = Node(newDomains,self.g+1,self,varToAssume, newAssumedVariables, newAssumedValues)
            successor.domains = GACrerun(successor)
            #returns False if is empty domain
            if successor.domains:
                #print successor.domains
                successors.append(successor)
            children = successors
        return successors
