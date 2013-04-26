'''
This module contains the 'Level' class which should represent a major element of the game.  In the most basic of games there should probably be 3 levels.  The main menu, the level, and the credits?  This class shall dictate how various items should be rendered to the screen, leveraging other libraries and modules as much as possible.
'''
import pyglet

class Level(object):
    def __init__(self):
        self.agents = []
        self.batch = pyglet.graphics.Batch()

    def add_agent(self, agent):
        self.agents += [agent]
        agent.level = self

    def draw(self):
        for agent in self.agents:
            agent.draw()
