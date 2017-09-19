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

    def toString(self):
        print "Variable: ", self.variable
        print "Parent: ", self.parent
        print "Domains: ", self.domains
        for i in range (len(self.assumedVariables)):
            print self.assumedVariables[i], ": ", self.assumedValues[i]

    def getHash(self):
        return (tuple(self.assumedVariables),tuple(self.assumedValues))

    def expand(self):
        from GAC import GACrerun
        successors = []
        for variable in self.domains:
            if variable not in self.assumedVariables:
                singleDomains = self.domains[variable]
                break
        for i in range(len(singleDomains)):
            newDomains = deepcopy(self.domains)
            newDomains[variable]=[singleDomains[i]]
            newAssumedVariables = deepcopy(self.assumedVariables)
            newAssumedVariables.append(variable)
            newAssumedValues = deepcopy(self.assumedValues)
            newAssumedValues.append(i)
            successor = Node(newDomains,self.g+1,self,variable, newAssumedVariables, newAssumedValues)
            successor.domains = GACrerun(successor)
            #returns False if is empty domain
            if successor.domains:
                successors.append(successor)
        return successors
