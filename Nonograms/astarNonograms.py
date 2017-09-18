from astarGeneral import Astar

class Nonogram(Astar):

    def __init__(self):
        Astar.__init__(self,self.heuristic,self.isSolution)
    '''
def astar(root, goal):
    current = root

    #make assumptions to create successor states
    children = current.expand()
    for state in children:
        GAC-rerun(state)
        #calculate the f, g and h values for the children states
'''
def heuristic():
    #calculate the size of each domain minus one
    #sum these
    h =0
    for domain in domains:
        h= h + len(domain)-1
    return h

#how can we have an input goal
def isSolution(goal):
    for domain in domains.values:
        if len(domain) != goal:
            return False
    return True
