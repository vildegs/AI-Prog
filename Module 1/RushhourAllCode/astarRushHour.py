import static
from astarGeneral import Astar

class RushHour(Astar):

    def __init__(self):
        #the goal is the goal position for the car-0
        self.goal = 4
        super(RushHour, self).__init__()

    def isSolution(self, node, goal):
        #check if the position of car-0 is the goal position
        return node.positions[0]==goal

    def heuristic(self, node, goal):
        h = 0
        #Add the number of spaces from current position to the goal position
        h+=goal-node.positions[0]
        #add the number of blocked spaces on way to goal
        for i in range(node.positions[0]+static.lengths[0],len(node.board)):
            if node.board[static.constantPos[0]][i] != '.':
                h +=1
        return h

    #the arccost going from a parent to a child is 1 move, so the cost is 1
    def arccost(self, parent, child):
        return 1

    #calls to the general astar algorithm
    def astar(self, root, goal):
        return super(RushHour,self).astar(root, self.goal)
