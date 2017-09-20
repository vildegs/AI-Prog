
class Constraint:

    def __init__(self, variables):
        self.variables = variables

    def getVariablesAffected(self,variable):
        return filter(lambda i: i!=variable, self.variables)

    def hasVar(self, variable):
        for var in self.variables:
            if var == variable:
                return True
        return False
