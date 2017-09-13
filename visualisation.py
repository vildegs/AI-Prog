import pygame, random, sys
from pygame.locals import *
from collections import Counter
import static
pygame.font.init()

class Visualisation:
    def __init__(self, positions, pathLength, nodesExpanded, tile=80):
        self.positions = positions
        self.tile = tile
        self.pathLength = pathLength
        self.nodesExpanded=nodesExpanded
        self.width = 6 * self.tile
        self.colors = self.get_colors()

        # initialize pygame and window
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_caption('Rush Hour')
        self.window.fill((255, 255, 255))
        self.draw_board(positions[0])
        pygame.display.update()

        # pause visualisation (wait for input)

        myfont = pygame.font.Font(pygame.font.get_default_font(), 60)
        textsurface1 = myfont.render('Press enter', True, (0, 0, 0))
        textsurface2 = myfont.render('to start', True,(0,0,0))
        self.window.blit(textsurface1,(60,80))
        self.window.blit(textsurface2,(60,140))
        self.pause()

        # start visualisation
        self.run()


    def get_colors(self):
        """
        creates random colors for each vehicle (except for the main vehicle)
        :param board: board representation from root node
        :return: dictionary containing colors
        """

        indexes =[(255, 0, 0)]
        for index in range(1,static.numCars):
            indexes.append ((130 + int(random.random() * 60), int(random.random() * 256), int(random.random() * 256)))

        return indexes

    def run(self):
        """
        start the visualisation, which will pause after completing
        """

        # iterate over the moves in the solution

        while len(self.positions)>0:
            self.window.fill((255, 255, 255))
            self.draw_board(self.positions.pop(0))
            pygame.display.update()
            pygame.time.wait(300)

        myfont =pygame.font.Font(pygame.font.get_default_font(), 60)
        myfont2 =pygame.font.Font(pygame.font.get_default_font(), 40)
        textsurface1 = myfont.render('FINITO', True, (0, 0, 0))
        textsurface2 = myfont2.render('Length of path: '+str(self.pathLength), True,(0,0,0))
        textsurface3 = myfont2.render('Nodes expanded: '+str(self.nodesExpanded), True,(0,0,0))
        self.window.blit(textsurface1,(60,80))
        self.window.blit(textsurface2,(60,140))
        self.window.blit(textsurface3, (60,200))
        pygame.display.update()
        self.pause
        # wait for input to quit
        while True:

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN:
                    self.exit()

    def draw_board(self, positions):
        """
        draw the current vehicles on the window
        """
        for i in range(static.numCars):
            length = static.lengths[i]
            pos = positions[i]
            fixedPos = static.constantPos[i]

            # draw horizontally orientated vehicles
            if static.orientations[i] ==0:
                pygame.draw.rect(self.window, self.colors[i], (pos*self.tile , fixedPos*self.tile,
                                                                   length *self.tile, self.tile))
            # draw vertically orientated vehicles
            else:
                pygame.draw.rect(self.window, self.colors[i], (fixedPos* self.tile, pos * self.tile,
                                                                   self.tile, length*self.tile))
    def check_input(self):
        """
        checks for input which pauses or quits the visualisation
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.exit()
                self.pause()


    def exit(self):
        """
        quit the visualisation
        """
        pygame.quit()
        sys.exit()

    def pause(self):
        """
        pause the visualisation, wait for input
        """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.exit()
                    return False
