

class Astar(object):

    def __init__(self):
        pass

    def astar(self,start, goal):
        print "Starting A*"
        opened = dict()
        closed = dict()
        start.h = self.heuristic(start, goal)
        current = start
        opened[start.getHash()]=start
        print "Looking for solution..."
        while opened:
            current = opened[min(opened, key = lambda n: opened[n].g + opened[n].h)]
            if self.isSolution(current,goal):
                return self.constructPath(current), len(closed)
            del opened[current.getHash()]
            closed[current.getHash()]=current
            successors = current.expand()
            for node in successors:
                if node.getHash() in closed:
                    newG = current.g + 1
                    if node.g > newG:
                        node.updateChildren(newG)
                if node.getHash() in opened:
                    newG = current.g + 1
                    if node.g > newG:
                        node.g = newG
                        node.parent = current
                        opened[node.getHash()]=node
                else:
                    #TODO remove in both
                    node.g = current.g +1
                    node.h = self.heuristic(node, goal)
                    node.parent = current
                    opened[node.getHash()]=node
        return [], len(closed)
        '''
    def astar(self,start, goal):
        opened = dict()
        closed = dict()
        start.h = self.heuristic(start, goal)
        current = start
        opened[start.getHash()]=start
        while opened:
            current = opened[min(opened, key = lambda n: opened[n].g + opened[n].h)]
            self.printOpened(opened)
            print "Chosen"
            print current.h
            print current.g
            if self.isSolution(current,goal):
                return self.constructPath(current), len(closed)
            del opened[current.getHash()]
            closed.add(current)
            successors = current.expand()
            for node in successors:
                if node in closed:
                    #TODO update if lower values, children aswell
                    continue
                if node.getHash() in opened.keys():
                    newG = current.g + 1
                    if node.g > newG:
                        node.g = newG
                        node.parent = current
                        opened[node.getHash()]=node
                else:
                    node.g = current.g +1
                    node.h = self.heuristic(node, goal)
                    node.parent = current
                    opened[node.getHash()]=node
        return [], len(closed)
        '''
    def printOpened(self,opened):
        for item in opened:
            print item
            print opened[item].g
            print opened[item].h

    def constructPath(self,current):
        path = []
        while current.parent:
            path.append(current)
            current = current.parent
        #get out the whole node
        path.append(current)
        #reverse the list, quicker than .reverse()
        return path[::-1]
