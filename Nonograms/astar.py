
def astar(root, goal):
    current = root

    #make assumptions to create successor states
    children = expand()
    for state in children:
        GAC-rerun(state)
        #calculate the f, g and h values for the children states

def heuristic():
    #calculate the size of each domain minus one
    #sum these
    return #the sum

#how can we have an input goal
def isSolution(goal):
    for varDom in domains:
        if varDom != 1:
            return False
    return True


def expand():
    #list of successor states, do not have to reduce the other domains here
    #the domain of the assumed variable is reduced to a singleton set
    return
