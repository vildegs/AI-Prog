

class Rowcolconstraint(Constraint):
    index = None
    def __init__(self, index, variables):
        Constraint.__init__(self.variables)
        self.index  =index

    def isValid(variable, value, domains):
        segNr = variable[2]
        left = variables[:segNr]
        right = variables[segNr+1:]
        for var in left:
            domain = domains[var]
            valid = False
            for val in domain:
                if val+var[3]<value:
                    valid = True
                    break
            if valid ==False:
                return False
        for var in right:
            domain = domains[var]
            valid = False
            for val in domain:
                if val=var[3]>value+variable[3]:
                    valid = True
                    break
            if valid ==False:
                return False
        return valid





def domain(index, segments, sumSegments, numSegments, id):
    if id ==1:
        length = numcols
    else:
        length = numrows
    #first
    '''if index == 0:
        dom = [i for i in range(length-numSegments-sumSegments)]
    #last
    elif index == numSegments-1:
        dom = [i for i in range(sumSegments+numSegments-segments[index]-1,length-segments[index]+1)]
    #other
else:'''
    left = segments[:index]
    right = segments[index+1:]
    leftlim = sum(left)+len(left)
    rightlim = length-(sum(right)+len(right))-segments[index]+1
    dom = [i for i in range(leftlim, rightlim)]
    return dom
