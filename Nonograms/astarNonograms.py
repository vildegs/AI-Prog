
from astarGeneral import Astar

class Nonogram(Astar):

    def __init__(self):
        self.goal = 1
        super(Nonogram, self).__init__()

    def heuristic(self, node, goal):
        #calculate the size of each domain minus one
        #sum these
        h =0
        for variable, domain in node.domains.iteritems():
            #h= h + len(domain)-1
            x =0
        return h

    #how can we have an input goal
    def isSolution(self,node,goal):
        for domain in node.domains.values():
            if len(domain) != goal:
                return False
        return True

    def arccost(self, parent, child):
        return 1

    def astar(self, root, goal):
        return super(Nonogram,self).astar(root, goal)

    
