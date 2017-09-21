from copy import deepcopy


class Node:

    def __init__(self, domains, variable = None, g = 0, h=0, parent =None, state= True):
        self.g = g
        self.h = h
        self.f = self.h + self.g
        self.parent = parent
        self.domains = domains
        self.variable = variable
        self.state = state
        self.setVariables = []
        self.setValues = []
        for variable in self.domains:
            if len(self.domains[variable])==1:
                self.setVariables.append(variable)
                self.setValues.append(self.domains[variable][0])
        self.children = []

    def toString(self):
        print "Variable: ", self.variable
        print "Parent: ", self.parent
        print "Domains: ", self.domains
        print "f-value",self.g + self.h
        for i in range (len(self.setVariables)):
            print self.setVariables[i], ": ", self.setValues[i]

    def getHash(self):
        return (tuple(self.setVariables),tuple(self.setValues))

    def addChild(self, child):
        self.children.append(child)

    def chooseVariable(self):
        posVar = filter(lambda var: var not in self.setVariables, self.domains)
        variable = min(posVar, key = lambda var: len(self.domains[var]))
        return variable

    def expand(self):
        from GAC import GACrerun
        successors = []
        varToAssume = self.chooseVariable()
        singleDomains = self.domains[varToAssume]
        for i in range(len(singleDomains)):
            newDomains = deepcopy(self.domains)
            newDomains[varToAssume]=[singleDomains[i]]

            successor = Node(newDomains,varToAssume)
            successor.domains = GACrerun(successor)
            #returns False if is empty domain
            if successor.domains:
                successors.append(successor)
        return successors
