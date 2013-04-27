import pyglet
from level import ComicLevel
import config

class LevelDriver(object):
    def __init__(self, initial_level):
        self.level = initial_level
        self.level.driver = self
        self.levels = {}

    def register_level(self, name, level):
        self.levels[name] = level

    def change_level(self, level_name):
        self.level = self.levels[level_name]
        self.level.begin(self)

    def process(self):
        self.level.process()

def main():
    window = pyglet.window.Window(width=config.WIDTH, height=config.HEIGHT)

    level = ComicLevel('test_comic')

    driver = LevelDriver(level)
    driver.register_level('credits', level)

    @window.event
    def on_draw():
        window.clear()
        driver.process()

    pyglet.app.run()


if __name__ == '__main__':
    main()

