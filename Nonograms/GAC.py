
queue = []
variables = []
constraints = []
domains = {}

#takes in the variables, domains and constraint for the problem
def gac(var, dom, cons):
    global variables, queue, constraints, domains
    #the domain
    #TODO Initialization
    #A set of revises to do
    #Each revise contain an variable Xij and an contraint Ci
    #i is the number of the constraint and j the number of variable X is in Ci
    variables = var
    constraints = cons
    domains = dom
    queue = GACinitialize(variables, constraints)
    print("KO",len(queue))
    #printQueue()
    printDomains(domains)

    GACDomainFilteringLoop()
    #printQueue()
    print " "
    printDomains(domains)

    #check is the current state is a solution, each domain has only one value
    #if not: do A*-search, having the root = current state
    astar(domains, goal)

def astar(root, goal):
    current = root
    opened = set()
    closed = set()
    #make assumptions to create successor states
    children = expand()
    for state in children:
        GAC-rerun(state)
        #calculate the f, g and h values for the children states

opened = dict()
closed = dict()
#currentHash = start.getHash()
opened[start[0]]=start[1]
while opened:
    current = opened[min(opened, key = lambda n: opened[n].g + opened[n].h)]
    currentHash = current.getHash()
    if isSolution(current,goal):
        return constructPath(current), len(closed)
    opened.pop(currentHash)
    closed[currentHash]=current
    children = current.expand()
    for (key, node) in children:
        #nodeHash = node.getHash()
        if key in closed:
            #TODO update if lower values, children aswell
            print("Already expanded and closed")
        elif key in opened:
            newG = current.g + 1
            if node.g > newG:
                node.g = newG
                node.parent = current
        else:
            node.g = current.g +1
            node.h = heuristic(node, goal)
            node.parent = current
            opened[nodeHash]= node
return [], len(closed)
def heuristic():
    #calculate the size of each domain minus one
    #sum these
    return 0

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

def printVariables():
    for var in variables:
        print var

def printDomains(domains):
    for key in domains.keys():
        print (key, domains[key])

def printConstraints():
    for constraint in constraints:
        constraint.toString()

def printQueue():
    count =1
    for (var, cons) in queue:
        print (count," Var: ", var, "Constraint: ", cons)
        count +=1

#combine variables and constraints
def GACinitialize(variables, constraints):
    for constraint in constraints:
        for var in variables:
            if constraint.hasVar(var):
                queue.append((var,constraint))
    return queue

def emptyDomains(domains):
    for (var, domain) in domains:
        if len(domain)==0:
            return True
    return False

def GACDomainFilteringLoop():
    counter = 0
    while queue:
        #print counter
        counter +=1
        (variable, constraint) = queue.pop(0)
        isReduced = revise(variable,constraint)
        if isReduced:
            affectedVar = constraint.getVariablesAffected(variable)
            for i in range(len(affectedVar)):
                todoRevise = (affectedVar[i],constraint)
                if todoRevise not in queue:
                    queue.append(todoRevise)
            for i in range (len(constraints)):
                if constraints[i].hasVar(variable):
                    todoRevise = (variable, constraints[i])
                    if todoRevise not in queue:
                        queue.append(todoRevise)

            #push todorevise(Xkm,Ck) to queue for all Ck (k!=i) where X* appears and all Xk,m != X*

#remove all x in the domain of the variable where there are no (x,y) that satisfy the constraint
def revise(var, constraint):
    global domains
    domain = domains[var]
    newDomain =[]
    isReduced = False
    for value in domain:
        if constraint.isValid(var, value, domains):
            newDomain.append(value)
        else:
            isReduced =True

    if newDomain!=domains[var]:
        print constraint
        print "Changed"
        print var
        print("new: ",newDomain)
        print("old: ", domains[var])
    else:
        print constraint
        print "Not Changed"

    domains[var]=newDomain
    return isReduced

def GACrerun():
    print ""
