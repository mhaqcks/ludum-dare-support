import pyglet
from level import ComicLevel
import config


def main():
    window = pyglet.window.Window(width=config.WIDTH, height=config.HEIGHT)

    level = ComicLevel('test_comic')

    @window.event
    def on_draw():
        window.clear()
        level.process()

    pyglet.app.run()


if __name__ == '__main__':
    main()

