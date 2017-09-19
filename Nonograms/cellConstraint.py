
from constraint import Constraint

class Cell(Constraint):
    x = 0
    y = 0

    def __init__(self, x, y, variables):
        Constraint.__init__(self,variables)
        self.x= x
        self.y = y

    def toString(self):
        print ""
        print "CellConstraint"
        print "Cell: (",self.x,",",self.y,")"
        print "Variables: ",self.variables

    def isValid(self, variable, value, domains):

        #check if var in col or row
        roworcol = variable[0]
        rowcolIndex = variable[1]
        #print "Var to reduce domain",variable
        #print "Domain value to check", value
        if roworcol == 0:
            if value != self.x:
                return True
        if roworcol == 1:
            if value != self.y:
                return True

        #if it is valid, it has to check the corresponding row/col
        #taking out the variables to check
        toCheck = filter (lambda var: var[0]!=roworcol, self.variables)
        #goes through all of the ones in the same row/col and check if one of them can fill the row/col
        #print "Variable: ", variable
        #print "Value: ", value
        for var in toCheck:
            #print "Var",var
            #print domains[var]
            length = var[3]
            for posStart in domains[var]:
                if posStart <= rowcolIndex and rowcolIndex < posStart+length:
                    #print posStart
                    return True
        return False
