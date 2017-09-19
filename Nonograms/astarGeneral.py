

class Astar(object):

    def __init__(self):
        pass

    def astar(self,start, goal):
        opened = dict()
        closed = set()
        start.h = self.heuristic(start, goal)
        current = start
        opened[start.getHash()]=start
        while opened:
            current = opened[min(opened, key = lambda n: opened[n].g + opened[n].h)]
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
        return current, len(closed)

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
