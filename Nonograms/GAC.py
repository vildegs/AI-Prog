
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
    #printQueue()
    printDomains(domains)

    GACDomainFilteringLoop()
    #printQueue()
    print ""
    printDomains(domains)

    #check is the current state is a solution, each domain has only one value
    #if not: do A*-search, having the root = current state
    #astar(root, goal)

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
        print "Changed"
        print var
        print("new: ",newDomain)
        print("old: ", domains[var])

    domains[var]=newDomain
    return isReduced




def GACrerun():
    print ""
