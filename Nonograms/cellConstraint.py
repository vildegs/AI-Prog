

class Cell(Constraint):
    x = 0
    y = 0

    def __init__(self, x, y, variables):
        Constraint.__init__(self,variables)
        self.x= x
        self.y = y

    def isValid(self, var, domains, variables):
        dir, index, segnum, lenght = var
        #column
        if dir == 1:
            segX =

        domain = domains[var]
        for value in domain:
