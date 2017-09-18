

class Astar:

    heuristic=heuristic
    isSolution=None

    def __init__(self, heuristic,isSolution):
        self.heuristic=heuristic
        self.isSolution=isSolution

    def astar(self,start, goal):
        print("A*")
        opened = dict()
        closed = dict()
        #currentHash = start.getHash()
        opened[start.getID())=start
        while opened:
            current = opened[min(opened, key = lambda n: opened[n].g + opened[n].h)]
            currentHash = current.getHash()
            if self.isSolution(current,goal):
                return constructPath(current), len(closed)
            opened.pop(currentHash)
            closed[currentHash]=current
            children = current.expand()
            for (key, node) in children:
                #nodeHash = node.getHash()
                if key in closed:
                    #TODO update if lower values, children aswell
                    print("Already expanded and closed")
                elif key in opened:
                    newG = current.g + 1
                    if node.g > newG:
                        node.g = newG
                        node.parent = current
                else:
                    node.g = current.g +1
                    node.h = self.heuristic(node, goal)
                    node.parent = current
                    opened[nodeHash]= node
        return [], len(closed)


    def constructPath(self,current):
        path = []
        while current.parent:
            path.append(current)
            current = current.parent
        #get out the whole node
        path.append(current)
        #reverse the list, quicker than .reverse()
        return path[::-1]

    def heuristic(self, node, goal):
        return 0
