import static
from astarGeneral import Astar

class RushHour(Astar):

    def __init__(self):
        super(RushHour, self).__init__()

    def isSolution(self, node, goal):
        return node.positions[0]==goal

    def heuristic(self, node, goal):
        h = 0
        #Adds the number of moves from current position to the goal
        h+=goal-node.positions[0]
        #add the number of blocked spaces on way to goal
        for i in range(node.positions[0]+static.lengths[0],len(node.board)):
            if node.board[static.constantPos[0]][i] != '.':
                h +=1
        return h

    def astar(self, root, goal):
        return super(RushHour,self).astar(root, goal)
