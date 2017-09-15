
from constraint import Constraint

class RowCol(Constraint):
    index = None
    def __init__(self, dir,index, variables):
        Constraint.__init__(self, variables)
        self.index  =index

    def isValid(self,variable, value, domains):
        #return True
        toCheck = filter(lambda var : var[0]==variable[0] and var[1]==variable[1], self.variables)
        segNr = variable[2]
        #checking the segment before
        if segNr !=0:
            before = toCheck[segNr-1]
            valid = False
            for i in domains[before]:
                if value > i + before[3]:
                    valid = True
                    break
            if valid == False:
                return False
        #checking the next segment
        if segNr != len(toCheck)-1:
            after = toCheck[segNr+1]
            for i in domains[after]:
                if value < i:
                    valid = True
                    break
            if valid == False:
                return False
        #if it is the only segment in this row/col
        return True
