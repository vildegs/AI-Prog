
from constraint import Constraint
counter = 0

class RowCol(Constraint):
    index = None
    def __init__(self,roworcol,index, variables):
        Constraint.__init__(self, variables)
        self.roworcol = roworcol
        self.index = index

    def toString(self):
        print ""
        print "RowColConstraint"
        if self.roworcol == 0:
            print "Row: ", self.index
        else:
            print "Col: ", self.index
        print "Variables: ", self.variables

    def isValid(self,variable, value, domains):
        toCheck = self.variables

        segNr = variable[2]

        #checking with the segment before
        if segNr !=0:
            before = toCheck[segNr-1]
            valid = False
            for i in domains[before]:
                if value > i + before[3]:
                    valid = True
                    break
            if valid == False:
                return False

        #checking with the next segment
        if segNr < len(toCheck)-1:
            after = toCheck[segNr+1]
            valid = False
            for i in domains[after]:
                if value + variable[3] < i:
                    valid = True
                    break
            if valid == False:
                return False
        #if it is the only segment in this row/col
        return True

    def printDomains(self,domains):
        print "printing domains"
        for variable, domain in domains.iteritems():
            print variable
            print domain
