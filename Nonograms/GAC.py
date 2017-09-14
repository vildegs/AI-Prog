
#takes in the variables, domains and constraint for the problem
def gac(var, dom, cons):
    #the domain 
    #TODO Initialization
    #A set of revises to do
    #Each revise contain an variable Xij and an contraint Ci
    #i is the number of the constraint and j the number of variable X is in Ci
    queue = GAC-initialize(var, cons)

    #TODO Domain-Filtering Loop
    GAC-Domain-Filtering-Loop()

    #check is the current state is a solution, each domain has only one value
    #if not: do A*-search, having the root = current state
    astar(root, goal)

#combine variables and constraints
def GAC-initialize(variables, constraints):
    queue = []
    for contraint in constraints:
        for var in variables:
            if constraint.hasVar(var):
                queue.append(tuple(var,constraint))
    return queue


def GAC-Domain-Filtering-Loop():
    while queue:
        #todoRevise = (var, constraint)
        todoRevise = queue.pop(0)
        reduced = revise(variable,constraint)
        if reduced:
            #push todorevise(Xkm,Ck) to queue for all Ck (k!=i) where X* appears and all Xk,m != X*

#remove all x in the domain of the variable where there are no (x,y) that satisfy the constraint
def revise(var, constraint):
    return constraint.isValid()

def GAC-rerun():


'''1: Procedure GAC(V,dom,C)
2:           Inputs
3:                     V: a set of variables
4:                     dom: a function such that dom(X) is the domain of variable X
5:                     C: set of constraints to be satisfied
6:           Output
7:                     arc-consistent domains for each variable
8:           Local
9:                     DX is a set of values for each variable X
10:                     TDA is a set of arcs
11:           for each variable X do
12:                     DX ←dom(X)
13:           TDA ←{⟨X,c⟩| c∈C  and X∈scope(c)}
14:           while (TDA ≠{})
15:                     select ⟨X,c⟩ ∈TDA;
16:                     TDA ←TDA  \ {⟨X,c⟩};
17:                     NDX ←{x| x ∈DX and some {X=x,Y1=y1,...,Yk=yk}∈c where yi ∈DYi for all i}
18:                     if (NDX ≠DX) then
19:                               TDA ←TDA ∪{⟨Z,c'⟩|X ∈scope(c'), c' is not c, Z∈scope(c') \ {X} }
20:                               DX ←NDX
21:           return {DX| X  is a variable}
'''
