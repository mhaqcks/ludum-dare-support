import graphics
from level import Level
import agent
from math import floor
import pyglet

import logging
logging.basicConfig(level=loggin.DEBUG)


if __name__ == '__main__':
    import argparse

    graphics.setup()

    pyglet.gl.glClearColor(1, 1, 1, 1)

    level = Invaders()

    graphics.set_level(level)

    parser = argparse.ArgumentParser()
    parser.parse_args()

    graphics.go()

