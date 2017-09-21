
from astarNonograms import Nonogram

queue = []
variables = []
constraints = []
domains = {}
search = Nonogram()
astar = search.astar
goal =1

#takes in the variables, domains and constraint for the problem
def gac(var, dom, cons):
    global variables, queue, constraints, domains
    variables = var
    constraints = cons
    domains = dom
    #initializes the queue by coupling variables and constraints
    queue = GACinitialize(variables, constraints)
    #running the domain filtering loop
    GACDomainFilteringLoop()
    from node import Node
    root = Node (domains)
    return astar(root, goal)


#combine variables and constraints
def GACinitialize(variables, constraints):
    for constraint in constraints:
        for var in variables:
            if constraint.hasVar(var):
                queue.append((var,constraint))
    return queue

def emptyDomains(domains):
    for variable in domains:
        if len(domains[variable])==0:
            return True
    return False

def GACDomainFilteringLoop():
    #revise the variable-constraint pairs until the queue is empty
    while queue:
        (variable, constraint) = queue.pop(0)
        isReduced = revise(variable,constraint)
        #in the domain for the variable was reduced
        #the affected variable-constraint pairs is added to the queue
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


#remove all x in the domain of the variable where there are no (x,y) that satisfy the constraint
def revise(var, constraint):
    global domains
    domain = domains[var]
    newDomain =[]
    isReduced = False
    #check whether or not a domain value is valid for a given variable
    for value in domain:
        if constraint.isValid(var, value, domains):
            newDomain.append(value)
        else:
            isReduced =True
    #updates the potentially reduced domain for the variable
    domains[var]=newDomain
    return isReduced

#the rerun function is called from astar
#it is called with a node where a variable is assumed
def GACrerun(node):
    global domains, queue
    queue = []
    domains = node.domains
    #TODO: convering
    #all of the constraints which are attached to the variable assumed
    #is coupled to all of its other variables and added to the queue
    for otherVar in variables:
        for constraint in constraints:
            if constraint.hasVar(otherVar) and otherVar != node.variable and constraint.hasVar(node.variable):
                queue.append((otherVar, constraint))
    #with the queue made, the domain filtering loop runs
    GACDomainFilteringLoop()
    #check if any of the domains are empty after the filtering loop
    #if it is, the node is a dead end
    if emptyDomains(domains):
        domains = False
    return domains
