'''
This module contains the agent class which is a basic element of the game that can be processed and rendered (if necessary).  The player character, if such a perversion exists, would appear in the form of an Agent.  Scores, mouse pointer(s), NPCs, vidja, etc. also would appear in the form of agents.
'''
import graphics


class Agent(object):
    def __init__(self):
        self.level = None

    def draw(self):
        pass


class SpriteAgent(Agent):
    def __init__(self):
        pass

    def draw(self):
        pass

class TextAgent(Agent):
    def __init__(self):
        self.text = graphics.text('')

    def draw(self):
        self.text.draw()
