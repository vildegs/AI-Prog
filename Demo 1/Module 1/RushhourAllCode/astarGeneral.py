import static
import random
from Tkinter import *

master = Tk()
canvas = Canvas(master, width=600, height=600)
canvas.pack()
text  = Text(master)

indexes = []

class Astar(object):
    def __init__(self):
        pass

    def astar(self,start, goal):
        #opened and closed are dictionaries to use hashing
        opened = dict()
        closed = dict()

        #initializing start state
        start.g = 0
        start.h = self.heuristic(start, goal)
        start.f = start.g + start.h

        #putting the start node in the opened queue
        opened[start.getHash()]=start

        #as long as we have more nodes to expand
        while opened:
            #take the node with the minimum f-value
            current = opened[min(opened, key = lambda n: opened[n].f)]
            self.vis(current)
            #check if the current node is a  solution, if it is it return the path
            if self.isSolution(current,goal):
                return self.constructPath(current), len(closed)
            #removes the current node from opened
            del opened[current.getHash()]
            #add the node to closed
            closed[current.getHash()]=current
            #update the state of the current node to closed
            current.state=False
            #creating successors by expanding the current node
            successors = current.expand()
            for successor in successors:
                #check if the successor already has been created and the state is the same
                #if it is, it sets successor = successor*
                #where successor* is the node previously created
                if (successor.getHash() in opened and successor.state) or (successor.getHash() in closed and not successor.state):
                    #successor* in opened
                    if successor.state:
                        successor = opened[successor.getHash()]
                    #successor* in closed
                    else:
                        successor = closed[successor.getHash()]
                #add the successor to current node's children
                current.addChild(successor)
                #if the successor has not been created, it is assigned values and parent
                if (not successor.getHash() in closed) and (not successor.getHash() in opened):
                    self.attachandeval(current, successor)
                    #add the successor to opened
                    opened[successor.getHash()]=successor
                #if it finds a cheaper path to successor, it reevalute the successor
                elif successor.g > current.g + self.arccost(current,successor):
                    self.attachandeval(current, successor)
                    #if the successor has already been expanded, it has to update its childrens g-values aswell
                    if successor.getHash() in closed:
                        self.propagatepathimprovements(successor)
        return [], len(closed)

    def attachandeval(self, current, child):
        #attaches the child to its parent
        child.parent = current
        #calculate the g, h and f values for the child
        child.g = current.g + self.arccost(current, child)
        child.h = self.heuristic(child,self.goal)
        child.f = child.g + child.h

    def propagatepathimprovements(current):
        for child in current.children:
            #if any of the children has a greater g value than the new g value
            #for the parent plus the arccost, it updates the value and parent
            #and reevaluates its children
            if current.g + self.arccost(current,child) < child.g:
                child.parent = current
                child.g = current.g + arccost(current, child)
                self.propagatepathimprovements(child)

    #goes through all of the nodes from solution to root and add them to the path
    def constructPath(self,current):
        path = []
        while current.parent:
            path.append(current)
            current = current.parent
        #add the root node
        path.append(current)
        #reverse the list so the first node is the root (quicker than .reverse())
        return path[::-1]


    def vis(self, current):
        global indexes
        if len(indexes)==0:
            indexes =["#ff0000"]
            for index in range(1,static.numCars):
                indexes.append ("#"+("%06x"%random.randint(0,16777215)))
        self.createboard(current)
        master.update_idletasks()
        master.update()
        master.after(100)

    def createboard(self, node):

        board = [[-1 for i in range(6)] for j in range(6)]

        for i in range(len(node.positions)):
            if static.orientations[i] ==0:
                for j in range (static.lengths[i]):
                    board[static.constantPos[i]][node.positions[i]+j] = i
            else:
                for j in range (static.lengths[i]):
                    board[node.positions[i]+j][static.constantPos[i]] = i
        self.drawboard(board)

    def drawboard(self, board):
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                self.drawCell(board, row, col)


    def drawCell(self, board, row, col):
        margin = 5
        cellSize = 30
        left = margin + col * cellSize
        right = left + cellSize
        top = margin + row * cellSize
        bottom = top + cellSize
        canvas.create_rectangle(left, top, right, bottom, fill="white")
        if (board[row][col] > -1):
            # draw part of the snake body
            canvas.create_rectangle(left, top, right, bottom, fill=indexes[board[row][col]])
