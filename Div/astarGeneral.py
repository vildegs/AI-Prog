class Astar(object):

    def __init__(self):
        pass

    def astar(self,start, goal):
        print "Starting A*"
        opened = dict()
        closed = dict()
        #initializing start state
        start.g = 0
        start.h = self.heuristic(start, goal)
        start.f = start.g + start.h
        #
        opened[start.getHash()]=start
        print "Looking for solution..."
        while opened:
            #take the node with the minimum f-value
            current = opened[min(opened, key = lambda n: opened[n].f)]
            #check if we found a solution
            if self.isSolution(current,goal):
                return self.constructPath(current), len(closed)
            del opened[current.getHash()]
            closed[current.getHash()]=current
            #creating successors by expanding the current node
            successors = current.expand()
            for successor in successors:
                current.addChild(successor)
                if not successor.getHash() in closed and not successor.getHash() in opened:
                    successor = self.attachandeval(current, successor)
                    opened[successor.getHash()]=successor
                #found cheaper path to successor
                elif successor.g > current.g + self.arccost(current,successor):
                    successor = self.attachandeval(current, successor)
                    if successor.getHash() in closed:
                        self.propagatepathimprovements(child)
                    '''
                if successor.getHash() in closed:
                    newG = current.g + 1
                    if successor.g > newG:
                        successor.updateChildren(newG)
                if successor.getHash() in opened:
                    newG = current.g + 1
                    if successor.g > newG:
                        successor.g = newG
                        successor.parent = current
                        opened[successor.getHash()]=successor
                    '''
        return [], len(closed)

    def attachandeval(self, current, child):
        child.parent = current
        child.g = current.g + self.arccost(current, child)
        child.h = self.heuristic(child,goal)
        child.f = child.g + child.h

    def propagatepathimprovements(current):
        for child in current.children:
            if current.g + self.arccost(current,child) < child.g:
                child.parent = current
                child.g = current.g + arccost(current, child)
                self.propagatepathimprovements(child)

    def constructPath(self,current):
        path = []
        while current.parent:
            path.append(current)
            current = current.parent
        #get out the whole node
        path.append(current)
        #reverse the list, quicker than .reverse()
        return path[::-1]
