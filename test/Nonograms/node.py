from copy import deepcopy


class Node:

    def __init__(self, domains, setVariables = [], setValues  =[], variable = None, parent =None, state= True, g= 0, h = 0):
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.parent = parent
        self.domains = domains
        self.variable = variable
        self.state = state
        self.setVariables = setVariables
        self.setValues = setValues
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

    def setVarAndVal(self, domains):
        variables, values = [], []
        for variable in domains:
            if len (domains[variable])==1:
                variables.append(variable)
                values.append(domains[variable][0])
        return variables, values

    def expand(self):
        from GAC import GACrerun
        successors = []
        varToAssume = self.chooseVariable()
        singleDomains = self.domains[varToAssume]
        for i in range(len(singleDomains)):
            newDomains = deepcopy(self.domains)
            newDomains[varToAssume]=[singleDomains[i]]
            #newValues.append(singleDomains[i])
            successor = Node(newDomains,[], [],varToAssume)
            #newValues.pop()
            successor.domains = GACrerun(successor)
            #returns False if is empty domain
            variables, values = self.setVarAndVal(newDomains)
            successor.setVariables=variables
            successor.setValues = values
            if successor.domains:
                successors.append(successor)
        return successors
