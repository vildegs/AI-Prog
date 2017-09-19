from copy import deepcopy


class Node:
    variable = None
    g = 0
    h = 0
    parent = None
    domains = {}

    def __init__(self, parent, domains, variable):
        self.parent = parent
        self.domains = domains
        self.variable = variable
        '''
    def getHash(self):
        print "Tuple: ", self.domains.values()
        return tuple(self.domains.values())
        '''''
    def getHash(self):
        hash = []
        for variable, domain in self.domains.iteritems():
            if len (domain)==1:
                hash.append(variable)
        return tuple(hash)

    def expand(self):
        from GAC import GACrerun
        successors = []
        for variable in self.domains:
            if (len(self.domains[variable]))>1:
                singleDomains = self.domains[variable]
                break
        for i in range(len(singleDomains)):
            newDomains = deepcopy(self.domains)
            newDomains[variable]=[singleDomains[i]]
            successor = Node(self,newDomains,variable)
            successor.domains = GACrerun(successor)
            #returns False if is empty domain
            if successor.domains:
                successors.append(successor)
        return successors
