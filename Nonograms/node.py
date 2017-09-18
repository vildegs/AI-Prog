

class Node:
    g = 0
    h = 0
    parent = None
    domains = {}

    def __init__(self, parent, domains, g):
        self.parent = parent
        self.domains = domains
        self.g = g

    def expand(self):
        successors = []
        for variable in domains:
            if (domains[variable])>1:
                singleDomains = domains[variable]
                break
        for i in range(len(singleDomains)):
            newDomains = domains
            newDomains[variable]=singleDomains[i]
            successor = Node(self,newDomains,self.g+1)
            successors.append(successor)

        return successors
