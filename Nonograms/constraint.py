
class Constraint:

    variables = None

    def __init__(self, variables):
        self.variables = variables

    def getVariablesAffected(variable):
        return filter(lambda i: i!=variable, self.variables))
